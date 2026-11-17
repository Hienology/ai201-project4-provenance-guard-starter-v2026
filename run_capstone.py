#!/usr/bin/env python3
"""
The capstone runner: the five criteria in criteria.md ("Capstone criteria (Unit 9)").

Inside the GitHub Actions workflow (.github/workflows/capstone.yml), on each machine:

    python run_capstone.py run

It starts the service itself, runs Capstone 1, 4 and 5 on every machine, and
Capstone 3 and 2 on macOS only (in that order, 2 last because it uninstalls
libraries), then prints everything to the run's page: every request, its
response, the caller's wait and the new lines of logs/audit.jsonl. The last
line is one JSON object (CAPSTONE-RESULT) that `report` reads back.

Afterwards, on your own machine, with the GitHub CLI signed in:

    python run_capstone.py report --label before RUN_ID RUN_ID RUN_ID

builds results/capstone_run_<stamp>_<label>.md from the three runs' pages
(`gh run view --log`). The Verdict column stays blank: the student writes it.

This file never edits run_eval.py or scenarios.py, and never touches /ping.
"""

import argparse
import datetime as dt
import hashlib
import json
import os
import platform
import re
import subprocess
import sys
import time
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent
LOG = ROOT / "logs" / "audit.jsonl"
PORT = int(os.getenv("CAPSTONE_PORT", "5050"))   # 5000 can be held by macOS AirPlay
BASE = f"http://127.0.0.1:{PORT}"
AI1 = (ROOT / "samples" / "ai-1.txt").read_text(encoding="utf-8")
MADE_UP_ID = "00000000-0000-0000-0000-000000000000"
BAD_MODEL = "no-such-model-capstone"
SIX = ("content_id", "guess", "confidence", "label", "model_score", "style_score")

COLD_WAIT, WARM_WAIT = 60, 30      # seconds per attempt (student)
MAX_ATTEMPTS, PAUSE = 4, 5         # 1 + 3 retries, 5 s pause (student)
HEALTH_WAIT = 60                   # cap on the /health wait before a cold retry


# ── small helpers ─────────────────────────────────────────────────────────────

def say(*parts):
    print(*parts, flush=True)


def expected_input(text):
    """The student's definition: SHA-256 of the trimmed text + its word count."""
    sys.path.insert(0, str(ROOT))
    import stylometry
    if not isinstance(text, str) or not text.strip():
        return None
    t = text.strip()
    return {"sha256": hashlib.sha256(t.encode("utf-8")).hexdigest(),
            "words": len(stylometry.words(t))}


def log_lines():
    if not LOG.exists():
        return []
    return [json.loads(l) for l in LOG.read_text(encoding="utf-8").splitlines() if l.strip()]


def post(path, body=None, raw=None, timeout=WARM_WAIT):
    """One attempt. Returns status, parsed JSON (or None), caller's wait (ms, 3 dp), problem."""
    import requests
    t0 = time.perf_counter()
    try:
        if raw is not None:
            r = requests.post(BASE + path, data=raw, timeout=timeout,
                              headers={"Content-Type": "application/json"})
        else:
            r = requests.post(BASE + path, json=body, timeout=timeout)
    except requests.exceptions.Timeout:
        return {"status": None, "json": None, "wait_ms": round((time.perf_counter() - t0) * 1000, 3),
                "problem": "timeout"}
    except requests.exceptions.ConnectionError:
        return {"status": None, "json": None, "wait_ms": round((time.perf_counter() - t0) * 1000, 3),
                "problem": "connection refused"}
    wait = round((time.perf_counter() - t0) * 1000, 3)
    try:
        js = r.json()
    except ValueError:
        js = None
    return {"status": r.status_code, "json": js, "wait_ms": wait, "problem": None,
            "body_start": r.text[:120] if js is None else None}


def health():
    import requests
    try:
        return requests.get(BASE + "/health", timeout=5).json()
    except Exception:  # noqa: BLE001
        return None


def with_retries(path, body, timeout, cold):
    """
    The student's retry rule: retry only after a timeout, at most 4 attempts,
    a 5 s pause, and before a cold retry wait until /health says the model is
    loaded (up to 60 s). A refused connection is a FAIL with no retry.
    """
    attempts = []
    start = time.perf_counter()
    for n in range(1, MAX_ATTEMPTS + 1):
        a = post(path, body=body, timeout=timeout)
        a["attempt"] = n
        attempts.append(a)
        if a["problem"] != "timeout":
            break
        if n < MAX_ATTEMPTS:
            time.sleep(PAUSE)
            if cold:
                t_h = time.perf_counter()
                while time.perf_counter() - t_h < HEALTH_WAIT:
                    h = health()
                    if h and h.get("detector_loaded"):
                        break
                    time.sleep(1)
    span = round((time.perf_counter() - start) * 1000, 3)
    return attempts, span


# ── the service ───────────────────────────────────────────────────────────────

def start_server(extra_env=None, label="start"):
    env = dict(os.environ)
    env["PORT"] = str(PORT)
    env["AI201_DEBUG"] = "0"
    env.pop("AI201_DETECTOR_MODEL", None)
    if extra_env:
        env.update(extra_env)          # only this one process gets it (Capstone 2, point 4)
    proc = subprocess.Popen([sys.executable, "app.py"], cwd=ROOT, env=env,
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    t0 = time.perf_counter()
    while time.perf_counter() - t0 < 120:
        if proc.poll() is not None:
            say(f"[{label}] the server exited with code {proc.returncode}")
            return proc, False
        if health() is not None:
            say(f"[{label}] server up on port {PORT} (pid {proc.pid}); /health answers")
            return proc, True
        time.sleep(0.5)
    say(f"[{label}] /health did not answer within 120 s")
    return proc, False


def stop_server(proc):
    import psutil
    try:
        p = psutil.Process(proc.pid)
        for child in p.children(recursive=True):
            child.kill()
        p.kill()
    except psutil.NoSuchProcess:
        pass
    proc.wait(timeout=30)
    time.sleep(1)


def server_rss_mb(proc):
    """
    psutil's memory_info().rss of the `python app.py` process, in MB (10^6 bytes).
    On Windows a venv's python.exe starts the real interpreter as a child, so the
    process in the tree whose command line runs app.py with the most memory is used.
    """
    import psutil
    root = psutil.Process(proc.pid)
    best = None
    for p in [root] + root.children(recursive=True):
        try:
            if any(part.endswith("app.py") for part in p.cmdline()):
                rss = p.memory_info().rss
                if best is None or rss > best[0]:
                    best = (rss, p.pid)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    if best is None:
        return None, None
    return round(best[0] / 1_000_000, 3), best[1]


def entry_for(content_id, status="decided"):
    for e in log_lines():
        if e.get("content_id") == content_id and "event" not in e and e.get("status") == status:
            return e
    return None


def show(label, a, entry=None):
    """Print one request the way the results file shows it."""
    say(f"  {label}: status {a['status']}{' (' + a['problem'] + ')' if a['problem'] else ''}, "
        f"caller's wait {a['wait_ms']} ms")
    if a["json"] is not None:
        say(f"    response: {json.dumps(a['json'], ensure_ascii=False)}")
    elif a.get("body_start"):
        say(f"    response (not JSON): {a['body_start']!r}")
    if entry is not None:
        say(f"    log entry: {json.dumps(entry, ensure_ascii=False)}")


# ── Capstone 1, 4, 5 (every machine, server start #1) ─────────────────────────

def capstone_1(out):
    say("\n== Capstone 1: first start (cap-a) ==")
    attempts, span = with_retries("/submit", {"text": AI1, "creator_id": "cap-a"}, COLD_WAIT, cold=True)
    passing, entry = None, None
    for a in attempts:
        js = a["json"] or {}
        ok = (a["status"] == 200
              and all(k in js and js[k] is not None for k in SIX)
              and js.get("guess") == "ai")
        e = entry_for(js.get("content_id")) if a["status"] == 200 else None
        a["entry"] = e
        show(f"attempt {a['attempt']}", a, e)
        if ok and e is not None:
            passing, entry = a, e
            break
    out["c1"] = {"pass": passing is not None, "attempts": len(attempts),
                 "cold_span_ms": span if passing else None,
                 "content_id": (passing["json"] or {}).get("content_id") if passing else None,
                 "evidence": attempts}
    say(f"  -> Capstone 1 on this machine: {'PASS' if passing else 'FAIL'} "
        f"(attempts used: {len(attempts)}; caller's span {span} ms)")
    return out["c1"]


def capstone_4(out, proc):
    say("\n== Capstone 4: cost and speed (cap-d) ==")
    c1 = out["c1"]
    cold = c1["cold_span_ms"]
    say(f"  cold (caller's clock, Capstone 1 attempt 1 start -> passing attempt end): {cold} ms")
    warm = []
    for i in range(3):
        attempts, _ = with_retries("/submit", {"text": AI1, "creator_id": "cap-d"}, WARM_WAIT, cold=False)
        last = attempts[-1]
        e = entry_for((last["json"] or {}).get("content_id")) if last["status"] == 200 else None
        reading = e.get("duration_ms") if (e and last["status"] == 200) else None
        show(f"warm {i + 1} (attempts {len(attempts)})", last, e)
        warm.append({"status": last["status"], "duration_ms": reading, "attempts": len(attempts)})
    mem, pid = server_rss_mb(proc)
    say(f"  memory right after the third warm answer: {mem} MB "
        f"(psutil memory_info().rss of pid {pid}, 1 MB = 1,000,000 bytes)")
    warm_ok = sum(1 for w in warm if w["status"] == 200 and w["duration_ms"] is not None
                  and w["duration_ms"] <= 5000)
    passed = (c1["pass"] and cold is not None and cold <= 45000
              and warm_ok >= 2 and mem is not None and mem <= 900)
    out["c4"] = {"pass": passed, "cold_ms": cold, "warm": warm, "warm_under": warm_ok,
                 "memory_mb": mem, "c1_pass": c1["pass"]}
    say(f"  -> Capstone 4 on this machine: {'PASS' if passed else 'FAIL'} "
        f"(cold {cold} ms vs 45000; warm at most 5000 ms: {warm_ok} of 3; memory {mem} MB vs 900)")


def capstone_5(out):
    say("\n== Capstone 5: the old behaviour and the boundary (cap-e) ==")
    checks = {}

    def one(key, label, path, body=None, raw=None, expect_status=None, expect_error=None, extra=None):
        attempts, _ = with_retries(path, body, WARM_WAIT, cold=False) if raw is None else ([post(path, raw=raw)], 0)
        a = attempts[-1]
        js = a["json"] or {}
        ok = a["status"] == expect_status and (expect_error is None or js.get("error") == expect_error)
        if ok and extra:
            ok = extra(js)
        checks[key] = {"label": label, "pass": bool(ok), "status": a["status"], "error": js.get("error")}
        show(f"{key} {label}", a)
        return js

    js1 = one("#1", "valid /submit", "/submit", {"text": AI1, "creator_id": "cap-e"}, expect_status=200,
              extra=lambda j: all(k in j and j[k] is not None for k in SIX)
              and j.get("guess") in ("human", "unsure", "ai"))
    one("#2", "not JSON", "/submit", raw="not json", expect_status=400, expect_error="invalid_json")
    one("#3", "no text field", "/submit", {"creator_id": "cap-e"}, expect_status=422, expect_error="missing_field")
    one("#4", "empty text", "/submit", {"text": "", "creator_id": "cap-e"}, expect_status=400,
        expect_error="empty_text")
    one("#5", "punctuation only", "/submit", {"text": "!!!", "creator_id": "cap-e"}, expect_status=400,
        expect_error="no_words")
    one("#6", "492 words", "/submit", {"text": " ".join([AI1.strip()] * 3), "creator_id": "cap-e"},
        expect_status=413, expect_error="text_too_long")
    one("#7", "Hi.", "/submit", {"text": "Hi.", "creator_id": "cap-e"}, expect_status=400,
        expect_error="text_too_short")
    cid = js1.get("content_id")
    if cid and checks["#1"]["pass"]:
        one("#8", "appeal", "/appeal", {"content_id": cid, "reasoning": "I wrote this myself."},
            expect_status=200, extra=lambda j: j.get("status") == "under_review")
        one("#9", "appeal again", "/appeal", {"content_id": cid, "reasoning": "Appealing again."},
            expect_status=409, expect_error="already_appealed")
    else:
        for k, lab in (("#8", "appeal"), ("#9", "appeal again")):
            checks[k] = {"label": lab, "pass": False, "status": None, "error": "no content_id from #1"}
            say(f"  {k} {lab}: FAIL (no content_id from #1)")
    one("#10", "made-up id", "/appeal", {"content_id": MADE_UP_ID, "reasoning": "Not a real id."},
        expect_status=404, expect_error="unknown_content_id")
    h = health()
    checks["#11"] = {"label": "GET /health", "pass": bool(h and h.get("ok") is True), "status": 200 if h else None}
    say(f"  #11 GET /health: {json.dumps(h)}")
    t = subprocess.run([sys.executable, "test.py"], cwd=ROOT, capture_output=True, text=True)
    summary = next((l for l in t.stdout.splitlines() if " passed, " in l and " failed" in l), "")
    m = re.search(r"(\d+) failed", summary)
    checks["#12"] = {"label": "python test.py", "pass": bool(m and m.group(1) == "0"), "summary": summary}
    say(f"  #12 python test.py: {summary!r}")

    # The boundary, in this process, with Flask's test client (the server is untouched).
    sys.path.insert(0, str(ROOT))
    import app as appmod
    import audit
    import detector
    import scoring
    appmod.app.testing = False
    appmod.app.config["PROPAGATE_EXCEPTIONS"] = False
    client = appmod.app.test_client()
    for key, target, name, where in (("(a)", detector, "model_signal", "while GPT-2 scores the text"),
                                     ("(b)", scoring, "combine_signals", "while combining and labelling"),
                                     ("(c)", audit, "log_decision", "while writing the log")):
        before = len(log_lines())
        with mock.patch.object(target, name, side_effect=RuntimeError(f"capstone boundary check {key}")):
            r = client.post("/submit", json={"text": AI1, "creator_id": "cap-e"})
        after = len(log_lines())
        is_json = r.get_json(silent=True) is not None
        ok = r.status_code == 500 and not is_json and after == before
        checks[key] = {"label": f"error {where}", "pass": ok, "status": r.status_code,
                       "json": is_json, "new_lines": after - before}
        say(f"  {key} RuntimeError in {target.__name__}.{name} ({where}): status {r.status_code}, "
            f"JSON body: {is_json}, new log lines: {after - before} (lines {before} -> {after})")

    required = ["#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9", "#10", "(a)", "(b)", "(c)"]
    n_req = sum(1 for k in required if checks[k]["pass"])
    n_all = sum(1 for k in checks if checks[k]["pass"])
    passed = n_req == 13
    out["c5"] = {"pass": passed, "required_pass": n_req, "all_pass": n_all, "checks": checks}
    say(f"  -> Capstone 5 on this machine: {'PASS' if passed else 'FAIL'} "
        f"({n_req} of the 13 required; {n_all} of 15 overall; #11 {checks['#11']['pass']}, #12 {checks['#12']['pass']})")


# ── Capstone 3 (macOS, server starts #2 and #3) ───────────────────────────────

def capstone_3(out):
    say("\n== Capstone 3: every log entry is complete ==")
    before = len(log_lines())
    say(f"  log lines before: {before}")
    sent = []   # (label, attempt dict, expected input, kind)

    proc, up = start_server(label="start #2")
    if up:
        attempts, _ = with_retries("/submit", {"text": AI1, "creator_id": "cap-c-decision"}, COLD_WAIT, cold=True)
        for a in attempts:
            sent.append(("1 decision", a, expected_input(AI1), "decision"))
        cid = (attempts[-1]["json"] or {}).get("content_id")
        for i in range(13):     # 12 repeats, then the 13th (the 429)
            attempts, _ = with_retries("/submit", {"text": AI1, "creator_id": "cap-c-repeat"}, WARM_WAIT, cold=False)
            for a in attempts:
                sent.append((f"2 repeat {i + 1}", a, expected_input(AI1), "decision" if a["status"] == 200 else "refused"))
        attempts, _ = with_retries("/submit", {"creator_id": "cap-c-missing"}, WARM_WAIT, cold=False)
        for a in attempts:
            sent.append(("3 no text", a, None, "refused"))
        for lab, body, kind in (("4 appeal", {"content_id": cid, "reasoning": "I wrote this myself."}, "appeal"),
                                ("4 appeal again", {"content_id": cid, "reasoning": "Appealing again."}, "refused"),
                                ("4 made-up id", {"content_id": MADE_UP_ID, "reasoning": "Not a real id."}, "refused")):
            attempts, _ = with_retries("/appeal", body, WARM_WAIT, cold=False)
            for a in attempts:
                sent.append((lab, a, expected_input(body["reasoning"]), kind))
    stop_server(proc)

    proc, up = start_server({"AI201_DETECTOR_MODEL": BAD_MODEL}, label="start #3 (bad model name)")
    if up:
        attempts, _ = with_retries("/submit", {"text": AI1, "creator_id": "cap-c-503"}, COLD_WAIT, cold=False)
        for a in attempts:
            sent.append(("5 bad model", a, expected_input(AI1), "refused"))
    stop_server(proc)

    new = log_lines()[before:]
    say(f"  requests sent: {len(sent)}; new log lines: {len(new)} (expected 19 each)")
    complete = 0
    rows = []
    for i, (label, a, exp_in, kind) in enumerate(sent):
        e = new[i] if i < len(new) else None
        js = a["json"] or {}
        problems = []
        if e is None:
            problems.append("no entry")
        else:
            if not e.get("timestamp"):
                problems.append("timestamp")
            if e.get("input") != exp_in:
                problems.append("input")
            if kind == "decision":
                exp_out = {"guess": js.get("guess"), "label": js.get("label")}
            elif kind == "appeal":
                exp_out = {"status": js.get("status"), "http_status": a["status"]}
            else:
                exp_out = {"reason": js.get("error"), "http_status": a["status"]}
            if e.get("output") != exp_out:
                problems.append("output")
            d = e.get("duration_ms")
            if not isinstance(d, (int, float)) or d <= 0 or d > a["wait_ms"]:
                problems.append("duration_ms")
            if (i == 0) != ("cold" in e) or (i == 0 and e.get("cold") is not True):
                problems.append("cold")
        ok = not problems and a["problem"] is None
        complete += ok
        rows.append({"label": label, "status": a["status"], "wait_ms": a["wait_ms"],
                     "duration_ms": e.get("duration_ms") if e else None, "complete": ok, "problems": problems})
        show(label, a, e)
        say(f"    duration_ms {e.get('duration_ms') if e else None} vs caller's wait {a['wait_ms']}: "
            f"{'complete' if ok else 'INCOMPLETE: ' + ', '.join(problems or [a['problem']])}")
    if len(sent) != 19 or len(new) != 19:
        say("  note: not exactly 19 requests / 19 lines, so at least one entry is missing or extra")
    passed = complete == 19 and len(sent) == 19 and len(new) == 19
    out["c3"] = {"pass": passed, "complete": complete, "sent": len(sent), "new_lines": len(new), "rows": rows}
    say(f"  -> Capstone 3: {'PASS' if passed else 'FAIL'} ({complete} of 19 complete)")


# ── Capstone 2 (macOS, last: it uninstalls libraries) ─────────────────────────

def capstone_2(out):
    say("\n== Capstone 2: the model can't load (cap-b) ==")
    causes = [("torch", ["-m", "pip", "uninstall", "-y", "torch"], None, "ModuleNotFoundError", "'torch'"),
              ("transformers", ["-m", "pip", "uninstall", "-y", "transformers"], None, "ModuleNotFoundError",
               "'transformers'"),
              ("bad model name", None, {"AI201_DETECTOR_MODEL": BAD_MODEL}, "OSError", None)]
    results = []
    for name, uninstall, env, exp_type, module in causes:
        say(f"  cause: {name}")
        if uninstall:
            subprocess.run([sys.executable] + uninstall, cwd=ROOT, capture_output=True, text=True)
        before = len(log_lines())
        proc, up = start_server(env, label=f"cause {name}")
        a = post("/submit", body={"text": AI1, "creator_id": "cap-b"}, timeout=COLD_WAIT) if up else \
            {"status": None, "json": None, "wait_ms": None, "problem": "server not up"}
        stop_server(proc)
        new = log_lines()[before:]
        e = new[0] if len(new) == 1 else None
        js = a["json"] or {}
        filled = lambda v: v is not None and v != ""  # noqa: E731
        checks = {
            "503": a["status"] == 503,
            "JSON": a["json"] is not None,
            "error": js.get("error") == "detector_could_not_load",
            "message identical, not empty": bool(js.get("message")) and e is not None
                                             and js.get("message") == e.get("message"),
            "exactly one new line": len(new) == 1,
            "reason/http_status": e is not None and e.get("reason") == "detector_could_not_load"
                                   and e.get("http_status") == 503,
            "fields filled": e is not None and all(filled(e.get(k)) for k in ("message", "model", "error_type",
                                                                                 "failed_at")),
            "error_type exact": e is not None and e.get("error_type") == exp_type,
            "names the module": True if module is None else module in (js.get("message") or ""),
        }
        ok = all(checks.values())
        show(f"cause {name}", a, e)
        say(f"    checks: {json.dumps(checks)}  -> {'PASS' if ok else 'FAIL'}")
        if uninstall:
            subprocess.run([sys.executable, "-m", "pip", "install", "-q", "-r", "requirements.txt"],
                           cwd=ROOT, capture_output=True, text=True)
        results.append({"cause": name, "pass": ok, "checks": checks})
    n = sum(r["pass"] for r in results)
    out["c2"] = {"pass": n == 3, "causes_pass": n, "causes": results}
    say(f"  -> Capstone 2: {'PASS' if n == 3 else 'FAIL'} ({n} of 3 causes)")


# ── run (one machine) ─────────────────────────────────────────────────────────

def cmd_run(args):
    out = {"machine": platform.system(), "python": platform.python_version(),
           "commit": os.getenv("GITHUB_SHA", ""), "run_id": os.getenv("GITHUB_RUN_ID", ""),
           "started": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
           "produced_by": "run_capstone.py::cmd_run"}
    say(f"Capstone run on {out['machine']} (Python {out['python']}), commit {out['commit'][:7]}, "
        f"run {out['run_id']}")
    proc, up = start_server(label="start #1")
    if not up:
        out["c1"] = {"pass": False, "attempts": 0, "cold_span_ms": None, "evidence": [], "note": "server never up"}
        out["c4"] = {"pass": False, "note": "Capstone 1 never passed"}
        out["c5"] = {"pass": False, "note": "server never up"}
    else:
        capstone_1(out)
        capstone_4(out, proc)
        capstone_5(out)
    stop_server(proc)
    if platform.system() == "Darwin" and not args.skip_macos_only:
        capstone_3(out)
        if not args.skip_c2:
            capstone_2(out)
    line = json.dumps(out, ensure_ascii=False, separators=(",", ":"))
    # Also saved as a file outside the repo, which the workflow attaches to the run as a backup copy.
    import tempfile
    folder = Path(os.getenv("RUNNER_TEMP") or tempfile.gettempdir())
    (folder / f"capstone_result_{out['machine']}.json").write_text(line, encoding="utf-8")
    say("\nCAPSTONE-RESULT " + line)


# ── report (your machine) ─────────────────────────────────────────────────────

def cmd_report(args):
    runs = []
    for run_id in args.run_ids:
        text = subprocess.run(["gh", "run", "view", run_id, "--log"], capture_output=True, text=True).stdout
        machines = {}
        for line in text.splitlines():
            i = line.find("CAPSTONE-RESULT ")
            if i >= 0:
                try:
                    r = json.loads(line[i + len("CAPSTONE-RESULT "):])
                    machines[r["machine"]] = r
                except ValueError:
                    pass   # a line cut short on the page; the attached copy is read below
        if len(machines) < 3:
            import tempfile
            dest = Path(tempfile.mkdtemp())
            subprocess.run(["gh", "run", "download", run_id, "--dir", str(dest)], capture_output=True)
            for f in dest.glob("**/capstone_result_*.json"):
                r = json.loads(f.read_text(encoding="utf-8"))
                machines.setdefault(r["machine"], r)
        runs.append({"run_id": run_id, "machines": machines})

    def frac(run, key, per):
        ms = run["machines"]
        if key in ("c2", "c3"):
            r = ms.get("Darwin", {}).get(key)
            if not r:
                return "not run"
            return f"{r['causes_pass']}/3 causes" if key == "c2" else f"{r['complete']}/19 entries"
        n = sum(1 for m in ("Linux", "Windows", "Darwin") if ms.get(m, {}).get(key, {}).get("pass"))
        return f"{n}/3 machines"

    names = {"c1": ("Capstone 1. First start on three systems", "3/3 machines, all three trials"),
             "c2": ("Capstone 2. The model can't load: three causes", "3/3 causes, all three trials"),
             "c3": ("Capstone 3. Every log entry is complete", "19/19 entries, all three trials"),
             "c4": ("Capstone 4. Cost and speed on three systems", "3/3 machines (cold ≤ 45000 ms, 2 of 3 warm ≤ 5000 ms, memory ≤ 900 MB), all three trials"),
             "c5": ("Capstone 5. The old behaviour and the boundary hold", "3/3 machines (13 of 15 named checks), all three trials")}
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    path = ROOT / "results" / f"capstone_run_{stamp}_{args.label}.md"
    commits = {m.get("commit", "")[:7] for r in runs for m in r["machines"].values()}
    lines = [f"# Capstone run: {args.label}", "",
             f"- Produced by: `run_capstone.py::cmd_run` on each GitHub machine (workflow `.github/workflows/capstone.yml`); this file by `run_capstone.py::cmd_report` from the runs' pages (`gh run view --log`)",
             f"- Date: {dt.date.today().isoformat()}",
             f"- Git commit tested: {', '.join(sorted(c for c in commits if c)) or 'unknown'}",
             f"- Workflow runs (trials): {', '.join(r['run_id'] for r in runs)}",
             "- Start command: `python app.py` (started by the runner, port 5050)", "",
             "| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |", "|---|---|---|---|---|---|"]
    for key, (name, target) in names.items():
        cells = [frac(r, key, None) for r in runs] + [""] * (3 - len(runs))
        lines.append(f"| {name} | {target} | {' | '.join(cells)} | |")
    lines += ["", "The Verdict column is blank on purpose: the student writes MET or MISSED.", "",
              "## Real output", "",
              "Below, per run and per machine, the runner's own summary lines and the machine-readable result, "
              "copied from each run's page. The full request-by-request output (every response, caller's wait "
              "and log line) is on the run's page under the step \"Capstone run\".", ""]
    for r in runs:
        lines.append(f"### Run {r['run_id']}")
        for m, res in sorted(r["machines"].items()):
            lines.append(f"#### {m} (Python {res.get('python')})")
            lines.append("```json")
            lines.append(json.dumps({k: v for k, v in res.items() if k != "produced_by"}, indent=1,
                                    ensure_ascii=False)[:60000])
            lines.append("```")
        lines.append("")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(path)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run", help="run the criteria on this machine")
    r.add_argument("--skip-macos-only", action="store_true", help="skip Capstone 3 and 2 on macOS (local tests)")
    r.add_argument("--skip-c2", action="store_true", help="skip Capstone 2 (it uninstalls torch/transformers)")
    rep = sub.add_parser("report", help="build the results file from three workflow runs")
    rep.add_argument("--label", default="before")
    rep.add_argument("run_ids", nargs="+")
    args = p.parse_args()
    {"run": cmd_run, "report": cmd_report}[args.cmd](args)


if __name__ == "__main__":
    main()
