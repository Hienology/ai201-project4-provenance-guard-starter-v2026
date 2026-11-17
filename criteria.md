# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1.

**Score spread.** Inputs: 5 AI texts and 5 texts I wrote myself, saved in `samples/`. Action: submit each one to `POST /submit`. Read: `model_score` from each response. Pass if: the average `model_score` of the 5 AI texts minus the average `model_score` of my 5 texts is at least 0.3, in all three trials.

**Why this target:** I want to catch the most obvious case.



---

## 2.

**False positives.** Inputs: my 5 own texts in `samples/` (the same ones as criterion 1). Action: submit each one to `POST /submit`. Read: `guess` from each response; a text counts as flagged when `guess` is `ai` or `unsure`. Pass if: at most 2 of the 5 are flagged, in all three trials.

**Why this target:** I'm not very confident, given how good prompt engineering can get. AI can be made to look human, so the service can't be sure and should say "unsure" often. Since I count "unsure" as flagged, some of my honest texts will be flagged, so I accept up to 2 of 5.



---

## 3.

**Bad input.** Inputs: five bad requests, saved as ready-to-run curl commands in `samples/`: not JSON, missing `text` or `creator_id`, empty text, too short, and over 350 words. Action: send each one to `POST /submit`. Read: the status code and the `error` field of each response; the expected pairs are 400 `invalid_json`, 422 `missing_field`, 400 `empty_text`, 400 `text_too_short` and 413 `text_too_long`. Pass if: at least 4 of the 5 return their expected code and `error`, in all three trials.

**Why this target:** It shows it can detect the proper case, especially with those sharing code 400, and because signal one doesn't have enough material to make calculations and comparisons on very short text.



---

## 4.

**The appeal path.** Inputs: one of my texts in `samples/`, submitted fresh in each trial, plus one made-up `content_id`. Action: submit the text to `POST /submit` and keep the returned `content_id`; appeal it with `POST /appeal`; appeal the same id a second time; then appeal the made-up id. Read: five checks. (1) The first appeal returns 200. (2) Its response has `status: "under_review"`. (3) `GET /log` shows an appeal entry with the same `content_id`, on a later line than the original decision. (4) The second appeal returns 409 `already_appealed`. (5) The made-up id returns 404 `unknown_content_id`. Pass if: all 5 of the 5 checks pass, in all three trials.

**Why this target:** The right to appeal must be guaranteed properly. Any first appeal in a valid format should go forward, not mentioning the fate.



---

## 5.

**Label coverage.** Inputs: the same 10 texts as criteria 1 and 2 (5 AI texts and my 5 own texts in `samples/`). Action: submit each one to `POST /submit`. Read: `guess` from each response. Pass if: at least 3 of the 5 AI texts get `ai`, at least 1 of the 10 texts gets `unsure`, and at least 2 of the 10 get `human`, in all three trials.

**Why this target:** I want more AI-generated test cases to be detected; given GPT-2's limits, I can expect detecting AI text can be easier.



---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->

---

## Capstone criteria (Unit 9)

Written before any capstone run. The reader I wrote these for is an IT student with no context on this project. Every run goes through the GitHub Actions workflow `.github/workflows/capstone.yml` on GitHub's Ubuntu, Windows and macOS machines, and every result is read from `results/capstone_run_<stamp>_<label>.md`, built from the run's page, where the workflow prints the responses and the new lines of `logs/audit.jsonl`. One trial = one workflow run. A re-run is a new trial, and every trial must hold.

### Capstone 1.

*(Assembled by the coding agent from my answers.)*

**First start on three systems.** Inputs: a fresh clone on each of GitHub's Ubuntu, Windows and macOS machines, none with GPT-2 cached; `samples/ai-1.txt`. Action: on each machine, the workflow runs `RUNNING.md`'s setup steps, including `python detector.py`, which downloads GPT-2 (about 550 MB); starts `python app.py` in the background; and waits until `GET /health` answers. Then it sends one `POST /submit` with the text of `samples/ai-1.txt` as `text` and `cap-a` as `creator_id`. This first request loads GPT-2 from disk. Each attempt waits up to 60 s for an answer. Only after a timeout, the workflow pauses 5 s, waits until `/health` shows `detector_loaded: true` (up to 60 s), and tries again: at most 4 attempts (1 + 3 retries), stopping at the first that passes. A refused connection (nothing listening) is a FAIL, with no retry. Read: the response and the new lines of `logs/audit.jsonl`, in the results file. Pass if: on 3 of 3 machines, one of the up to 4 attempts gets status 200; all six fields (`content_id`, `guess`, `confidence`, `label`, `model_score`, `style_score`) present and not `null`; `guess` = `ai`; and a log entry with the same `content_id` and `status` `decided`; in all three trials. A machine that never ran is a FAIL, unless GitHub failed it before the workflow's first step (the job was cancelled, or no machine was assigned): then that run does not count and a new run is started.

**Why this target:** "modern tech, I don't know, I just think everything now is too reliable."

### Capstone 2.

*(Assembled by the coding agent from my answers.)*

**The model can't load: three causes.** Inputs: `samples/ai-1.txt`, on GitHub's macOS machine, in the same workflow run, after Capstone 3 (last of all). Action: three causes, one at a time: (1) `pip uninstall -y torch`; (2) `pip uninstall -y transformers`; (3) `AI201_DETECTOR_MODEL=no-such-model-capstone`, passed to that one server start only. For each cause: count the lines in `logs/audit.jsonl`; start `python app.py` in the same virtual environment; send one `POST /submit` of `ai-1` as `cap-b`; stop the server; then undo the cause (`pip install -r requirements.txt`, or clear the variable) before the next one. Read: each response and the new log line, in the results file. Pass if: for 3 of 3 causes, the response has status 503, is JSON, has `error` `detector_could_not_load` and a `message` that is not empty and identical to the entry's `message` (equal strings after reading the JSON, line breaks included); there is exactly one new line, with `reason` `detector_could_not_load`, `http_status` 503, and `message`, `model`, `error_type` and `failed_at` filled (present, not `null` and not empty); `error_type` is exactly `ModuleNotFoundError` for a missing library and exactly `OSError` for the bad name; and, for a missing library, the message names the removed module (`torch` or `transformers`); in all three trials. One trial = all three causes once each.

**Why this target:** *(Reworded by the coding agent from my answers, at my request.)* No torch issue, no transformers issue, no bad name issue: when any of the three happens, the writer's text isn't processed and it costs them time. They can submit again, but they have to wait until the server is fixed and up again, and they don't know when or how that will happen.

### Capstone 3.

*(Assembled by the coding agent from my answers.)*

**Every log entry is complete.** Inputs: GitHub's macOS machine, after Capstones 1, 4 and 5; `samples/ai-1.txt`; the appeal texts and made-up id from `samples/appeal_check.sh`. Action: count the lines in `logs/audit.jsonl`. Start `python app.py` afresh. Then, waiting for each answer (up to 60 s for the first request and 30 s for the others; retry only after a timeout):
1. one `POST /submit` of `ai-1` as `cap-c-decision` (this one loads GPT-2);
2. 12 more as `cap-c-repeat`, then a 13th as the same (→ 429), all 13 within 60 s of the first;
3. one `POST /submit` with no `text` field;
4. `POST /appeal` on step 1's `content_id` with "I wrote this myself."; again with "Appealing again."; then on `00000000-0000-0000-0000-000000000000` with "Not a real id.";
5. stop; start with `AI201_DETECTOR_MODEL=no-such-model-capstone`; one `POST /submit` of `ai-1`; stop; clear the variable.

Record the caller's wait for each of the 19 requests, in ms with 3 decimals. Read: in the results file, the 19 lines added after the count and before the end of step 5, each shown with its response and with the caller's wait next to its `duration_ms`. Pass if: all 19 of those entries are complete, in all three trials. An entry is complete when all of these hold:
- `timestamp` is present.
- `input` = `{sha256, words}` of the trimmed text (for appeals, of `reasoning`), or `null` when the request had no text. Trimmed = Python's `str.strip()`. Words = `len(stylometry.words(...))`. Check with:
  `python -c "import hashlib; t=open('samples/ai-1.txt',encoding='utf-8').read().strip(); print(hashlib.sha256(t.encode('utf-8')).hexdigest())"`
  `python -c "import stylometry; t=open('samples/ai-1.txt',encoding='utf-8').read().strip(); print(len(stylometry.words(t)))"`
- `output` matches the response, each value equal to the same thing in the response: `guess` and `label` for a decision; `status` `under_review` and `http_status` 200 for the accepted appeal; otherwise `reason` = the response's `error` and `http_status` = its status code.
- `duration_ms` is a number greater than 0 and at most the caller's wait (both in ms with 3 decimals; equal passes).
- A `cold` field is on step 1's entry, and there is no `cold` field on the other 18.

**Why this target:** *(Reworded by the coding agent from my answers, at my request.)* This criterion is about the log being right, not about the service being fast, so all 19 entries have to be right. `input` must be deterministic: the same trimmed text must give the same hash every time, so each text has one unique key in the log. If it is faulty, the text can't be found correctly later, or the wrong text gets credited. `duration_ms` only has to be true: a request slowed down by an unstable but working Internet connection deserves a chance, so a long time is fine as long as it's real.

### Capstone 4.

*(Assembled by the coding agent from my answers.)*

**Cost and speed on three systems.** Inputs: the same clones and server start as Capstone 1, on GitHub's Ubuntu, Windows and macOS machines; `samples/ai-1.txt`. Action: on each machine, Capstone 1's request is the cold request. After its answer, send 3 more `POST /submit` of `ai-1` as `cap-d`, one at a time, each waiting up to 30 s (retry only after a timeout). Right after the third answer, read the memory of the `python app.py` process: `psutil`'s `memory_info().rss` (resident memory; on Windows, the working set). Read: in the results file, with the clocks labelled: cold = the caller's clock, from the start of Capstone 1's attempt 1 to the end of its passing attempt; warm = each warm entry's `duration_ms`; memory in MB (1 MB = 1,000,000 bytes). Pass if: on 3 of 3 machines, cold is at most 45000 ms; at least 2 of the 3 warm readings are at most 5000 ms (a reading counts only if its request got 200); and memory is at most 900 MB; in all three trials. If Capstone 1 never passes on a machine, Capstone 4 fails on that machine.

**Why these targets:** *(Reworded by the coding agent from my answers, at my request.)* Each target is backed by arithmetic. Cold: I calibrate to a 100 Mbps connection, the FCC's minimum for broadband. GPT-2's 550 MB download is 4,400 megabits, which takes 44 s at 100 Mbps; add 1 s for loading and scoring, so 45000 ms. Warm: the service allows one writer 12 requests a minute, and 60 s ÷ 12 = 5 s; at 5000 ms a request, the service keeps up with a writer sending as fast as it allows. Memory: 550 MB for GPT-2's weights plus 350 MB for everything else, so 900 MB.

### Capstone 5.

*(Assembled by the coding agent from my answers.)*

**The old behaviour and the boundary hold.** Inputs: the same clones and server start as Capstone 1, on GitHub's Ubuntu, Windows and macOS machines, after Capstone 4's memory reading; `samples/ai-1.txt`; the appeal texts and made-up id from `samples/appeal_check.sh`. Action: on each machine, 15 checks, as `cap-e`, each request waiting up to 30 s (retry only after a timeout). The old behaviour:
- #1 `POST /submit` of `ai-1` → 200, all six fields, `guess` one of `human`, `unsure`, `ai` (any of the three passes: this checks the old behaviour, not accuracy);
- #2 the body `not json` with `Content-Type: application/json` → 400 `invalid_json`;
- #3 no `text` field → 422 `missing_field`;
- #4 `"text": ""` → 400 `empty_text`;
- #5 `"text": "!!!"` → 400 `no_words`;
- #6 three copies of `ai-1` joined by a single space (492 words) → 413 `text_too_long`;
- #7 `"text": "Hi."` → 400 `text_too_short`;
- #8 `POST /appeal` on #1's `content_id` with "I wrote this myself." → 200, `status` `under_review`;
- #9 the same appeal again, with "Appealing again." → 409 `already_appealed`;
- #10 `POST /appeal` on `00000000-0000-0000-0000-000000000000` with "Not a real id." → 404 `unknown_content_id`;
- #11 `GET /health` → `ok: true`;
- #12 `python test.py` → its summary line says 0 failed.

The boundary, in test code in `run_capstone.py` using Flask's test client: a `RuntimeError` is made to happen (a) in `detector.model_signal`, while GPT-2 scores the text, (b) in `scoring.combine_signals`, while combining and labelling, and (c) in `audit.log_decision`, while writing the log; each time one `POST /submit` of `ai-1` is sent. Read: in the results file, each response, `test.py`'s summary line, and the line count of `logs/audit.jsonl` just before and just after each of (a) to (c). Pass if: on 3 of 3 machines, #1 to #10 and (a) to (c) all pass, 13 of 15; #11 and #12 are recorded but may fail; in all three trials. If #1 fails, #8 to #10 are FAIL. (a) to (c) pass when the answer has status 500 and a body that isn't JSON (so not `detector_could_not_load`), and no new log line.

**Why this target:** *(Reworded by the coding agent from my answers, at my request. The `test.py` part and the indirect effect of a wrong 503 restate facts the agent showed me, which I took as my reason.)* What decides is whether a failure impacts the users' operations, directly or indirectly. The main path, the six refusals and the three appeal outcomes touch writers directly. The three boundary checks touch them indirectly: a wrong 503 points whoever runs the server at the wrong cause, so the real fault lasts longer and writers wait longer. None of those 13 may fail. `/health` is spared because it doesn't touch the users: writers' requests still work if it breaks. `test.py` is spared because it checks the machine's setup, not the service's behaviour, and its own header says nothing in it is graded.
