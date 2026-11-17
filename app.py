#!/usr/bin/env python3
"""
Provenance Guard — the web service.

    python app.py

Then, in another terminal:

    curl -X POST http://127.0.0.1:5000/ping \
      -H "Content-Type: application/json" \
      -d '{"message": "hello"}'

That's the example route. It works right now, before you've written anything.
**Leave it alone** — it's your control. When something breaks later, check that
`/ping` still answers: if it does, the problem is in your handler; if it
doesn't, it's the service itself.

Routes:

    POST /ping        the worked example. Already works. Don't edit it
    POST /submit      ← YOU BUILD THIS (Milestone 3, 4, 5)
    POST /appeal      ← YOU BUILD THIS (Milestone 5)
    GET  /log         the audit log. Already works
    GET  /health      is the service up, and is the model loaded
"""

import hashlib
import time
import uuid

from flask import Flask, g, jsonify, request

import audit
import config
import detector
import scoring
import stylometry

app = Flask(__name__)


# ── Capstone instrumentation (student's decisions, M3) ────────────────────────
# Every entry gets `input`, `output` and `duration_ms`; the request that loaded
# GPT-2 also gets `cold: true` (no `cold` field anywhere else).

def _stamp_arrival(wsgi_app):
    """Note when a request arrives, before the rate limiter sees it (429 timing)."""
    def wrapped(environ, start_response):
        environ["capstone.arrived"] = time.perf_counter()
        return wsgi_app(environ, start_response)
    return wrapped


app.wsgi_app = _stamp_arrival(app.wsgi_app)


def _input_of(text):
    """SHA-256 of the trimmed text plus its word count; None when there's no text."""
    if not isinstance(text, str) or not text.strip():
        return None
    trimmed = text.strip()
    return {
        "sha256": hashlib.sha256(trimmed.encode("utf-8")).hexdigest(),
        "words": len(stylometry.words(trimmed)),
    }


def _ms_since(t0):
    """Milliseconds since t0 (a time.perf_counter() reading), 3 decimals."""
    return round((time.perf_counter() - t0) * 1000, 3)


# ── Rate limiting — UNIT 8 ────────────────────────────────────────────────────
# Off until you turn it on. In unit 8, Milestone 1:
#
#   1. Set RATE_LIMITING_ENABLED = True in config.py (or AI201_RATE_LIMITS=1)
#   2. Choose your numbers there
#   3. Uncomment the @limiter.limit(...) line on /submit below
#
# The order doesn't matter. While limiting is off, that decorator is a no-op
# that quietly does nothing, so uncommenting it early costs you nothing — but
# it also means no 429 until you've done step 1.
#
# The storage backend is preconfigured, which stops Flask-Limiter printing a
# warning on every start. In-memory is right for one laptop and wrong for
# anything real — a restart forgets every count.

class _LimiterOff:
    """
    Stands in for the real limiter while rate limiting is off.

    It makes @limiter.limit(...) a decorator that returns the route
    untouched, so uncommenting the line before you flip the setting is
    harmless instead of a crash on startup.
    """

    def limit(self, *args, **kwargs):
        return lambda view: view


limiter = _LimiterOff()
if config.RATE_LIMITING_ENABLED:
    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address

    def rate_limit_key():
        """
        Who a request counts against.

        Falling back to the caller's address is the easy version. Unit 8's
        stretch asks about per-creator limits instead — and the difference
        matters: one script can look like a thousand callers, and one household
        can look like one.
        """
        payload = request.get_json(silent=True)
        # A body that parses as JSON but isn't an object — a bare list or
        # string — has no .get. Without this guard the key function raises
        # BEFORE the route runs, and a malformed request becomes a 500 that
        # looks like your handler crashed when your handler never ran.
        if not isinstance(payload, dict):
            return get_remote_address()
        creator = payload.get("creator_id")
        return creator if isinstance(creator, str) and creator.strip() else get_remote_address()

    limiter = Limiter(
        key_func=rate_limit_key,
        app=app,
        storage_uri=config.RATE_LIMIT_STORAGE,
        default_limits=[],
    )

    @app.errorhandler(429)
    def rate_limited(exc):
        """
        A rejected request still leaves a trace.

        ⚠️ An attack that shows up only as an absence is one you'll never find.
        """
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            payload = {}
        # Capstone: timed from arrival (before the limiter) to here.
        arrived = request.environ.get("capstone.arrived")
        audit.log_rejection(
            creator_id=payload.get("creator_id", "unknown"),
            reason="rate_limited",
            limit=str(exc.description),
            input=_input_of(payload.get("text")),
            output={"reason": "rate_limited", "http_status": 429},
            duration_ms=_ms_since(arrived) if arrived is not None else None,
        )
        return jsonify({
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly.",
            "limit": str(exc.description),
        }), 429


# ── The worked example. Already works. Don't edit. ────────────────────────────

@app.post("/ping")
def ping():
    """
    Everything a route needs, in six lines.

    JSON arrives as a dict. You pull things out of it. You return a dict and
    the framework turns it into a response. That's the whole idea.
    """
    payload = request.get_json(silent=True) or {}
    return jsonify({
        "ok": True,
        "you_sent": payload.get("message"),
        "service": "provenance-guard",
    })


@app.get("/health")
def health():
    """Is the service up, and has the model been downloaded yet?"""
    import detector

    loaded = detector._model is not None
    return jsonify({
        "ok": True,
        "detector_model": config.DETECTOR_MODEL,
        "detector_loaded": loaded,
        "rate_limiting": config.RATE_LIMITING_ENABLED,
        "log_entries": len(audit.read_entries()),
    })


# ── YOU BUILD THIS ────────────────────────────────────────────────────────────

def _refuse(status, error, message, creator_id=None, log_extra=None, text=None, cold=False):
    """
    A request /submit won't score: logged as a rejection (no content_id), then
    answered. A refused request that leaves no trace is an attack you can't see.

    `log_extra` (capstone): a dict of more fields for the log entry only, not
    the response. A dict, so a field can be called `message` too.
    `text`, `cold` (capstone): what came in, and whether this request loaded GPT-2.
    """
    fields = {
        "input": _input_of(text),
        "output": {"reason": error, "http_status": status},
        "duration_ms": _ms_since(g.t0) if "t0" in g else None,
    }
    if cold:
        fields["cold"] = True
    audit.log_rejection(
        creator_id=creator_id if isinstance(creator_id, str) and creator_id else "unknown",
        reason=error,
        http_status=status,
        **(log_extra or {}),
        **fields,
    )
    return jsonify({"error": error, "message": message}), status


@app.post("/submit")
@limiter.limit(f"{config.RATE_LIMIT_PER_MINUTE}/minute;{config.RATE_LIMIT_PER_DAY}/day")
def submit():
    """
    Take a piece of text, decide about it, log the decision, answer.
    ← TODO — Milestones 3, 4 and 5

    Expects JSON:
        {"text": "...", "creator_id": "..."}

    Should return JSON with, at minimum:
        {"content_id": "...", "guess": "...", "confidence": 0.0, "label": "...",
         "model_score": 0.0, "style_score": 0.0}

    ⚠️ **Both signal scores go in the response, not just the log.** Unit 8's
    `run_attacks.py` and `run_eval.py` read `model_score` and `style_score`
    straight off this response and put them in your reports. Leave them out and
    every row of next unit's evidence says `null` — which is exactly the
    diagnostic you need to name a stage and a mechanism. You do not want to
    find that out after running the attack set.

    ─────────────────────────────────────────────────────────────────────────
    Build it in three passes. Do not skip ahead — the ordering is how you tell
    a broken route from a broken signal.

    **Milestone 3 — the route answers.**
      1. Return a hardcoded response. Confirm `curl` gets it back before you
         add any logic at all.
      2. Then pull `text` and `creator_id` out of the payload.
      3. Then call ONE signal — `detector.model_signal(text)` — and put the
         real number in. Leave confidence and label as placeholders.
      4. Log every submission with `audit.log_decision(...)`. The content_id
         matters: `/appeal` needs it, and a student who skips it rebuilds this
         whole flow later.

    **Milestone 4 — the second signal and the score.**
      5. Add `stylometry.style_signal(text)`.
      6. Combine them with `scoring.combine_signals(...)`.
      7. Log BOTH signal scores alongside the combined one, and put them in the
         response too. Next unit you can't diagnose anything without them.

    **Milestone 5 — the label.**
      8. `scoring.score_to_label(...)` and put the real label in the response.

    ─────────────────────────────────────────────────────────────────────────
    Worth deciding early, because unit 8's attack set will decide it for you:
    what should this do when `text` is missing, empty, or enormous? A crash on
    a malformed input is one of the most common real failures there is.
    """
    # Capstone: `duration_ms` for /submit is the whole request inside this function.
    g.t0 = time.perf_counter()

    # Bad input never reaches a signal, and never gets a content_id. Each refusal
    # is logged as a rejection (unit 8).
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return _refuse(400, "invalid_json", "The request body must be JSON.")

    text = payload.get("text")
    creator_id = payload.get("creator_id")
    if not isinstance(text, str) or not isinstance(creator_id, str):
        return _refuse(422, "missing_field", "Both text and creator_id are required.",
                       creator_id, text=text)
    # Leading/trailing whitespace moves signal one's score, so it never gets scored.
    text = text.strip()
    if not text:
        return _refuse(400, "empty_text", "The text is empty.", creator_id, text=text)
    # Punctuation-only text passes signal one but gives signal two nothing to count.
    n_words = len(stylometry.words(text))
    if n_words == 0:
        return _refuse(400, "no_words", "The text has no words to score.", creator_id,
                       text=text)
    if n_words > config.MAX_WORDS:
        return _refuse(413, "text_too_long",
                       f"The text is too long to score. Please send at most {config.MAX_WORDS} words.",
                       creator_id, text=text)

    # Signal one. Under 3 tokens it raises ValueError: too little to score.
    # Capstone (student's contract): if GPT-2 can't be loaded, the writer gets a
    # 503 with the full error text instead of a bare 500, and the failure is
    # logged as a rejection instead of leaving no trace.
    # Capstone: `cold` marks the request that loaded GPT-2 (it wasn't loaded
    # before this call and is after it).
    was_loaded = detector._model is not None
    try:
        model_score = detector.model_signal(text)
    except ValueError:
        return _refuse(400, "text_too_short",
                       "The text is too short to score. Please send at least a few sentences.",
                       creator_id, text=text,
                       cold=not was_loaded and detector._model is not None)
    except detector.DetectorUnavailable as exc:
        # The entry records the full message, which model, which stage, and
        # the underlying error's type (student: "Both").
        return _refuse(503, "detector_could_not_load", str(exc), creator_id,
                       log_extra={
                           "message": str(exc),
                           "model": config.DETECTOR_MODEL,
                           "error_type": type(exc.__cause__ or exc).__name__,
                           "failed_at": "model_load",
                       },
                       text=text)
    cold = not was_loaded and detector._model is not None

    # Signal two. It can't raise here: no-word text was rejected above.
    style_score = stylometry.style_signal(text)
    combined_score = scoring.combine_signals(model_score, style_score)

    # Only real decisions get an id: after the combined score, before the label.
    content_id = str(uuid.uuid4())
    guess, label = scoring.score_to_label(
        combined_score, model_score, style_score,
        one_sentence=len(stylometry.sentences(text)) < 2,
    )

    fields = {
        "input": _input_of(text),
        "output": {"guess": guess, "label": label},
        "duration_ms": _ms_since(g.t0),
    }
    if cold:
        fields["cold"] = True
    audit.log_decision(
        content_id=content_id,
        creator_id=creator_id,
        guess=guess,
        model_score=model_score,
        style_score=style_score,
        combined_score=combined_score,
        label=label,
        **fields,
    )

    # confidence = combined_score (AI-likelihood, M1 contract).
    return jsonify({
        "content_id": content_id,
        "guess": guess,
        "confidence": combined_score,
        "label": label,
        "model_score": model_score,
        "style_score": style_score,
    })


@app.post("/appeal")
def appeal():
    """
    A writer says you got it wrong. ← TODO — Milestone 5

    Expects JSON:
        {"content_id": "...", "reasoning": "..."}

    Should:
      1. Check the content_id actually exists — `audit.entries_for(id)` tells
         you. A typo here fails silently and looks like a broken endpoint,
         which is the single most common way this milestone eats an hour.
      2. Record the appeal with `audit.log_appeal(...)`, which moves the item
         to `under_review`.
      3. Confirm to the writer. No automatic re-checking needed.

    This is the smallest endpoint in the project and the one that matters most
    to the person on the other end. It's the only thing standing between a
    wrong accusation and nothing at all.
    """
    # Capstone: `duration_ms` for /appeal is the whole request inside this function.
    t0 = time.perf_counter()

    def refused(status, error, message, creator_id="unknown", reasoning=None):
        # Capstone: a refused appeal now leaves a rejection-format entry too.
        audit.log_rejection(
            creator_id=creator_id,
            reason=error,
            http_status=status,
            input=_input_of(reasoning),
            output={"reason": error, "http_status": status},
            duration_ms=_ms_since(t0),
        )
        return jsonify({"error": error, "message": message}), status

    # Not JSON / missing content_id follow the /submit rules (M1 contract).
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return refused(400, "invalid_json", "The request body must be JSON.")

    content_id = payload.get("content_id")
    # Missing or empty reasoning is allowed (M1 contract).
    reasoning = payload.get("reasoning")
    if reasoning is None:
        reasoning = ""
    if not isinstance(content_id, str) or not isinstance(reasoning, str):
        return refused(422, "missing_field",
                       "A content_id is required, and reasoning, if sent, must be text.",
                       reasoning=reasoning)

    # Decision entries carry no "event"; appeals and rejections do.
    entries = audit.entries_for(content_id)
    decisions = [e for e in entries if "event" not in e]
    if not decisions:
        return refused(404, "unknown_content_id",
                       "No decision was found for that content_id.",
                       reasoning=reasoning)
    if any(e.get("event") == "appeal" for e in entries):
        return refused(409, "already_appealed",
                       "This decision has already been appealed.",
                       creator_id=decisions[0]["creator_id"], reasoning=reasoning)

    # /appeal isn't sent a creator_id, so it comes from the original decision.
    # The decision line stays as it was; the appeal is appended after it.
    audit.log_appeal(
        content_id=content_id,
        creator_id=decisions[0]["creator_id"],
        reasoning=reasoning,
        input=_input_of(reasoning),
        output={"status": "under_review", "http_status": 200},
        duration_ms=_ms_since(t0),
    )
    return jsonify({
        "content_id": content_id,
        "status": "under_review",
        "message": "Your appeal has been recorded next to the original decision.",
    })


# ── Already works ─────────────────────────────────────────────────────────────

@app.get("/log")
def get_log():
    """
    The audit log, most recent last.

        curl "http://127.0.0.1:5000/log?limit=10"

    You need this in unit 8 to paste entries into your README, and you need it
    now to see whether your logging is actually working.
    """
    limit = request.args.get("limit", type=int)
    entries = audit.read_entries(limit=limit)
    return jsonify({"count": len(entries), "entries": entries})


def main():
    print(f"Provenance Guard on http://{config.HOST}:{config.PORT}")
    print(f"  detector model:  {config.DETECTOR_MODEL}")
    print(f"  rate limiting:   {'ON' if config.RATE_LIMITING_ENABLED else 'off (unit 8)'}")
    print(f"  audit log:       {config.AUDIT_LOG}")
    print()
    print("Check it's alive:")
    print(f'  curl -X POST http://{config.HOST}:{config.PORT}/ping \\')
    print('    -H "Content-Type: application/json" \\')
    print("    -d '{\"message\": \"hello\"}'")
    print()
    # debug=True hands out an interactive debugger, so it's local-only — see config.py
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)


if __name__ == "__main__":
    main()
