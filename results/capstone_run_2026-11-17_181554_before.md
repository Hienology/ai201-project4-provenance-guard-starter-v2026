# Capstone run: before

- Produced by: `run_capstone.py::cmd_run` on each GitHub machine (workflow `.github/workflows/capstone.yml`); this file by `run_capstone.py::cmd_report` from the runs' pages (`gh run view --log`)
- Date: 2026-11-17
- Git commit tested: 519dfda
- Workflow runs (trials): 44194503556, 44196618194, 44196649907
- Start command: `python app.py` (started by the runner, port 5050)

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| Capstone 1. First start on three systems | 3/3 machines, all three trials | 3/3 machines | 3/3 machines | 3/3 machines | |
| Capstone 2. The model can't load: three causes | 3/3 causes, all three trials | 3/3 causes | 3/3 causes | 3/3 causes | |
| Capstone 3. Every log entry is complete | 19/19 entries, all three trials | 19/19 entries | 19/19 entries | 19/19 entries | |
| Capstone 4. Cost and speed on three systems | 3/3 machines (cold ≤ 45000 ms, 2 of 3 warm ≤ 5000 ms, memory ≤ 900 MB), all three trials | 0/3 machines | 0/3 machines | 0/3 machines | |
| Capstone 5. The old behaviour and the boundary hold | 3/3 machines (13 of 15 named checks), all three trials | 3/3 machines | 3/3 machines | 3/3 machines | |

The Verdict column is blank on purpose: the student writes MET or MISSED.

## Real output

### Run 44194503556, copied from the run's page (step "Capstone run")

Every request, its response, the caller's wait and the new lines of `logs/audit.jsonl`, as printed by `run_capstone.py::cmd_run` (Capstone 1 `capstone_1`, 4 `capstone_4`, 5 `capstone_5`, 3 `capstone_3`, 2 `capstone_2`). The tracebacks under Capstone 5 are the three errors it makes happen on purpose.

#### capstone (macos-latest)
```text
﻿2026-11-17T22:55:38.1355690Z ##[group]Run if [ -f .venv/Scripts/activate ]; then source .venv/Scripts/activate; else source .venv/bin/activate; fi
2026-11-17T22:55:38.1360890Z ^[[36;1mif [ -f .venv/Scripts/activate ]; then source .venv/Scripts/activate; else source .venv/bin/activate; fi^[[0m
2026-11-17T22:55:38.1366270Z ^[[36;1mpython run_capstone.py run^[[0m
2026-11-17T22:55:38.2262790Z shell: /bin/bash --noprofile --norc -e -o pipefail {0}
2026-11-17T22:55:38.2263270Z env:
2026-11-17T22:55:38.2263560Z   PYTHONUTF8: 1
2026-11-17T22:55:38.2263930Z   pythonLocation: /Users/runner/hostedtoolcache/Python/3.12.10/arm64
2026-11-17T22:55:38.2264430Z   PKG_CONFIG_PATH: /Users/runner/hostedtoolcache/Python/3.12.10/arm64/lib/pkgconfig
2026-11-17T22:55:38.2270680Z   Python_ROOT_DIR: /Users/runner/hostedtoolcache/Python/3.12.10/arm64
2026-11-17T22:55:38.2271170Z   Python2_ROOT_DIR: /Users/runner/hostedtoolcache/Python/3.12.10/arm64
2026-11-17T22:55:38.2271780Z   Python3_ROOT_DIR: /Users/runner/hostedtoolcache/Python/3.12.10/arm64
2026-11-17T22:55:38.2272330Z ##[endgroup]
2026-11-17T22:55:38.5875520Z Capstone run on Darwin (Python 3.12.10), commit 519dfda, run 44194503556
2026-11-17T22:56:14.5889110Z [start #1] server up on port 5050 (pid 1589); /health answers
2026-11-17T22:56:14.5893560Z 
2026-11-17T22:56:14.5894540Z == Capstone 1: first start (cap-a) ==
2026-11-17T22:56:24.3876210Z   attempt 1: status 200, caller's wait 9786.774 ms
2026-11-17T22:56:24.3880220Z     response: {"confidence": 0.9275, "content_id": "0f552ad7-1c48-4ff3-a3f7-6966eb880b06", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-17T22:56:24.3883320Z     log entry: {"timestamp": "2026-11-17T22:56:24+00:00", "content_id": "0f552ad7-1c48-4ff3-a3f7-6966eb880b06", "creator_id": "cap-a", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 9762.933, "cold": true}
2026-11-17T22:56:24.3887150Z   -> Capstone 1 on this machine: PASS (attempts used: 1; caller's span 9787.47 ms)
2026-11-17T22:56:24.3887730Z 
2026-11-17T22:56:24.3891720Z == Capstone 4: cost and speed (cap-d) ==
2026-11-17T22:56:24.3893000Z   cold (caller's clock, Capstone 1 attempt 1 start -> passing attempt end): 9787.47 ms
2026-11-17T22:56:24.6426260Z   warm 1 (attempts 1): status 200, caller's wait 248.666 ms
2026-11-17T22:56:24.6528510Z     response: {"confidence": 0.9275, "content_id": "256cfdd2-09af-44e3-bb98-708accc912c9", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-17T22:56:24.6632280Z     log entry: {"timestamp": "2026-11-17T22:56:24+00:00", "content_id": "256cfdd2-09af-44e3-bb98-708accc912c9", "creator_id": "cap-d", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 242.13}
2026-11-17T22:56:24.8629350Z   warm 2 (attempts 1): status 200, caller's wait 218.95 ms
2026-11-17T22:56:24.8731270Z     response: {"confidence": 0.9275, "content_id": "3d2c5c29-b1e8-4374-94e3-45538da11992", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-17T22:56:24.8832860Z     log entry: {"timestamp": "2026-11-17T22:56:24+00:00", "content_id": "3d2c5c29-b1e8-4374-94e3-45538da11992", "creator_id": "cap-d", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 213.692}
2026-11-17T22:56:25.1301280Z   warm 3 (attempts 1): status 200, caller's wait 259.046 ms
2026-11-17T22:56:25.1403160Z     response: {"confidence": 0.9275, "content_id": "b33b32e2-597d-4046-a810-1c8cbd0aefaf", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-17T22:56:25.1517410Z     log entry: {"timestamp": "2026-11-17T22:56:25+00:00", "content_id": "b33b32e2-597d-4046-a810-1c8cbd0aefaf", "creator_id": "cap-d", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 255.928}
2026-11-17T22:56:25.1785900Z   memory right after the third warm answer: 1008.206 MB (psutil memory_info().rss of pid 1589, 1 MB = 1,000,000 bytes)
2026-11-17T22:56:25.1807540Z   -> Capstone 4 on this machine: FAIL (cold 9787.47 ms vs 45000; warm at most 5000 ms: 3 of 3; memory 1008.206 MB vs 900)
2026-11-17T22:56:25.1808250Z 
2026-11-17T22:56:25.1808720Z == Capstone 5: the old behaviour and the boundary (cap-e) ==
2026-11-17T22:56:25.3429770Z   #1 valid /submit: status 200, caller's wait 192.38 ms
2026-11-17T22:56:25.3604410Z     response: {"confidence": 0.9275, "content_id": "c829c52a-d730-481b-90e6-bcedaf3f3a75", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-17T22:56:25.3605500Z   #2 not JSON: status 400, caller's wait 2.158 ms
2026-11-17T22:56:25.3605890Z     response: {"error": "invalid_json", "message": "The request body must be JSON."}
2026-11-17T22:56:25.3606350Z   #3 no text field: status 422, caller's wait 3.739 ms
2026-11-17T22:56:25.3606780Z     response: {"error": "missing_field", "message": "Both text and creator_id are required."}
2026-11-17T22:56:25.3607190Z   #4 empty text: status 400, caller's wait 2.011 ms
2026-11-17T22:56:25.3607570Z     response: {"error": "empty_text", "message": "The text is empty."}
2026-11-17T22:56:25.3607960Z   #5 punctuation only: status 400, caller's wait 1.507 ms
2026-11-17T22:56:25.3608310Z     response: {"error": "no_words", "message": "The text has no words to score."}
2026-11-17T22:56:25.3608730Z   #6 492 words: status 413, caller's wait 2.97 ms
2026-11-17T22:56:25.3609200Z     response: {"error": "text_too_long", "message": "The text is too long to score. Please send at most 350 words."}
2026-11-17T22:56:25.3609630Z   #7 Hi.: status 400, caller's wait 2.475 ms
2026-11-17T22:56:25.3610250Z     response: {"error": "text_too_short", "message": "The text is too short to score. Please send at least a few sentences."}
2026-11-17T22:56:25.3640720Z   #8 appeal: status 200, caller's wait 5.833 ms
2026-11-17T22:56:25.3641350Z     response: {"content_id": "c829c52a-d730-481b-90e6-bcedaf3f3a75", "message": "Your appeal has been recorded next to the original decision.", "status": "under_review"}
2026-11-17T22:56:25.3676550Z   #9 appeal again: status 409, caller's wait 3.418 ms
2026-11-17T22:56:25.3681220Z     response: {"error": "already_appealed", "message": "This decision has already been appealed."}
2026-11-17T22:56:25.3733020Z   #10 made-up id: status 404, caller's wait 3.114 ms
2026-11-17T22:56:25.3749920Z     response: {"error": "unknown_content_id", "message": "No decision was found for that content_id."}
2026-11-17T22:56:25.3752590Z   #11 GET /health: {"detector_loaded": true, "detector_model": "gpt2", "log_entries": 407, "ok": true, "rate_limiting": true}
2026-11-17T22:56:29.3390190Z   #12 python test.py: '9 passed, 0 failed, 0 to look at, 0 skipped'
2026-11-17T22:56:29.4992270Z [2026-11-17 22:56:29,491] ERROR in app: Exception on /submit [POST]
2026-11-17T22:56:29.5093720Z Traceback (most recent call last):
2026-11-17T22:56:29.5095820Z   (a) RuntimeError in detector.model_signal (while GPT-2 scores the text): status 500, JSON body: False, new log lines: 0 (lines 407 -> 407)
2026-11-17T22:56:29.5211910Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 1511, in wsgi_app
2026-11-17T22:56:29.5314410Z     response = self.full_dispatch_request()
2026-11-17T22:56:29.5393210Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:29.5403220Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 919, in full_dispatch_request
2026-11-17T22:56:29.5430160Z     rv = self.handle_user_exception(e)
2026-11-17T22:56:29.5440530Z          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:29.5441990Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 917, in full_dispatch_request
2026-11-17T22:56:29.5443480Z     rv = self.dispatch_request()
2026-11-17T22:56:29.5444010Z          ^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:29.5445250Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 902, in dispatch_request
2026-11-17T22:56:29.5446530Z     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
2026-11-17T22:56:29.5447450Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:29.5448840Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask_limiter/extension.py", line 1314, in __inner
2026-11-17T22:56:29.5450490Z     return cast(R, flask.current_app.ensure_sync(obj)(*a, **k))
2026-11-17T22:56:29.5451040Z                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:29.5451910Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/app.py", line 305, in submit
2026-11-17T22:56:29.5452780Z     model_score = detector.model_signal(text)
2026-11-17T22:56:29.5453120Z                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:29.5453900Z   File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py", line 1139, in __call__
2026-11-17T22:56:29.5454600Z     return self._mock_call(*args, **kwargs)
2026-11-17T22:56:29.5454930Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:29.5455580Z   File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py", line 1143, in _mock_call
2026-11-17T22:56:29.5456150Z     return self._execute_mock_call(*args, **kwargs)
2026-11-17T22:56:29.5456560Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:29.5457370Z   File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py", line 1198, in _execute_mock_call
2026-11-17T22:56:29.5457930Z     raise effect
2026-11-17T22:56:29.5458300Z RuntimeError: capstone boundary check (a)
2026-11-17T22:56:34.1314300Z `loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.
2026-11-17T22:56:34.1962020Z [2026-11-17 22:56:34,187] ERROR in app: Exception on /submit [POST]
2026-11-17T22:56:34.1963040Z   (b) RuntimeError in scoring.combine_signals (while combining and labelling): status 500, JSON body: False, new log lines: 0 (lines 407 -> 407)
2026-11-17T22:56:34.2037610Z Traceback (most recent call last):
2026-11-17T22:56:34.2041810Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 1511, in wsgi_app
2026-11-17T22:56:34.2081890Z     response = self.full_dispatch_request()
2026-11-17T22:56:34.2103730Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:34.2106440Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 919, in full_dispatch_request
2026-11-17T22:56:34.2108560Z     rv = self.handle_user_exception(e)
2026-11-17T22:56:34.2109390Z          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:34.2111640Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 917, in full_dispatch_request
2026-11-17T22:56:34.2146940Z     rv = self.dispatch_request()
2026-11-17T22:56:34.2147380Z          ^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:34.2148510Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 902, in dispatch_request
2026-11-17T22:56:34.2149590Z     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
2026-11-17T22:56:34.2150200Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:34.2151210Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask_limiter/extension.py", line 1314, in __inner
2026-11-17T22:56:34.2152160Z     return cast(R, flask.current_app.ensure_sync(obj)(*a, **k))
2026-11-17T22:56:34.2152590Z                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:34.2153570Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/app.py", line 326, in submit
2026-11-17T22:56:34.2154410Z     combined_score = scoring.combine_signals(model_score, style_score)
2026-11-17T22:56:34.2154830Z                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:34.2155450Z   File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py", line 1139, in __call__
2026-11-17T22:56:34.2156000Z     return self._mock_call(*args, **kwargs)
2026-11-17T22:56:34.2156440Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:34.2157150Z   File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py", line 1143, in _mock_call
2026-11-17T22:56:34.2157830Z     return self._execute_mock_call(*args, **kwargs)
2026-11-17T22:56:34.2158260Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:34.2158810Z   File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py", line 1198, in _execute_mock_call
2026-11-17T22:56:34.2159390Z     raise effect
2026-11-17T22:56:34.2159670Z RuntimeError: capstone boundary check (b)
2026-11-17T22:56:34.4783670Z [2026-11-17 22:56:34,477] ERROR in app: Exception on /submit [POST]
2026-11-17T22:56:34.4886060Z Traceback (most recent call last):
2026-11-17T22:56:34.4888190Z   (c) RuntimeError in audit.log_decision (while writing the log): status 500, JSON body: False, new log lines: 0 (lines 407 -> 407)
2026-11-17T22:56:34.4987790Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 1511, in wsgi_app
2026-11-17T22:56:34.4989020Z     response = self.full_dispatch_request()
2026-11-17T22:56:34.4989500Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:34.4990620Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 919, in full_dispatch_request
2026-11-17T22:56:34.4991830Z     rv = self.handle_user_exception(e)
2026-11-17T22:56:34.4992680Z          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:34.4993910Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 917, in full_dispatch_request
2026-11-17T22:56:34.4996130Z     rv = self.dispatch_request()
2026-11-17T22:56:34.4996540Z          ^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:34.4998150Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 902, in dispatch_request
2026-11-17T22:56:34.4999850Z     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
2026-11-17T22:56:34.5000520Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:34.5002660Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask_limiter/extension.py", line 1314, in __inner
2026-11-17T22:56:34.5003940Z     return cast(R, flask.current_app.ensure_sync(obj)(*a, **k))
2026-11-17T22:56:34.5004780Z                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:34.5007650Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/app.py", line 342, in submit
2026-11-17T22:56:34.5009510Z     audit.log_decision(
2026-11-17T22:56:34.5010770Z   File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py", line 1139, in __call__
2026-11-17T22:56:34.5012410Z     return self._mock_call(*args, **kwargs)
2026-11-17T22:56:34.5012870Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:34.5014670Z   File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py", line 1143, in _mock_call
2026-11-17T22:56:34.5015640Z     return self._execute_mock_call(*args, **kwargs)
2026-11-17T22:56:34.5016170Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:34.5017230Z   File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py", line 1198, in _execute_mock_call
2026-11-17T22:56:34.5018060Z     raise effect
2026-11-17T22:56:34.5019040Z RuntimeError: capstone boundary check (c)
2026-11-17T22:56:34.5020480Z   -> Capstone 5 on this machine: PASS (13 of the 13 required; 15 of 15 overall; #11 True, #12 True)
2026-11-17T22:56:35.5823320Z 
2026-11-17T22:56:35.5823930Z == Capstone 3: every log entry is complete ==
2026-11-17T22:56:35.5841490Z   log lines before: 407
2026-11-17T22:57:11.5583890Z [start #2] server up on port 5050 (pid 2348); /health answers
2026-11-17T22:57:59.4556550Z [start #3 (bad model name)] server up on port 5050 (pid 3515); /health answers
2026-11-17T22:58:05.8918220Z   requests sent: 19; new log lines: 19 (expected 19 each)
2026-11-17T22:58:05.9042790Z   1 decision: status 200, caller's wait 7754.637 ms
2026-11-17T22:58:05.9101850Z     response: {"confidence": 0.9275, "content_id": "4e64ef2d-2367-416b-b795-68ab4b64c6ad", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-17T22:58:05.9105340Z     log entry: {"timestamp": "2026-11-17T22:57:19+00:00", "content_id": "4e64ef2d-2367-416b-b795-68ab4b64c6ad", "creator_id": "cap-c-decision", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 7732.467, "cold": true}
2026-11-17T22:58:05.9109490Z     duration_ms 7732.467 vs caller's wait 7754.637: complete
2026-11-17T22:58:05.9111450Z   2 repeat 1: status 200, caller's wait 291.906 ms
2026-11-17T22:58:05.9114670Z     response: {"confidence": 0.9275, "content_id": "8cec65c3-8964-4343-a925-455c660f5674", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-17T22:58:05.9411240Z     log entry: {"timestamp": "2026-11-17T22:57:19+00:00", "content_id": "8cec65c3-8964-4343-a925-455c660f5674", "creator_id": "cap-c-repeat", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 278.052}
2026-11-17T22:58:05.9413490Z     duration_ms 278.052 vs caller's wait 291.906: complete
2026-11-17T22:58:05.9414000Z   2 repeat 2: status 200, caller's wait 324.966 ms
2026-11-17T22:58:05.9704140Z     response: {"confidence": 0.9275, "content_id": "a298ac99-cd8f-496e-bbda-29751939cdde", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-17T22:58:05.9706620Z     log entry: {"timestamp": "2026-11-17T22:57:19+00:00", "content_id": "a298ac99-cd8f-496e-bbda-29751939cdde", "creator_id": "cap-c-repeat", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 315.444}
2026-11-17T22:58:05.9708950Z     duration_ms 315.444 vs caller's wait 324.966: complete
2026-11-17T22:58:05.9709480Z   2 repeat 3: status 200, caller's wait 342.805 ms
2026-11-17T22:58:05.9710400Z     response: {"confidence": 0.9275, "content_id": "3fd388a8-500d-48ff-8288-4f60ed002b7b", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-17T22:58:05.9712550Z     log entry: {"timestamp": "2026-11-17T22:57:20+00:00", "content_id": "3fd388a8-500d-48ff-8288-4f60ed002b7b", "creator_id": "cap-c-repeat", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 338.069}
2026-11-17T22:58:05.9715650Z     duration_ms 338.069 vs caller's wait 342.805: complete
2026-11-17T22:58:05.9716100Z   2 repeat 4: status 200, caller's wait 338.24 ms
2026-11-17T22:58:05.9716890Z     response: {"confidence": 0.9275, "content_id": "696837b2-ac7e-4b25-964b-80daa3d9f824", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-17T22:58:05.9721130Z     log entry: {"timestamp": "2026-11-17T22:57:20+00:00", "content_id": "696837b2-ac7e-4b25-964b-80daa3d9f824", "creator_id": "cap-c-repeat", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 333.341}
2026-11-17T22:58:05.9725420Z     duration_ms 333.341 vs caller's wait 338.24: complete
2026-11-17T22:58:05.9725900Z   2 repeat 5: status 200, caller's wait 305.882 ms
2026-11-17T22:58:05.9727380Z     response: {"confidence": 0.9275, "content_id": "305d90b1-4d8e-4312-ac2d-6dcd52e360ad", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-17T22:58:05.9732680Z     log entry: {"timestamp": "2026-11-17T22:57:20+00:00", "content_id": "305d90b1-4d8e-4312-ac2d-6dcd52e360ad", "creator_id": "cap-c-repeat", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 300.612}
2026-11-17T22:58:05.9803960Z     duration_ms 300.612 vs caller's wait 305.882: complete
2026-11-17T22:58:05.9805080Z   2 repeat 6: status 200, caller's wait 188.019 ms
2026-11-17T22:58:05.9805910Z     response: {"confidence": 0.9275, "content_id": "2a020f89-66ed-46cb-921c-b0889f0c6a89", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-17T22:58:05.9816610Z     log entry: {"timestamp": "2026-11-17T22:57:21+00:00", "content_id": "2a020f89-66ed-46cb-921c-b0889f0c6a89", "creator_id": "cap-c-repeat", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 185.13}
2026-11-17T22:58:05.9856690Z     duration_ms 185.13 vs caller's wait 188.019: complete
2026-11-17T22:58:05.9857170Z   2 repeat 7: status 200, caller's wait 188.977 ms
2026-11-17T22:58:05.9857970Z     response: {"confidence": 0.9275, "content_id": "3b528be8-41fe-4c31-806e-46d0d09d6e6b", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-17T22:58:05.9860360Z     log entry: {"timestamp": "2026-11-17T22:57:21+00:00", "content_id": "3b528be8-41fe-4c31-806e-46d0d09d6e6b", "creator_id": "cap-c-repeat", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 185.507}
2026-11-17T22:58:05.9862220Z     duration_ms 185.507 vs caller's wait 188.977: complete
2026-11-17T22:58:05.9881750Z   2 repeat 8: status 200, caller's wait 215.284 ms
2026-11-17T22:58:05.9882620Z     response: {"confidence": 0.9275, "content_id": "c76f0102-ad8a-40e2-a4e6-ab8c6b4669cc", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-17T22:58:05.9884670Z     log entry: {"timestamp": "2026-11-17T22:57:21+00:00", "content_id": "c76f0102-ad8a-40e2-a4e6-ab8c6b4669cc", "creator_id": "cap-c-repeat", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 212.423}
2026-11-17T22:58:05.9886510Z     duration_ms 212.423 vs caller's wait 215.284: complete
2026-11-17T22:58:05.9886960Z   2 repeat 9: status 200, caller's wait 266.077 ms
2026-11-17T22:58:05.9887690Z     response: {"confidence": 0.9275, "content_id": "c190195d-e16b-4005-b1c3-324f8a82d2db", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-17T22:58:05.9889710Z     log entry: {"timestamp": "2026-11-17T22:57:21+00:00", "content_id": "c190195d-e16b-4005-b1c3-324f8a82d2db", "creator_id": "cap-c-repeat", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 262.049}
2026-11-17T22:58:05.9891390Z     duration_ms 262.049 vs caller's wait 266.077: complete
2026-11-17T22:58:05.9891740Z   2 repeat 10: status 200, caller's wait 247.318 ms
2026-11-17T22:58:05.9896290Z     response: {"confidence": 0.9275, "content_id": "795160be-5377-4e8d-a590-b3288bdd6530", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-17T22:58:05.9898170Z     log entry: {"timestamp": "2026-11-17T22:57:22+00:00", "content_id": "795160be-5377-4e8d-a590-b3288bdd6530", "creator_id": "cap-c-repeat", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 243.576}
2026-11-17T22:58:05.9900330Z     duration_ms 243.576 vs caller's wait 247.318: complete
2026-11-17T22:58:05.9900750Z   2 repeat 11: status 200, caller's wait 251.888 ms
2026-11-17T22:58:05.9901440Z     response: {"confidence": 0.9275, "content_id": "8842bbb1-7365-46ab-9406-ef71ac8e168a", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-17T22:58:06.0060530Z     log entry: {"timestamp": "2026-11-17T22:57:22+00:00", "content_id": "8842bbb1-7365-46ab-9406-ef71ac8e168a", "creator_id": "cap-c-repeat", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 247.962}
2026-11-17T22:58:06.0063130Z     duration_ms 247.962 vs caller's wait 251.888: complete
2026-11-17T22:58:06.0063850Z   2 repeat 12: status 200, caller's wait 196.945 ms
2026-11-17T22:58:06.0065200Z     response: {"confidence": 0.9275, "content_id": "8a2f2e44-db87-4322-8176-863d3e3210e1", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-17T22:58:06.0107960Z     log entry: {"timestamp": "2026-11-17T22:57:22+00:00", "content_id": "8a2f2e44-db87-4322-8176-863d3e3210e1", "creator_id": "cap-c-repeat", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 192.487}
2026-11-17T22:58:06.0309630Z     duration_ms 192.487 vs caller's wait 196.945: complete
2026-11-17T22:58:06.0362360Z   2 repeat 13: status 429, caller's wait 2.101 ms
2026-11-17T22:58:06.0363420Z     response: {"error": "rate_limited", "limit": "12 per 1 minute", "message": "Too many submissions. Try again shortly."}
2026-11-17T22:58:06.0365100Z     log entry: {"timestamp": "2026-11-17T22:57:22+00:00", "content_id": null, "creator_id": "cap-c-repeat", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "rate_limited", "limit": "12 per 1 minute", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"reason": "rate_limited", "http_status": 429}, "duration_ms": 0.461}
2026-11-17T22:58:06.0366720Z     duration_ms 0.461 vs caller's wait 2.101: complete
2026-11-17T22:58:06.0367080Z   3 no text: status 422, caller's wait 1.606 ms
2026-11-17T22:58:06.0371620Z     response: {"error": "missing_field", "message": "Both text and creator_id are required."}
2026-11-17T22:58:06.0373010Z     log entry: {"timestamp": "2026-11-17T22:57:22+00:00", "content_id": null, "creator_id": "cap-c-missing", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "missing_field", "http_status": 422, "input": null, "output": {"reason": "missing_field", "http_status": 422}, "duration_ms": 0.013}
2026-11-17T22:58:06.0375070Z     duration_ms 0.013 vs caller's wait 1.606: complete
2026-11-17T22:58:06.0375520Z   4 appeal: status 200, caller's wait 3.162 ms
2026-11-17T22:58:06.0376440Z     response: {"content_id": "4e64ef2d-2367-416b-b795-68ab4b64c6ad", "message": "Your appeal has been recorded next to the original decision.", "status": "under_review"}
2026-11-17T22:58:06.0378560Z     log entry: {"timestamp": "2026-11-17T22:57:22+00:00", "content_id": "4e64ef2d-2367-416b-b795-68ab4b64c6ad", "creator_id": "cap-c-decision", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "under_review", "event": "appeal", "reasoning": "I wrote this myself.", "input": {"sha256": "da3ec48b7a7f8e0915fee0a032a004826bacd3e05c9a3916a301e9ffca7a7d1c", "words": 4}, "output": {"status": "under_review", "http_status": 200}, "duration_ms": 1.443}
2026-11-17T22:58:06.0380690Z     duration_ms 1.443 vs caller's wait 3.162: complete
2026-11-17T22:58:06.0381930Z   4 appeal again: status 409, caller's wait 3.537 ms
2026-11-17T22:58:06.0383520Z     response: {"error": "already_appealed", "message": "This decision has already been appealed."}
2026-11-17T22:58:06.0387090Z     log entry: {"timestamp": "2026-11-17T22:57:22+00:00", "content_id": null, "creator_id": "cap-c-decision", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "already_appealed", "http_status": 409, "input": {"sha256": "63b20b566dab38bcad7ce239b9e4e0193eff60470968281b0577391f7a809020", "words": 2}, "output": {"reason": "already_appealed", "http_status": 409}, "duration_ms": 1.821}
2026-11-17T22:58:06.0388710Z     duration_ms 1.821 vs caller's wait 3.537: complete
2026-11-17T22:58:06.0389160Z   4 made-up id: status 404, caller's wait 3.283 ms
2026-11-17T22:58:06.0389640Z     response: {"error": "unknown_content_id", "message": "No decision was found for that content_id."}
2026-11-17T22:58:06.0393410Z     log entry: {"timestamp": "2026-11-17T22:57:22+00:00", "content_id": null, "creator_id": "unknown", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "unknown_content_id", "http_status": 404, "input": {"sha256": "df91ca48d8fa30eecb786ffa4401e9a2bbc8a7ca2df52b8a452f2fcb61513070", "words": 4}, "output": {"reason": "unknown_content_id", "http_status": 404}, "duration_ms": 1.407}
2026-11-17T22:58:06.0395300Z     duration_ms 1.407 vs caller's wait 3.283: complete
2026-11-17T22:58:06.0397950Z   5 bad model: status 503, caller's wait 5308.662 ms
2026-11-17T22:58:06.0404280Z     response: {"error": "detector_could_not_load", "message": "Couldn't load 'no-such-model-capstone': no-such-model-capstone is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<your_token>`\nThe first run downloads about 550 MB — check your connection and that you have disk space free."}
2026-11-17T22:58:06.0820980Z     log entry: {"timestamp": "2026-11-17T22:58:04+00:00", "content_id": null, "creator_id": "cap-c-503", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "detector_could_not_load", "http_status": 503, "message": "Couldn't load 'no-such-model-capstone': no-such-model-capstone is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<your_token>`\nThe first run downloads about 550 MB — check your connection and that you have disk space free.", "model": "no-such-model-capstone", "error_type": "OSError", "failed_at": "model_load", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"reason": "detector_could_not_load", "http_status": 503}, "duration_ms": 5286.768}
2026-11-17T22:58:06.0839790Z     duration_ms 5286.768 vs caller's wait 5308.662: complete
2026-11-17T22:58:06.0841070Z   -> Capstone 3: PASS (19 of 19 complete)
2026-11-17T22:58:06.0841460Z 
2026-11-17T22:58:06.0841800Z == Capstone 2: the model can't load (cap-b) ==
2026-11-17T22:58:06.1476830Z   cause: torch
2026-11-17T22:58:45.1129580Z [cause torch] server up on port 5050 (pid 4359); /health answers
2026-11-17T22:58:46.2829470Z   cause torch: status 503, caller's wait 6.998 ms
2026-11-17T22:58:46.2831300Z     response: {"error": "detector_could_not_load", "message": "transformers or torch isn't installed (No module named 'torch').\nRun: pip install -r requirements.txt"}
2026-11-17T22:58:46.2838470Z     log entry: {"timestamp": "2026-11-17T22:58:45+00:00", "content_id": null, "creator_id": "cap-b", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "detector_could_not_load", "http_status": 503, "message": "transformers or torch isn't installed (No module named 'torch').\nRun: pip install -r requirements.txt", "model": "gpt2", "error_type": "ModuleNotFoundError", "failed_at": "model_load", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"reason": "detector_could_not_load", "http_status": 503}, "duration_ms": 0.618}
2026-11-17T22:58:46.2847970Z     checks: {"503": true, "JSON": true, "error": true, "message identical, not empty": true, "exactly one new line": true, "reason/http_status": true, "fields filled": true, "error_type exact": true, "names the module": true}  -> PASS
2026-11-17T22:59:02.6264670Z   cause: transformers
2026-11-17T22:59:40.2667480Z [cause transformers] server up on port 5050 (pid 5538); /health answers
2026-11-17T22:59:43.7148070Z   cause transformers: status 503, caller's wait 2357.632 ms
2026-11-17T22:59:43.7150230Z     response: {"error": "detector_could_not_load", "message": "transformers or torch isn't installed (No module named 'transformers').\nRun: pip install -r requirements.txt"}
2026-11-17T22:59:43.7156710Z     log entry: {"timestamp": "2026-11-17T22:59:42+00:00", "content_id": null, "creator_id": "cap-b", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "detector_could_not_load", "http_status": 503, "message": "transformers or torch isn't installed (No module named 'transformers').\nRun: pip install -r requirements.txt", "model": "gpt2", "error_type": "ModuleNotFoundError", "failed_at": "model_load", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"reason": "detector_could_not_load", "http_status": 503}, "duration_ms": 2349.086}
2026-11-17T22:59:43.7163780Z     checks: {"503": true, "JSON": true, "error": true, "message identical, not empty": true, "exactly one new line": true, "reason/http_status": true, "fields filled": true, "error_type exact": true, "names the module": true}  -> PASS
2026-11-17T22:59:53.4108860Z   cause: bad model name
2026-11-17T23:00:29.7573240Z [cause bad model name] server up on port 5050 (pid 6479); /health answers
2026-11-17T23:00:36.6444630Z   cause bad model name: status 503, caller's wait 5750.739 ms
2026-11-17T23:00:36.6472280Z     response: {"error": "detector_could_not_load", "message": "Couldn't load 'no-such-model-capstone': no-such-model-capstone is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<your_token>`\nThe first run downloads about 550 MB — check your connection and that you have disk space free."}
2026-11-17T23:00:36.6519030Z     log entry: {"timestamp": "2026-11-17T23:00:35+00:00", "content_id": null, "creator_id": "cap-b", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "detector_could_not_load", "http_status": 503, "message": "Couldn't load 'no-such-model-capstone': no-such-model-capstone is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<your_token>`\nThe first run downloads about 550 MB — check your connection and that you have disk space free.", "model": "no-such-model-capstone", "error_type": "OSError", "failed_at": "model_load", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"reason": "detector_could_not_load", "http_status": 503}, "duration_ms": 5740.643}
2026-11-17T23:00:36.6523650Z     checks: {"503": true, "JSON": true, "error": true, "message identical, not empty": true, "exactly one new line": true, "reason/http_status": true, "fields filled": true, "error_type exact": true, "names the module": true}  -> PASS
2026-11-17T23:00:36.6524380Z   -> Capstone 2: PASS (3 of 3 causes)
2026-11-17T23:00:36.6524710Z 
```

#### capstone (ubuntu-latest)
```text
﻿2026-11-17T22:56:43.7570636Z ##[group]Run if [ -f .venv/Scripts/activate ]; then source .venv/Scripts/activate; else source .venv/bin/activate; fi
2026-11-17T22:56:43.7571544Z ^[[36;1mif [ -f .venv/Scripts/activate ]; then source .venv/Scripts/activate; else source .venv/bin/activate; fi^[[0m
2026-11-17T22:56:43.7572116Z ^[[36;1mpython run_capstone.py run^[[0m
2026-11-17T22:56:43.7608064Z shell: /usr/bin/bash --noprofile --norc -e -o pipefail {0}
2026-11-17T22:56:43.7608573Z env:
2026-11-17T22:56:43.7608914Z   PYTHONUTF8: 1
2026-11-17T22:56:43.7609278Z   pythonLocation: /opt/hostedtoolcache/Python/3.12.16/x64
2026-11-17T22:56:43.7609834Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.12.16/x64/lib/pkgconfig
2026-11-17T22:56:43.7610649Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.16/x64
2026-11-17T22:56:43.7611509Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.16/x64
2026-11-17T22:56:43.7612033Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.16/x64
2026-11-17T22:56:43.7612483Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.12.16/x64/lib
2026-11-17T22:56:43.7613071Z ##[endgroup]
2026-11-17T22:56:43.8507978Z Capstone run on Linux (Python 3.12.16), commit 519dfda, run 44194503556
2026-11-17T22:56:44.4135023Z [start #1] server up on port 5050 (pid 2551); /health answers
2026-11-17T22:56:44.4135973Z 
2026-11-17T22:56:44.4136431Z == Capstone 1: first start (cap-a) ==
2026-11-17T22:56:48.5963190Z   attempt 1: status 200, caller's wait 4180.208 ms
2026-11-17T22:56:48.5964549Z     response: {"confidence": 0.9275, "content_id": "5a61799b-eb31-4864-a06e-c1823d12301e", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-17T22:56:48.5966741Z     log entry: {"timestamp": "2026-11-17T22:56:48+00:00", "content_id": "5a61799b-eb31-4864-a06e-c1823d12301e", "creator_id": "cap-a", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 4176.757, "cold": true}
2026-11-17T22:56:48.5968687Z   -> Capstone 1 on this machine: PASS (attempts used: 1; caller's span 4180.309 ms)
2026-11-17T22:56:48.5969122Z 
2026-11-17T22:56:48.5969339Z == Capstone 4: cost and speed (cap-d) ==
2026-11-17T22:56:48.5969928Z   cold (caller's clock, Capstone 1 attempt 1 start -> passing attempt end): 4180.309 ms
2026-11-17T22:56:48.8324367Z   warm 1 (attempts 1): status 200, caller's wait 233.893 ms
2026-11-17T22:56:48.8326112Z     response: {"confidence": 0.9275, "content_id": "706c2ae7-a137-4b81-b2a4-71a20ff275c9", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-17T22:56:48.8328264Z     log entry: {"timestamp": "2026-11-17T22:56:48+00:00", "content_id": "706c2ae7-a137-4b81-b2a4-71a20ff275c9", "creator_id": "cap-d", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 230.672}
2026-11-17T22:56:49.0693625Z   warm 2 (attempts 1): status 200, caller's wait 234.352 ms
2026-11-17T22:56:49.0695036Z     response: {"confidence": 0.9275, "content_id": "26836c8b-f250-4302-8b61-15f34769d187", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-17T22:56:49.0698090Z     log entry: {"timestamp": "2026-11-17T22:56:49+00:00", "content_id": "26836c8b-f250-4302-8b61-15f34769d187", "creator_id": "cap-d", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 231.26}
2026-11-17T22:56:49.2986743Z   warm 3 (attempts 1): status 200, caller's wait 226.851 ms
2026-11-17T22:56:49.2988475Z     response: {"confidence": 0.9275, "content_id": "e91a274c-0ac7-4b52-805b-875d1f3173f0", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-17T22:56:49.2991769Z     log entry: {"timestamp": "2026-11-17T22:56:49+00:00", "content_id": "e91a274c-0ac7-4b52-805b-875d1f3173f0", "creator_id": "cap-d", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 223.547}
2026-11-17T22:56:49.3087738Z   memory right after the third warm answer: 1625.084 MB (psutil memory_info().rss of pid 2551, 1 MB = 1,000,000 bytes)
2026-11-17T22:56:49.3089057Z   -> Capstone 4 on this machine: FAIL (cold 4180.309 ms vs 45000; warm at most 5000 ms: 3 of 3; memory 1625.084 MB vs 900)
2026-11-17T22:56:49.3089758Z 
2026-11-17T22:56:49.3090035Z == Capstone 5: the old behaviour and the boundary (cap-e) ==
2026-11-17T22:56:49.5371485Z   #1 valid /submit: status 200, caller's wait 228.268 ms
2026-11-17T22:56:49.5372933Z     response: {"confidence": 0.9275, "content_id": "1ab2af4f-e61a-46e8-a3b0-4384f2e07468", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-17T22:56:49.5404002Z   #2 not JSON: status 400, caller's wait 3.131 ms
2026-11-17T22:56:49.5405089Z     response: {"error": "invalid_json", "message": "The request body must be JSON."}
2026-11-17T22:56:49.5428653Z   #3 no text field: status 422, caller's wait 2.383 ms
2026-11-17T22:56:49.5429677Z     response: {"error": "missing_field", "message": "Both text and creator_id are required."}
2026-11-17T22:56:49.5450924Z   #4 empty text: status 400, caller's wait 2.124 ms
2026-11-17T22:56:49.5451683Z     response: {"error": "empty_text", "message": "The text is empty."}
2026-11-17T22:56:49.5472056Z   #5 punctuation only: status 400, caller's wait 2.02 ms
2026-11-17T22:56:49.5472837Z     response: {"error": "no_words", "message": "The text has no words to score."}
2026-11-17T22:56:49.5495023Z   #6 492 words: status 413, caller's wait 2.187 ms
2026-11-17T22:56:49.5495952Z     response: {"error": "text_too_long", "message": "The text is too long to score. Please send at most 350 words."}
2026-11-17T22:56:49.5519393Z   #7 Hi.: status 400, caller's wait 2.292 ms
2026-11-17T22:56:49.5560139Z     response: {"error": "text_too_short", "message": "The text is too short to score. Please send at least a few sentences."}
2026-11-17T22:56:49.5561070Z   #8 appeal: status 200, caller's wait 3.975 ms
2026-11-17T22:56:49.5561998Z     response: {"content_id": "1ab2af4f-e61a-46e8-a3b0-4384f2e07468", "message": "Your appeal has been recorded next to the original decision.", "status": "under_review"}
2026-11-17T22:56:49.5597350Z   #9 appeal again: status 409, caller's wait 3.621 ms
2026-11-17T22:56:49.5598357Z     response: {"error": "already_appealed", "message": "This decision has already been appealed."}
2026-11-17T22:56:49.5634203Z   #10 made-up id: status 404, caller's wait 3.555 ms
2026-11-17T22:56:49.5635101Z     response: {"error": "unknown_content_id", "message": "No decision was found for that content_id."}
2026-11-17T22:56:49.5668093Z   #11 GET /health: {"detector_loaded": true, "detector_model": "gpt2", "log_entries": 407, "ok": true, "rate_limiting": true}
2026-11-17T22:56:52.4899391Z   #12 python test.py: '9 passed, 0 failed, 0 to look at, 0 skipped'
2026-11-17T22:56:52.5890836Z [2026-11-17 22:56:52,587] ERROR in app: Exception on /submit [POST]
2026-11-17T22:56:52.5891947Z Traceback (most recent call last):
2026-11-17T22:56:52.5902506Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 1511, in wsgi_app
2026-11-17T22:56:52.5904329Z     response = self.full_dispatch_request()
2026-11-17T22:56:52.5904925Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:52.5906495Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 919, in full_dispatch_request
2026-11-17T22:56:52.5908003Z     rv = self.handle_user_exception(e)
2026-11-17T22:56:52.5908566Z          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:52.5910077Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 917, in full_dispatch_request
2026-11-17T22:56:52.5911866Z     rv = self.dispatch_request()
2026-11-17T22:56:52.5912510Z          ^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:52.5914000Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 902, in dispatch_request
2026-11-17T22:56:52.5915831Z     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
2026-11-17T22:56:52.5916822Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:52.5918380Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask_limiter/extension.py", line 1314, in __inner
2026-11-17T22:56:52.5919955Z     return cast(R, flask.current_app.ensure_sync(obj)(*a, **k))
2026-11-17T22:56:52.5920838Z                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:52.5921886Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/app.py", line 305, in submit
2026-11-17T22:56:52.5923088Z     model_score = detector.model_signal(text)
2026-11-17T22:56:52.5923625Z                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:52.5924504Z   File "/opt/hostedtoolcache/Python/3.12.16/x64/lib/python3.12/unittest/mock.py", line 1139, in __call__
2026-11-17T22:56:52.5925298Z     return self._mock_call(*args, **kwargs)
2026-11-17T22:56:52.5925797Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:52.5926597Z   File "/opt/hostedtoolcache/Python/3.12.16/x64/lib/python3.12/unittest/mock.py", line 1143, in _mock_call
2026-11-17T22:56:52.5927428Z     return self._execute_mock_call(*args, **kwargs)
2026-11-17T22:56:52.5927964Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:52.5928979Z   File "/opt/hostedtoolcache/Python/3.12.16/x64/lib/python3.12/unittest/mock.py", line 1198, in _execute_mock_call
2026-11-17T22:56:52.5929828Z     raise effect
2026-11-17T22:56:52.5930473Z RuntimeError: capstone boundary check (a)
2026-11-17T22:56:52.5931544Z   (a) RuntimeError in detector.model_signal (while GPT-2 scores the text): status 500, JSON body: False, new log lines: 0 (lines 407 -> 407)
2026-11-17T22:56:56.6561082Z `loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.
2026-11-17T22:56:56.6725469Z [2026-11-17 22:56:56,671] ERROR in app: Exception on /submit [POST]
2026-11-17T22:56:56.6726501Z Traceback (most recent call last):
2026-11-17T22:56:56.6728066Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 1511, in wsgi_app
2026-11-17T22:56:56.6729518Z     response = self.full_dispatch_request()
2026-11-17T22:56:56.6730058Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:56.6731759Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 919, in full_dispatch_request
2026-11-17T22:56:56.6733919Z     rv = self.handle_user_exception(e)
2026-11-17T22:56:56.6734491Z          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:56.6736010Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 917, in full_dispatch_request
2026-11-17T22:56:56.6737412Z     rv = self.dispatch_request()
2026-11-17T22:56:56.6737891Z          ^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:56.6739431Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 902, in dispatch_request
2026-11-17T22:56:56.6741431Z     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
2026-11-17T22:56:56.6742408Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:56.6744196Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask_limiter/extension.py", line 1314, in __inner
2026-11-17T22:56:56.6745883Z     return cast(R, flask.current_app.ensure_sync(obj)(*a, **k))
2026-11-17T22:56:56.6746619Z                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:56.6747865Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/app.py", line 326, in submit
2026-11-17T22:56:56.6749198Z     combined_score = scoring.combine_signals(model_score, style_score)
2026-11-17T22:56:56.6749934Z                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:56.6750996Z   File "/opt/hostedtoolcache/Python/3.12.16/x64/lib/python3.12/unittest/mock.py", line 1139, in __call__
2026-11-17T22:56:56.6752046Z     return self._mock_call(*args, **kwargs)
2026-11-17T22:56:56.6752605Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:56.6753524Z   File "/opt/hostedtoolcache/Python/3.12.16/x64/lib/python3.12/unittest/mock.py", line 1143, in _mock_call
2026-11-17T22:56:56.6754446Z     return self._execute_mock_call(*args, **kwargs)
2026-11-17T22:56:56.6755145Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:56.6756277Z   File "/opt/hostedtoolcache/Python/3.12.16/x64/lib/python3.12/unittest/mock.py", line 1198, in _execute_mock_call
2026-11-17T22:56:56.6757242Z     raise effect
2026-11-17T22:56:56.6757756Z RuntimeError: capstone boundary check (b)
2026-11-17T22:56:56.6764383Z   (b) RuntimeError in scoring.combine_signals (while combining and labelling): status 500, JSON body: False, new log lines: 0 (lines 407 -> 407)
2026-11-17T22:56:56.8992406Z [2026-11-17 22:56:56,898] ERROR in app: Exception on /submit [POST]
2026-11-17T22:56:56.8993849Z Traceback (most recent call last):
2026-11-17T22:56:56.8995375Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 1511, in wsgi_app
2026-11-17T22:56:56.8996793Z     response = self.full_dispatch_request()
2026-11-17T22:56:56.8997694Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:56.8998632Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 919, in full_dispatch_request
2026-11-17T22:56:56.8999537Z     rv = self.handle_user_exception(e)
2026-11-17T22:56:56.8999935Z          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:56.9001037Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 917, in full_dispatch_request
2026-11-17T22:56:56.9001920Z     rv = self.dispatch_request()
2026-11-17T22:56:56.9002371Z          ^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:56.9003233Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 902, in dispatch_request
2026-11-17T22:56:56.9004276Z     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
2026-11-17T22:56:56.9004860Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:56.9005890Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask_limiter/extension.py", line 1314, in __inner
2026-11-17T22:56:56.9006786Z     return cast(R, flask.current_app.ensure_sync(obj)(*a, **k))
2026-11-17T22:56:56.9007256Z                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:56.9008032Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/app.py", line 342, in submit
2026-11-17T22:56:56.9008742Z     audit.log_decision(
2026-11-17T22:56:56.9009280Z   File "/opt/hostedtoolcache/Python/3.12.16/x64/lib/python3.12/unittest/mock.py", line 1139, in __call__
2026-11-17T22:56:56.9009804Z     return self._mock_call(*args, **kwargs)
2026-11-17T22:56:56.9010198Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:56.9011037Z   File "/opt/hostedtoolcache/Python/3.12.16/x64/lib/python3.12/unittest/mock.py", line 1143, in _mock_call
2026-11-17T22:56:56.9011604Z     return self._execute_mock_call(*args, **kwargs)
2026-11-17T22:56:56.9012014Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:56.9012626Z   File "/opt/hostedtoolcache/Python/3.12.16/x64/lib/python3.12/unittest/mock.py", line 1198, in _execute_mock_call
2026-11-17T22:56:56.9013206Z     raise effect
2026-11-17T22:56:56.9013528Z RuntimeError: capstone boundary check (c)
2026-11-17T22:56:56.9020454Z   (c) RuntimeError in audit.log_decision (while writing the log): status 500, JSON body: False, new log lines: 0 (lines 407 -> 407)
2026-11-17T22:56:56.9021368Z   -> Capstone 5 on this machine: PASS (13 of the 13 required; 15 of 15 overall; #11 True, #12 True)
2026-11-17T22:56:57.9365342Z 
```

#### capstone (windows-latest)
```text
﻿2026-11-17T22:55:49.9791873Z ##[group]Run if [ -f .venv/Scripts/activate ]; then source .venv/Scripts/activate; else source .venv/bin/activate; fi
2026-11-17T22:55:49.9792780Z ^[[36;1mif [ -f .venv/Scripts/activate ]; then source .venv/Scripts/activate; else source .venv/bin/activate; fi^[[0m
2026-11-17T22:55:49.9793559Z ^[[36;1mpython run_capstone.py run^[[0m
2026-11-17T22:55:49.9810428Z shell: C:\Program Files\Git\bin\bash.EXE --noprofile --norc -e -o pipefail {0}
2026-11-17T22:55:49.9810813Z env:
2026-11-17T22:55:49.9810979Z   PYTHONUTF8: 1
2026-11-17T22:55:49.9811250Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-17T22:55:49.9811709Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
2026-11-17T22:55:49.9812173Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-17T22:55:49.9812594Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-17T22:55:49.9812999Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-17T22:55:49.9813659Z ##[endgroup]
2026-11-17T22:55:50.2510758Z Capstone run on Windows (Python 3.12.10), commit 519dfda, run 44194503556
2026-11-17T22:55:50.8542417Z [start #1] server up on port 5050 (pid 9716); /health answers
2026-11-17T22:55:50.8542918Z 
2026-11-17T22:55:50.8543091Z == Capstone 1: first start (cap-a) ==
2026-11-17T22:55:56.5538846Z   attempt 1: status 200, caller's wait 5696.199 ms
2026-11-17T22:55:56.5540242Z     response: {"confidence": 0.9275, "content_id": "507c7e3b-69ed-4522-a009-61ca7c43f20e", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-17T22:55:56.5542498Z     log entry: {"timestamp": "2026-11-17T22:55:56+00:00", "content_id": "507c7e3b-69ed-4522-a009-61ca7c43f20e", "creator_id": "cap-a", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 5681.977, "cold": true}
2026-11-17T22:55:56.5544403Z   -> Capstone 1 on this machine: PASS (attempts used: 1; caller's span 5696.305 ms)
2026-11-17T22:55:56.5544719Z 
2026-11-17T22:55:56.5544839Z == Capstone 4: cost and speed (cap-d) ==
2026-11-17T22:55:56.5545255Z   cold (caller's clock, Capstone 1 attempt 1 start -> passing attempt end): 5696.305 ms
2026-11-17T22:55:56.9938969Z   warm 1 (attempts 1): status 200, caller's wait 436.886 ms
2026-11-17T22:55:56.9940289Z     response: {"confidence": 0.9275, "content_id": "06831a78-7a7b-49d5-850d-413c7092120c", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-17T22:55:56.9943576Z     log entry: {"timestamp": "2026-11-17T22:55:56+00:00", "content_id": "06831a78-7a7b-49d5-850d-413c7092120c", "creator_id": "cap-d", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 421.118}
2026-11-17T22:55:57.4867252Z   warm 2 (attempts 1): status 200, caller's wait 489.642 ms
2026-11-17T22:55:57.4869090Z     response: {"confidence": 0.9275, "content_id": "a6d951f0-5697-4110-9b71-bd374425d74d", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-17T22:55:57.4872863Z     log entry: {"timestamp": "2026-11-17T22:55:57+00:00", "content_id": "a6d951f0-5697-4110-9b71-bd374425d74d", "creator_id": "cap-d", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 471.753}
2026-11-17T22:55:57.9666873Z   warm 3 (attempts 1): status 200, caller's wait 476.68 ms
2026-11-17T22:55:57.9668653Z     response: {"confidence": 0.9275, "content_id": "09f36a19-5a02-4348-a5a4-813728fc0084", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-17T22:55:57.9672508Z     log entry: {"timestamp": "2026-11-17T22:55:57+00:00", "content_id": "09f36a19-5a02-4348-a5a4-813728fc0084", "creator_id": "cap-d", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 460.546}
2026-11-17T22:55:57.9803537Z   memory right after the third warm answer: 1081.684 MB (psutil memory_info().rss of pid 2848, 1 MB = 1,000,000 bytes)
2026-11-17T22:55:57.9805110Z   -> Capstone 4 on this machine: FAIL (cold 5696.305 ms vs 45000; warm at most 5000 ms: 3 of 3; memory 1081.684 MB vs 900)
2026-11-17T22:55:57.9806194Z 
2026-11-17T22:55:57.9806472Z == Capstone 5: the old behaviour and the boundary (cap-e) ==
2026-11-17T22:55:58.5220197Z   #1 valid /submit: status 200, caller's wait 541.474 ms
2026-11-17T22:55:58.5221671Z     response: {"confidence": 0.9275, "content_id": "de602e90-95ab-4187-8df9-5570695a7f56", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-17T22:55:58.5260717Z   #2 not JSON: status 400, caller's wait 3.966 ms
2026-11-17T22:55:58.5261448Z     response: {"error": "invalid_json", "message": "The request body must be JSON."}
2026-11-17T22:55:58.5292670Z   #3 no text field: status 422, caller's wait 3.09 ms
2026-11-17T22:55:58.5293468Z     response: {"error": "missing_field", "message": "Both text and creator_id are required."}
2026-11-17T22:55:58.5479455Z   #4 empty text: status 400, caller's wait 18.56 ms
2026-11-17T22:55:58.5480127Z     response: {"error": "empty_text", "message": "The text is empty."}
2026-11-17T22:55:58.5642116Z   #5 punctuation only: status 400, caller's wait 16.091 ms
2026-11-17T22:55:58.5642880Z     response: {"error": "no_words", "message": "The text has no words to score."}
2026-11-17T22:55:58.5674677Z   #6 492 words: status 413, caller's wait 3.129 ms
2026-11-17T22:55:58.5675565Z     response: {"error": "text_too_long", "message": "The text is too long to score. Please send at most 350 words."}
2026-11-17T22:55:58.5708556Z   #7 Hi.: status 400, caller's wait 3.282 ms
2026-11-17T22:55:58.5709549Z     response: {"error": "text_too_short", "message": "The text is too short to score. Please send at least a few sentences."}
2026-11-17T22:55:58.5971487Z   #8 appeal: status 200, caller's wait 26.14 ms
2026-11-17T22:55:58.5973107Z     response: {"content_id": "de602e90-95ab-4187-8df9-5570695a7f56", "message": "Your appeal has been recorded next to the original decision.", "status": "under_review"}
2026-11-17T22:55:58.6130037Z   #9 appeal again: status 409, caller's wait 15.72 ms
2026-11-17T22:55:58.6131184Z     response: {"error": "already_appealed", "message": "This decision has already been appealed."}
2026-11-17T22:55:58.6180769Z   #10 made-up id: status 404, caller's wait 4.961 ms
2026-11-17T22:55:58.6181615Z     response: {"error": "unknown_content_id", "message": "No decision was found for that content_id."}
2026-11-17T22:55:58.6227045Z   #11 GET /health: {"detector_loaded": true, "detector_model": "gpt2", "log_entries": 407, "ok": true, "rate_limiting": true}
2026-11-17T22:56:02.3680892Z   #12 python test.py: '9 passed, 0 failed, 0 to look at, 0 skipped'
2026-11-17T22:56:02.5139623Z [2026-11-17 22:56:02,511] ERROR in app: Exception on /submit [POST]
2026-11-17T22:56:02.5141328Z Traceback (most recent call last):
2026-11-17T22:56:02.5146709Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
2026-11-17T22:56:02.5147663Z     response = self.full_dispatch_request()
2026-11-17T22:56:02.5147998Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:02.5149192Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
2026-11-17T22:56:02.5150122Z     rv = self.handle_user_exception(e)
2026-11-17T22:56:02.5150401Z          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:02.5151534Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
2026-11-17T22:56:02.5152434Z     rv = self.dispatch_request()
2026-11-17T22:56:02.5152703Z          ^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:02.5153551Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
2026-11-17T22:56:02.5154694Z     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
2026-11-17T22:56:02.5155965Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:02.5156860Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask_limiter\extension.py", line 1314, in __inner
2026-11-17T22:56:02.5157714Z     return cast(R, flask.current_app.ensure_sync(obj)(*a, **k))
2026-11-17T22:56:02.5158063Z                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:02.5158729Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\app.py", line 305, in submit
2026-11-17T22:56:02.5159408Z     model_score = detector.model_signal(text)
2026-11-17T22:56:02.5159683Z                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:02.5160149Z   File "C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\unittest\mock.py", line 1139, in __call__
2026-11-17T22:56:02.5160621Z     return self._mock_call(*args, **kwargs)
2026-11-17T22:56:02.5160881Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:02.5161339Z   File "C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\unittest\mock.py", line 1143, in _mock_call
2026-11-17T22:56:02.5161820Z     return self._execute_mock_call(*args, **kwargs)
2026-11-17T22:56:02.5162108Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:02.5162627Z   File "C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\unittest\mock.py", line 1198, in _execute_mock_call
2026-11-17T22:56:02.5163098Z     raise effect
2026-11-17T22:56:02.5163310Z RuntimeError: capstone boundary check (a)
2026-11-17T22:56:02.5169615Z   (a) RuntimeError in detector.model_signal (while GPT-2 scores the text): status 500, JSON body: False, new log lines: 0 (lines 407 -> 407)
2026-11-17T22:56:08.0050327Z `loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.
2026-11-17T22:56:08.0212400Z [2026-11-17 22:56:08,018] ERROR in app: Exception on /submit [POST]
2026-11-17T22:56:08.0213002Z Traceback (most recent call last):
2026-11-17T22:56:08.0214268Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
2026-11-17T22:56:08.0215454Z     response = self.full_dispatch_request()
2026-11-17T22:56:08.0215848Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:08.0218254Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
2026-11-17T22:56:08.0219925Z     rv = self.handle_user_exception(e)
2026-11-17T22:56:08.0220291Z          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:08.0221493Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
2026-11-17T22:56:08.0222706Z     rv = self.dispatch_request()
2026-11-17T22:56:08.0223048Z          ^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:08.0224341Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
2026-11-17T22:56:08.0225833Z     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
2026-11-17T22:56:08.0226590Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:08.0227989Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask_limiter\extension.py", line 1314, in __inner
2026-11-17T22:56:08.0229287Z     return cast(R, flask.current_app.ensure_sync(obj)(*a, **k))
2026-11-17T22:56:08.0229785Z                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:08.0231038Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\app.py", line 326, in submit
2026-11-17T22:56:08.0232335Z     combined_score = scoring.combine_signals(model_score, style_score)
2026-11-17T22:56:08.0232888Z                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:08.0233609Z   File "C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\unittest\mock.py", line 1139, in __call__
2026-11-17T22:56:08.0234302Z     return self._mock_call(*args, **kwargs)
2026-11-17T22:56:08.0234676Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:08.0235336Z   File "C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\unittest\mock.py", line 1143, in _mock_call
2026-11-17T22:56:08.0236058Z     return self._execute_mock_call(*args, **kwargs)
2026-11-17T22:56:08.0236474Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:08.0237205Z   File "C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\unittest\mock.py", line 1198, in _execute_mock_call
2026-11-17T22:56:08.0237917Z     raise effect
2026-11-17T22:56:08.0238215Z RuntimeError: capstone boundary check (b)
2026-11-17T22:56:08.0260685Z   (b) RuntimeError in scoring.combine_signals (while combining and labelling): status 500, JSON body: False, new log lines: 0 (lines 407 -> 407)
2026-11-17T22:56:08.4306400Z [2026-11-17 22:56:08,428] ERROR in app: Exception on /submit [POST]
2026-11-17T22:56:08.4306876Z Traceback (most recent call last):
2026-11-17T22:56:08.4307793Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
2026-11-17T22:56:08.4308602Z     response = self.full_dispatch_request()
2026-11-17T22:56:08.4308874Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:08.4309665Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
2026-11-17T22:56:08.4310695Z     rv = self.handle_user_exception(e)
2026-11-17T22:56:08.4310947Z          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:08.4311911Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
2026-11-17T22:56:08.4312686Z     rv = self.dispatch_request()
2026-11-17T22:56:08.4312913Z          ^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:08.4313906Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
2026-11-17T22:56:08.4315233Z     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
2026-11-17T22:56:08.4315744Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:08.4317142Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask_limiter\extension.py", line 1314, in __inner
2026-11-17T22:56:08.4318609Z     return cast(R, flask.current_app.ensure_sync(obj)(*a, **k))
2026-11-17T22:56:08.4319166Z                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:08.4320285Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\app.py", line 342, in submit
2026-11-17T22:56:08.4321379Z     audit.log_decision(
2026-11-17T22:56:08.4321938Z   File "C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\unittest\mock.py", line 1139, in __call__
2026-11-17T22:56:08.4322408Z     return self._mock_call(*args, **kwargs)
2026-11-17T22:56:08.4322687Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:08.4344085Z   File "C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\unittest\mock.py", line 1143, in _mock_call
2026-11-17T22:56:08.4345102Z     return self._execute_mock_call(*args, **kwargs)
2026-11-17T22:56:08.4345974Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-17T22:56:08.4347144Z   File "C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\unittest\mock.py", line 1198, in _execute_mock_call
2026-11-17T22:56:08.4347969Z     raise effect
2026-11-17T22:56:08.4348277Z RuntimeError: capstone boundary check (c)
2026-11-17T22:56:08.4352132Z   (c) RuntimeError in audit.log_decision (while writing the log): status 500, JSON body: False, new log lines: 0 (lines 407 -> 407)
2026-11-17T22:56:08.4353299Z   -> Capstone 5 on this machine: PASS (13 of the 13 required; 15 of 15 overall; #11 True, #12 True)
2026-11-17T22:56:09.4415059Z 
```

## Machine-readable results, all three runs

The last line of each machine's output (`CAPSTONE-RESULT`), per run.

### Run 44194503556
#### Darwin (Python 3.12.10)
```json
{
 "machine": "Darwin",
 "python": "3.12.10",
 "commit": "519dfdaf25ebb623f904f731fb24c446f890ba90",
 "run_id": "44194503556",
 "started": "2026-11-17T22:55:38+00:00",
 "c1": {
  "pass": true,
  "attempts": 1,
  "cold_span_ms": 9787.47,
  "content_id": "0f552ad7-1c48-4ff3-a3f7-6966eb880b06",
  "evidence": [
   {
    "status": 200,
    "json": {
     "confidence": 0.9275,
     "content_id": "0f552ad7-1c48-4ff3-a3f7-6966eb880b06",
     "guess": "ai",
     "label": "This is starting to be similar to AI text.",
     "model_score": 0.8551,
     "style_score": 1.0
    },
    "wait_ms": 9786.774,
    "problem": null,
    "body_start": null,
    "attempt": 1,
    "entry": {
     "timestamp": "2026-11-17T22:56:24+00:00",
     "content_id": "0f552ad7-1c48-4ff3-a3f7-6966eb880b06",
     "creator_id": "cap-a",
     "guess": "ai",
     "model_score": 0.8551,
     "style_score": 1.0,
     "combined_score": 0.9275,
     "label": "This is starting to be similar to AI text.",
     "status": "decided",
     "input": {
      "sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5",
      "words": 164
     },
     "output": {
      "guess": "ai",
      "label": "This is starting to be similar to AI text."
     },
     "duration_ms": 9762.933,
     "cold": true
    }
   }
  ]
 },
 "c4": {
  "pass": false,
  "cold_ms": 9787.47,
  "warm": [
   {
    "status": 200,
    "duration_ms": 242.13,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 213.692,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 255.928,
    "attempts": 1
   }
  ],
  "warm_under": 3,
  "memory_mb": 1008.206,
  "c1_pass": true
 },
 "c5": {
  "pass": true,
  "required_pass": 13,
  "all_pass": 15,
  "checks": {
   "#1": {
    "label": "valid /submit",
    "pass": true,
    "status": 200,
    "error": null
   },
   "#2": {
    "label": "not JSON",
    "pass": true,
    "status": 400,
    "error": "invalid_json"
   },
   "#3": {
    "label": "no text field",
    "pass": true,
    "status": 422,
    "error": "missing_field"
   },
   "#4": {
    "label": "empty text",
    "pass": true,
    "status": 400,
    "error": "empty_text"
   },
   "#5": {
    "label": "punctuation only",
    "pass": true,
    "status": 400,
    "error": "no_words"
   },
   "#6": {
    "label": "492 words",
    "pass": true,
    "status": 413,
    "error": "text_too_long"
   },
   "#7": {
    "label": "Hi.",
    "pass": true,
    "status": 400,
    "error": "text_too_short"
   },
   "#8": {
    "label": "appeal",
    "pass": true,
    "status": 200,
    "error": null
   },
   "#9": {
    "label": "appeal again",
    "pass": true,
    "status": 409,
    "error": "already_appealed"
   },
   "#10": {
    "label": "made-up id",
    "pass": true,
    "status": 404,
    "error": "unknown_content_id"
   },
   "#11": {
    "label": "GET /health",
    "pass": true,
    "status": 200
   },
   "#12": {
    "label": "python test.py",
    "pass": true,
    "summary": "9 passed, 0 failed, 0 to look at, 0 skipped"
   },
   "(a)": {
    "label": "error while GPT-2 scores the text",
    "pass": true,
    "status": 500,
    "json": false,
    "new_lines": 0
   },
   "(b)": {
    "label": "error while combining and labelling",
    "pass": true,
    "status": 500,
    "json": false,
    "new_lines": 0
   },
   "(c)": {
    "label": "error while writing the log",
    "pass": true,
    "status": 500,
    "json": false,
    "new_lines": 0
   }
  }
 },
 "c3": {
  "pass": true,
  "complete": 19,
  "sent": 19,
  "new_lines": 19,
  "rows": [
   {
    "label": "1 decision",
    "status": 200,
    "wait_ms": 7754.637,
    "duration_ms": 7732.467,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 1",
    "status": 200,
    "wait_ms": 291.906,
    "duration_ms": 278.052,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 2",
    "status": 200,
    "wait_ms": 324.966,
    "duration_ms": 315.444,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 3",
    "status": 200,
    "wait_ms": 342.805,
    "duration_ms": 338.069,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 4",
    "status": 200,
    "wait_ms": 338.24,
    "duration_ms": 333.341,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 5",
    "status": 200,
    "wait_ms": 305.882,
    "duration_ms": 300.612,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 6",
    "status": 200,
    "wait_ms": 188.019,
    "duration_ms": 185.13,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 7",
    "status": 200,
    "wait_ms": 188.977,
    "duration_ms": 185.507,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 8",
    "status": 200,
    "wait_ms": 215.284,
    "duration_ms": 212.423,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 9",
    "status": 200,
    "wait_ms": 266.077,
    "duration_ms": 262.049,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 10",
    "status": 200,
    "wait_ms": 247.318,
    "duration_ms": 243.576,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 11",
    "status": 200,
    "wait_ms": 251.888,
    "duration_ms": 247.962,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 12",
    "status": 200,
    "wait_ms": 196.945,
    "duration_ms": 192.487,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 13",
    "status": 429,
    "wait_ms": 2.101,
    "duration_ms": 0.461,
    "complete": true,
    "problems": []
   },
   {
    "label": "3 no text",
    "status": 422,
    "wait_ms": 1.606,
    "duration_ms": 0.013,
    "complete": true,
    "problems": []
   },
   {
    "label": "4 appeal",
    "status": 200,
    "wait_ms": 3.162,
    "duration_ms": 1.443,
    "complete": true,
    "problems": []
   },
   {
    "label": "4 appeal again",
    "status": 409,
    "wait_ms": 3.537,
    "duration_ms": 1.821,
    "complete": true,
    "problems": []
   },
   {
    "label": "4 made-up id",
    "status": 404,
    "wait_ms": 3.283,
    "duration_ms": 1.407,
    "complete": true,
    "problems": []
   },
   {
    "label": "5 bad model",
    "status": 503,
    "wait_ms": 5308.662,
    "duration_ms": 5286.768,
    "complete": true,
    "problems": []
   }
  ]
 },
 "c2": {
  "pass": true,
  "causes_pass": 3,
  "causes": [
   {
    "cause": "torch",
    "pass": true,
    "checks": {
     "503": true,
     "JSON": true,
     "error": true,
     "message identical, not empty": true,
     "exactly one new line": true,
     "reason/http_status": true,
     "fields filled": true,
     "error_type exact": true,
     "names the module": true
    }
   },
   {
    "cause": "transformers",
    "pass": true,
    "checks": {
     "503": true,
     "JSON": true,
     "error": true,
     "message identical, not empty": true,
     "exactly one new line": true,
     "reason/http_status": true,
     "fields filled": true,
     "error_type exact": true,
     "names the module": true
    }
   },
   {
    "cause": "bad model name",
    "pass": true,
    "checks": {
     "503": true,
     "JSON": true,
     "error": true,
     "message identical, not empty": true,
     "exactly one new line": true,
     "reason/http_status": true,
     "fields filled": true,
     "error_type exact": true,
     "names the module": true
    }
   }
  ]
 }
}
```
#### Linux (Python 3.12.16)
```json
{
 "machine": "Linux",
 "python": "3.12.16",
 "commit": "519dfdaf25ebb623f904f731fb24c446f890ba90",
 "run_id": "44194503556",
 "started": "2026-11-17T22:56:43+00:00",
 "c1": {
  "pass": true,
  "attempts": 1,
  "cold_span_ms": 4180.309,
  "content_id": "5a61799b-eb31-4864-a06e-c1823d12301e",
  "evidence": [
   {
    "status": 200,
    "json": {
     "confidence": 0.9275,
     "content_id": "5a61799b-eb31-4864-a06e-c1823d12301e",
     "guess": "ai",
     "label": "This is starting to be similar to AI text.",
     "model_score": 0.8551,
     "style_score": 1.0
    },
    "wait_ms": 4180.208,
    "problem": null,
    "body_start": null,
    "attempt": 1,
    "entry": {
     "timestamp": "2026-11-17T22:56:48+00:00",
     "content_id": "5a61799b-eb31-4864-a06e-c1823d12301e",
     "creator_id": "cap-a",
     "guess": "ai",
     "model_score": 0.8551,
     "style_score": 1.0,
     "combined_score": 0.9275,
     "label": "This is starting to be similar to AI text.",
     "status": "decided",
     "input": {
      "sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5",
      "words": 164
     },
     "output": {
      "guess": "ai",
      "label": "This is starting to be similar to AI text."
     },
     "duration_ms": 4176.757,
     "cold": true
    }
   }
  ]
 },
 "c4": {
  "pass": false,
  "cold_ms": 4180.309,
  "warm": [
   {
    "status": 200,
    "duration_ms": 230.672,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 231.26,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 223.547,
    "attempts": 1
   }
  ],
  "warm_under": 3,
  "memory_mb": 1625.084,
  "c1_pass": true
 },
 "c5": {
  "pass": true,
  "required_pass": 13,
  "all_pass": 15,
  "checks": {
   "#1": {
    "label": "valid /submit",
    "pass": true,
    "status": 200,
    "error": null
   },
   "#2": {
    "label": "not JSON",
    "pass": true,
    "status": 400,
    "error": "invalid_json"
   },
   "#3": {
    "label": "no text field",
    "pass": true,
    "status": 422,
    "error": "missing_field"
   },
   "#4": {
    "label": "empty text",
    "pass": true,
    "status": 400,
    "error": "empty_text"
   },
   "#5": {
    "label": "punctuation only",
    "pass": true,
    "status": 400,
    "error": "no_words"
   },
   "#6": {
    "label": "492 words",
    "pass": true,
    "status": 413,
    "error": "text_too_long"
   },
   "#7": {
    "label": "Hi.",
    "pass": true,
    "status": 400,
    "error": "text_too_short"
   },
   "#8": {
    "label": "appeal",
    "pass": true,
    "status": 200,
    "error": null
   },
   "#9": {
    "label": "appeal again",
    "pass": true,
    "status": 409,
    "error": "already_appealed"
   },
   "#10": {
    "label": "made-up id",
    "pass": true,
    "status": 404,
    "error": "unknown_content_id"
   },
   "#11": {
    "label": "GET /health",
    "pass": true,
    "status": 200
   },
   "#12": {
    "label": "python test.py",
    "pass": true,
    "summary": "9 passed, 0 failed, 0 to look at, 0 skipped"
   },
   "(a)": {
    "label": "error while GPT-2 scores the text",
    "pass": true,
    "status": 500,
    "json": false,
    "new_lines": 0
   },
   "(b)": {
    "label": "error while combining and labelling",
    "pass": true,
    "status": 500,
    "json": false,
    "new_lines": 0
   },
   "(c)": {
    "label": "error while writing the log",
    "pass": true,
    "status": 500,
    "json": false,
    "new_lines": 0
   }
  }
 }
}
```
#### Windows (Python 3.12.10)
```json
{
 "machine": "Windows",
 "python": "3.12.10",
 "commit": "519dfdaf25ebb623f904f731fb24c446f890ba90",
 "run_id": "44194503556",
 "started": "2026-11-17T22:55:50+00:00",
 "c1": {
  "pass": true,
  "attempts": 1,
  "cold_span_ms": 5696.305,
  "content_id": "507c7e3b-69ed-4522-a009-61ca7c43f20e",
  "evidence": [
   {
    "status": 200,
    "json": {
     "confidence": 0.9275,
     "content_id": "507c7e3b-69ed-4522-a009-61ca7c43f20e",
     "guess": "ai",
     "label": "This is starting to be similar to AI text.",
     "model_score": 0.8551,
     "style_score": 1.0
    },
    "wait_ms": 5696.199,
    "problem": null,
    "body_start": null,
    "attempt": 1,
    "entry": {
     "timestamp": "2026-11-17T22:55:56+00:00",
     "content_id": "507c7e3b-69ed-4522-a009-61ca7c43f20e",
     "creator_id": "cap-a",
     "guess": "ai",
     "model_score": 0.8551,
     "style_score": 1.0,
     "combined_score": 0.9275,
     "label": "This is starting to be similar to AI text.",
     "status": "decided",
     "input": {
      "sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5",
      "words": 164
     },
     "output": {
      "guess": "ai",
      "label": "This is starting to be similar to AI text."
     },
     "duration_ms": 5681.977,
     "cold": true
    }
   }
  ]
 },
 "c4": {
  "pass": false,
  "cold_ms": 5696.305,
  "warm": [
   {
    "status": 200,
    "duration_ms": 421.118,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 471.753,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 460.546,
    "attempts": 1
   }
  ],
  "warm_under": 3,
  "memory_mb": 1081.684,
  "c1_pass": true
 },
 "c5": {
  "pass": true,
  "required_pass": 13,
  "all_pass": 15,
  "checks": {
   "#1": {
    "label": "valid /submit",
    "pass": true,
    "status": 200,
    "error": null
   },
   "#2": {
    "label": "not JSON",
    "pass": true,
    "status": 400,
    "error": "invalid_json"
   },
   "#3": {
    "label": "no text field",
    "pass": true,
    "status": 422,
    "error": "missing_field"
   },
   "#4": {
    "label": "empty text",
    "pass": true,
    "status": 400,
    "error": "empty_text"
   },
   "#5": {
    "label": "punctuation only",
    "pass": true,
    "status": 400,
    "error": "no_words"
   },
   "#6": {
    "label": "492 words",
    "pass": true,
    "status": 413,
    "error": "text_too_long"
   },
   "#7": {
    "label": "Hi.",
    "pass": true,
    "status": 400,
    "error": "text_too_short"
   },
   "#8": {
    "label": "appeal",
    "pass": true,
    "status": 200,
    "error": null
   },
   "#9": {
    "label": "appeal again",
    "pass": true,
    "status": 409,
    "error": "already_appealed"
   },
   "#10": {
    "label": "made-up id",
    "pass": true,
    "status": 404,
    "error": "unknown_content_id"
   },
   "#11": {
    "label": "GET /health",
    "pass": true,
    "status": 200
   },
   "#12": {
    "label": "python test.py",
    "pass": true,
    "summary": "9 passed, 0 failed, 0 to look at, 0 skipped"
   },
   "(a)": {
    "label": "error while GPT-2 scores the text",
    "pass": true,
    "status": 500,
    "json": false,
    "new_lines": 0
   },
   "(b)": {
    "label": "error while combining and labelling",
    "pass": true,
    "status": 500,
    "json": false,
    "new_lines": 0
   },
   "(c)": {
    "label": "error while writing the log",
    "pass": true,
    "status": 500,
    "json": false,
    "new_lines": 0
   }
  }
 }
}
```

### Run 44196618194
#### Darwin (Python 3.12.10)
```json
{
 "machine": "Darwin",
 "python": "3.12.10",
 "commit": "519dfdaf25ebb623f904f731fb24c446f890ba90",
 "run_id": "44196618194",
 "started": "2026-11-17T23:09:10+00:00",
 "c1": {
  "pass": true,
  "attempts": 1,
  "cold_span_ms": 14037.457,
  "content_id": "e3573d55-82a0-48a4-bf2e-d5752907b523",
  "evidence": [
   {
    "status": 200,
    "json": {
     "confidence": 0.9275,
     "content_id": "e3573d55-82a0-48a4-bf2e-d5752907b523",
     "guess": "ai",
     "label": "This is starting to be similar to AI text.",
     "model_score": 0.8551,
     "style_score": 1.0
    },
    "wait_ms": 14036.114,
    "problem": null,
    "body_start": null,
    "attempt": 1,
    "entry": {
     "timestamp": "2026-11-17T23:10:00+00:00",
     "content_id": "e3573d55-82a0-48a4-bf2e-d5752907b523",
     "creator_id": "cap-a",
     "guess": "ai",
     "model_score": 0.8551,
     "style_score": 1.0,
     "combined_score": 0.9275,
     "label": "This is starting to be similar to AI text.",
     "status": "decided",
     "input": {
      "sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5",
      "words": 164
     },
     "output": {
      "guess": "ai",
      "label": "This is starting to be similar to AI text."
     },
     "duration_ms": 13992.421,
     "cold": true
    }
   }
  ]
 },
 "c4": {
  "pass": false,
  "cold_ms": 14037.457,
  "warm": [
   {
    "status": 200,
    "duration_ms": 700.31,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 371.355,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 478.891,
    "attempts": 1
   }
  ],
  "warm_under": 3,
  "memory_mb": 1043.104,
  "c1_pass": true
 },
 "c5": {
  "pass": true,
  "required_pass": 13,
  "all_pass": 15,
  "checks": {
   "#1": {
    "label": "valid /submit",
    "pass": true,
    "status": 200,
    "error": null
   },
   "#2": {
    "label": "not JSON",
    "pass": true,
    "status": 400,
    "error": "invalid_json"
   },
   "#3": {
    "label": "no text field",
    "pass": true,
    "status": 422,
    "error": "missing_field"
   },
   "#4": {
    "label": "empty text",
    "pass": true,
    "status": 400,
    "error": "empty_text"
   },
   "#5": {
    "label": "punctuation only",
    "pass": true,
    "status": 400,
    "error": "no_words"
   },
   "#6": {
    "label": "492 words",
    "pass": true,
    "status": 413,
    "error": "text_too_long"
   },
   "#7": {
    "label": "Hi.",
    "pass": true,
    "status": 400,
    "error": "text_too_short"
   },
   "#8": {
    "label": "appeal",
    "pass": true,
    "status": 200,
    "error": null
   },
   "#9": {
    "label": "appeal again",
    "pass": true,
    "status": 409,
    "error": "already_appealed"
   },
   "#10": {
    "label": "made-up id",
    "pass": true,
    "status": 404,
    "error": "unknown_content_id"
   },
   "#11": {
    "label": "GET /health",
    "pass": true,
    "status": 200
   },
   "#12": {
    "label": "python test.py",
    "pass": true,
    "summary": "9 passed, 0 failed, 0 to look at, 0 skipped"
   },
   "(a)": {
    "label": "error while GPT-2 scores the text",
    "pass": true,
    "status": 500,
    "json": false,
    "new_lines": 0
   },
   "(b)": {
    "label": "error while combining and labelling",
    "pass": true,
    "status": 500,
    "json": false,
    "new_lines": 0
   },
   "(c)": {
    "label": "error while writing the log",
    "pass": true,
    "status": 500,
    "json": false,
    "new_lines": 0
   }
  }
 },
 "c3": {
  "pass": true,
  "complete": 19,
  "sent": 19,
  "new_lines": 19,
  "rows": [
   {
    "label": "1 decision",
    "status": 200,
    "wait_ms": 5101.889,
    "duration_ms": 5088.684,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 1",
    "status": 200,
    "wait_ms": 231.997,
    "duration_ms": 224.869,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 2",
    "status": 200,
    "wait_ms": 209.659,
    "duration_ms": 205.814,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 3",
    "status": 200,
    "wait_ms": 199.235,
    "duration_ms": 196.435,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 4",
    "status": 200,
    "wait_ms": 225.197,
    "duration_ms": 222.529,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 5",
    "status": 200,
    "wait_ms": 180.58,
    "duration_ms": 177.53,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 6",
    "status": 200,
    "wait_ms": 187.841,
    "duration_ms": 184.706,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 7",
    "status": 200,
    "wait_ms": 213.213,
    "duration_ms": 207.618,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 8",
    "status": 200,
    "wait_ms": 190.615,
    "duration_ms": 185.227,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 9",
    "status": 200,
    "wait_ms": 187.79,
    "duration_ms": 184.219,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 10",
    "status": 200,
    "wait_ms": 197.346,
    "duration_ms": 194.372,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 11",
    "status": 200,
    "wait_ms": 148.908,
    "duration_ms": 146.261,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 12",
    "status": 200,
    "wait_ms": 160.593,
    "duration_ms": 158.169,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 13",
    "status": 429,
    "wait_ms": 2.954,
    "duration_ms": 0.574,
    "complete": true,
    "problems": []
   },
   {
    "label": "3 no text",
    "status": 422,
    "wait_ms": 3.108,
    "duration_ms": 0.012,
    "complete": true,
    "problems": []
   },
   {
    "label": "4 appeal",
    "status": 200,
    "wait_ms": 5.054,
    "duration_ms": 1.856,
    "complete": true,
    "problems": []
   },
   {
    "label": "4 appeal again",
    "status": 409,
    "wait_ms": 4.701,
    "duration_ms": 1.962,
    "complete": true,
    "problems": []
   },
   {
    "label": "4 made-up id",
    "status": 404,
    "wait_ms": 5.273,
    "duration_ms": 2.092,
    "complete": true,
    "problems": []
   },
   {
    "label": "5 bad model",
    "status": 503,
    "wait_ms": 3539.268,
    "duration_ms": 3534.861,
    "complete": true,
    "problems": []
   }
  ]
 },
 "c2": {
  "pass": true,
  "causes_pass": 3,
  "causes": [
   {
    "cause": "torch",
    "pass": true,
    "checks": {
     "503": true,
     "JSON": true,
     "error": true,
     "message identical, not empty": true,
     "exactly one new line": true,
     "reason/http_status": true,
     "fields filled": true,
     "error_type exact": true,
     "names the module": true
    }
   },
   {
    "cause": "transformers",
    "pass": true,
    "checks": {
     "503": true,
     "JSON": true,
     "error": true,
     "message identical, not empty": true,
     "exactly one new line": true,
     "reason/http_status": true,
     "fields filled": true,
     "error_type exact": true,
     "names the module": true
    }
   },
   {
    "cause": "bad model name",
    "pass": true,
    "checks": {
     "503": true,
     "JSON": true,
     "error": true,
     "message identical, not empty": true,
     "exactly one new line": true,
     "reason/http_status": true,
     "fields filled": true,
     "error_type exact": true,
     "names the module": true
    }
   }
  ]
 }
}
```
#### Linux (Python 3.12.16)
```json
{
 "machine": "Linux",
 "python": "3.12.16",
 "commit": "519dfdaf25ebb623f904f731fb24c446f890ba90",
 "run_id": "44196618194",
 "started": "2026-11-17T23:10:00+00:00",
 "c1": {
  "pass": true,
  "attempts": 1,
  "cold_span_ms": 4750.619,
  "content_id": "8ea8c864-3190-4826-8b5c-78ee33e8034a",
  "evidence": [
   {
    "status": 200,
    "json": {
     "confidence": 0.9275,
     "content_id": "8ea8c864-3190-4826-8b5c-78ee33e8034a",
     "guess": "ai",
     "label": "This is starting to be similar to AI text.",
     "model_score": 0.8551,
     "style_score": 1.0
    },
    "wait_ms": 4750.53,
    "problem": null,
    "body_start": null,
    "attempt": 1,
    "entry": {
     "timestamp": "2026-11-17T23:10:05+00:00",
     "content_id": "8ea8c864-3190-4826-8b5c-78ee33e8034a",
     "creator_id": "cap-a",
     "guess": "ai",
     "model_score": 0.8551,
     "style_score": 1.0,
     "combined_score": 0.9275,
     "label": "This is starting to be similar to AI text.",
     "status": "decided",
     "input": {
      "sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5",
      "words": 164
     },
     "output": {
      "guess": "ai",
      "label": "This is starting to be similar to AI text."
     },
     "duration_ms": 4747.01,
     "cold": true
    }
   }
  ]
 },
 "c4": {
  "pass": false,
  "cold_ms": 4750.619,
  "warm": [
   {
    "status": 200,
    "duration_ms": 446.753,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 441.098,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 424.634,
    "attempts": 1
   }
  ],
  "warm_under": 3,
  "memory_mb": 1654.297,
  "c1_pass": true
 },
 "c5": {
  "pass": true,
  "required_pass": 13,
  "all_pass": 15,
  "checks": {
   "#1": {
    "label": "valid /submit",
    "pass": true,
    "status": 200,
    "error": null
   },
   "#2": {
    "label": "not JSON",
    "pass": true,
    "status": 400,
    "error": "invalid_json"
   },
   "#3": {
    "label": "no text field",
    "pass": true,
    "status": 422,
    "error": "missing_field"
   },
   "#4": {
    "label": "empty text",
    "pass": true,
    "status": 400,
    "error": "empty_text"
   },
   "#5": {
    "label": "punctuation only",
    "pass": true,
    "status": 400,
    "error": "no_words"
   },
   "#6": {
    "label": "492 words",
    "pass": true,
    "status": 413,
    "error": "text_too_long"
   },
   "#7": {
    "label": "Hi.",
    "pass": true,
    "status": 400,
    "error": "text_too_short"
   },
   "#8": {
    "label": "appeal",
    "pass": true,
    "status": 200,
    "error": null
   },
   "#9": {
    "label": "appeal again",
    "pass": true,
    "status": 409,
    "error": "already_appealed"
   },
   "#10": {
    "label": "made-up id",
    "pass": true,
    "status": 404,
    "error": "unknown_content_id"
   },
   "#11": {
    "label": "GET /health",
    "pass": true,
    "status": 200
   },
   "#12": {
    "label": "python test.py",
    "pass": true,
    "summary": "9 passed, 0 failed, 0 to look at, 0 skipped"
   },
   "(a)": {
    "label": "error while GPT-2 scores the text",
    "pass": true,
    "status": 500,
    "json": false,
    "new_lines": 0
   },
   "(b)": {
    "label": "error while combining and labelling",
    "pass": true,
    "status": 500,
    "json": false,
    "new_lines": 0
   },
   "(c)": {
    "label": "error while writing the log",
    "pass": true,
    "status": 500,
    "json": false,
    "new_lines": 0
   }
  }
 }
}
```
#### Windows (Python 3.12.10)
```json
{
 "machine": "Windows",
 "python": "3.12.10",
 "commit": "519dfdaf25ebb623f904f731fb24c446f890ba90",
 "run_id": "44196618194",
 "started": "2026-11-17T23:09:42+00:00",
 "c1": {
  "pass": true,
  "attempts": 1,
  "cold_span_ms": 5723.328,
  "content_id": "51a9edd7-40fa-4bb7-81c4-3855296e382e",
  "evidence": [
   {
    "status": 200,
    "json": {
     "confidence": 0.9275,
     "content_id": "51a9edd7-40fa-4bb7-81c4-3855296e382e",
     "guess": "ai",
     "label": "This is starting to be similar to AI text.",
     "model_score": 0.8551,
     "style_score": 1.0
    },
    "wait_ms": 5723.222,
    "problem": null,
    "body_start": null,
    "attempt": 1,
    "entry": {
     "timestamp": "2026-11-17T23:09:48+00:00",
     "content_id": "51a9edd7-40fa-4bb7-81c4-3855296e382e",
     "creator_id": "cap-a",
     "guess": "ai",
     "model_score": 0.8551,
     "style_score": 1.0,
     "combined_score": 0.9275,
     "label": "This is starting to be similar to AI text.",
     "status": "decided",
     "input": {
      "sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5",
      "words": 164
     },
     "output": {
      "guess": "ai",
      "label": "This is starting to be similar to AI text."
     },
     "duration_ms": 5693.947,
     "cold": true
    }
   }
  ]
 },
 "c4": {
  "pass": false,
  "cold_ms": 5723.328,
  "warm": [
   {
    "status": 200,
    "duration_ms": 512.283,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 461.698,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 463.833,
    "attempts": 1
   }
  ],
  "warm_under": 3,
  "memory_mb": 1046.151,
  "c1_pass": true
 },
 "c5": {
  "pass": true,
  "required_pass": 13,
  "all_pass": 15,
  "checks": {
   "#1": {
    "label": "valid /submit",
    "pass": true,
    "status": 200,
    "error": null
   },
   "#2": {
    "label": "not JSON",
    "pass": true,
    "status": 400,
    "error": "invalid_json"
   },
   "#3": {
    "label": "no text field",
    "pass": true,
    "status": 422,
    "error": "missing_field"
   },
   "#4": {
    "label": "empty text",
    "pass": true,
    "status": 400,
    "error": "empty_text"
   },
   "#5": {
    "label": "punctuation only",
    "pass": true,
    "status": 400,
    "error": "no_words"
   },
   "#6": {
    "label": "492 words",
    "pass": true,
    "status": 413,
    "error": "text_too_long"
   },
   "#7": {
    "label": "Hi.",
    "pass": true,
    "status": 400,
    "error": "text_too_short"
   },
   "#8": {
    "label": "appeal",
    "pass": true,
    "status": 200,
    "error": null
   },
   "#9": {
    "label": "appeal again",
    "pass": true,
    "status": 409,
    "error": "already_appealed"
   },
   "#10": {
    "label": "made-up id",
    "pass": true,
    "status": 404,
    "error": "unknown_content_id"
   },
   "#11": {
    "label": "GET /health",
    "pass": true,
    "status": 200
   },
   "#12": {
    "label": "python test.py",
    "pass": true,
    "summary": "9 passed, 0 failed, 0 to look at, 0 skipped"
   },
   "(a)": {
    "label": "error while GPT-2 scores the text",
    "pass": true,
    "status": 500,
    "json": false,
    "new_lines": 0
   },
   "(b)": {
    "label": "error while combining and labelling",
    "pass": true,
    "status": 500,
    "json": false,
    "new_lines": 0
   },
   "(c)": {
    "label": "error while writing the log",
    "pass": true,
    "status": 500,
    "json": false,
    "new_lines": 0
   }
  }
 }
}
```

### Run 44196649907
#### Darwin (Python 3.12.10)
```json
{
 "machine": "Darwin",
 "python": "3.12.10",
 "commit": "519dfdaf25ebb623f904f731fb24c446f890ba90",
 "run_id": "44196649907",
 "started": "2026-11-17T23:09:29+00:00",
 "c1": {
  "pass": true,
  "attempts": 1,
  "cold_span_ms": 12570.265,
  "content_id": "56adc464-5e8a-46ea-9f4d-3f95714bd6a6",
  "evidence": [
   {
    "status": 200,
    "json": {
     "confidence": 0.9275,
     "content_id": "56adc464-5e8a-46ea-9f4d-3f95714bd6a6",
     "guess": "ai",
     "label": "This is starting to be similar to AI text.",
     "model_score": 0.8551,
     "style_score": 1.0
    },
    "wait_ms": 12569.468,
    "problem": null,
    "body_start": null,
    "attempt": 1,
    "entry": {
     "timestamp": "2026-11-17T23:10:18+00:00",
     "content_id": "56adc464-5e8a-46ea-9f4d-3f95714bd6a6",
     "creator_id": "cap-a",
     "guess": "ai",
     "model_score": 0.8551,
     "style_score": 1.0,
     "combined_score": 0.9275,
     "label": "This is starting to be similar to AI text.",
     "status": "decided",
     "input": {
      "sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5",
      "words": 164
     },
     "output": {
      "guess": "ai",
      "label": "This is starting to be similar to AI text."
     },
     "duration_ms": 12538.938,
     "cold": true
    }
   }
  ]
 },
 "c4": {
  "pass": false,
  "cold_ms": 12570.265,
  "warm": [
   {
    "status": 200,
    "duration_ms": 512.157,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 360.16,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 328.689,
    "attempts": 1
   }
  ],
  "warm_under": 3,
  "memory_mb": 988.234,
  "c1_pass": true
 },
 "c5": {
  "pass": true,
  "required_pass": 13,
  "all_pass": 15,
  "checks": {
   "#1": {
    "label": "valid /submit",
    "pass": true,
    "status": 200,
    "error": null
   },
   "#2": {
    "label": "not JSON",
    "pass": true,
    "status": 400,
    "error": "invalid_json"
   },
   "#3": {
    "label": "no text field",
    "pass": true,
    "status": 422,
    "error": "missing_field"
   },
   "#4": {
    "label": "empty text",
    "pass": true,
    "status": 400,
    "error": "empty_text"
   },
   "#5": {
    "label": "punctuation only",
    "pass": true,
    "status": 400,
    "error": "no_words"
   },
   "#6": {
    "label": "492 words",
    "pass": true,
    "status": 413,
    "error": "text_too_long"
   },
   "#7": {
    "label": "Hi.",
    "pass": true,
    "status": 400,
    "error": "text_too_short"
   },
   "#8": {
    "label": "appeal",
    "pass": true,
    "status": 200,
    "error": null
   },
   "#9": {
    "label": "appeal again",
    "pass": true,
    "status": 409,
    "error": "already_appealed"
   },
   "#10": {
    "label": "made-up id",
    "pass": true,
    "status": 404,
    "error": "unknown_content_id"
   },
   "#11": {
    "label": "GET /health",
    "pass": true,
    "status": 200
   },
   "#12": {
    "label": "python test.py",
    "pass": true,
    "summary": "9 passed, 0 failed, 0 to look at, 0 skipped"
   },
   "(a)": {
    "label": "error while GPT-2 scores the text",
    "pass": true,
    "status": 500,
    "json": false,
    "new_lines": 0
   },
   "(b)": {
    "label": "error while combining and labelling",
    "pass": true,
    "status": 500,
    "json": false,
    "new_lines": 0
   },
   "(c)": {
    "label": "error while writing the log",
    "pass": true,
    "status": 500,
    "json": false,
    "new_lines": 0
   }
  }
 },
 "c3": {
  "pass": true,
  "complete": 19,
  "sent": 19,
  "new_lines": 19,
  "rows": [
   {
    "label": "1 decision",
    "status": 200,
    "wait_ms": 7273.964,
    "duration_ms": 7246.794,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 1",
    "status": 200,
    "wait_ms": 278.493,
    "duration_ms": 272.0,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 2",
    "status": 200,
    "wait_ms": 257.47,
    "duration_ms": 254.392,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 3",
    "status": 200,
    "wait_ms": 226.552,
    "duration_ms": 222.829,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 4",
    "status": 200,
    "wait_ms": 231.688,
    "duration_ms": 229.022,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 5",
    "status": 200,
    "wait_ms": 242.254,
    "duration_ms": 238.389,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 6",
    "status": 200,
    "wait_ms": 278.522,
    "duration_ms": 275.527,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 7",
    "status": 200,
    "wait_ms": 431.667,
    "duration_ms": 427.074,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 8",
    "status": 200,
    "wait_ms": 379.33,
    "duration_ms": 375.668,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 9",
    "status": 200,
    "wait_ms": 138.871,
    "duration_ms": 136.436,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 10",
    "status": 200,
    "wait_ms": 138.529,
    "duration_ms": 136.372,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 11",
    "status": 200,
    "wait_ms": 135.75,
    "duration_ms": 133.608,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 12",
    "status": 200,
    "wait_ms": 141.425,
    "duration_ms": 139.053,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 13",
    "status": 429,
    "wait_ms": 2.165,
    "duration_ms": 0.415,
    "complete": true,
    "problems": []
   },
   {
    "label": "3 no text",
    "status": 422,
    "wait_ms": 1.631,
    "duration_ms": 0.006,
    "complete": true,
    "problems": []
   },
   {
    "label": "4 appeal",
    "status": 200,
    "wait_ms": 3.674,
    "duration_ms": 1.858,
    "complete": true,
    "problems": []
   },
   {
    "label": "4 appeal again",
    "status": 409,
    "wait_ms": 3.414,
    "duration_ms": 1.526,
    "complete": true,
    "problems": []
   },
   {
    "label": "4 made-up id",
    "status": 404,
    "wait_ms": 2.768,
    "duration_ms": 1.216,
    "complete": true,
    "problems": []
   },
   {
    "label": "5 bad model",
    "status": 503,
    "wait_ms": 5086.442,
    "duration_ms": 5072.781,
    "complete": true,
    "problems": []
   }
  ]
 },
 "c2": {
  "pass": true,
  "causes_pass": 3,
  "causes": [
   {
    "cause": "torch",
    "pass": true,
    "checks": {
     "503": true,
     "JSON": true,
     "error": true,
     "message identical, not empty": true,
     "exactly one new line": true,
     "reason/http_status": true,
     "fields filled": true,
     "error_type exact": true,
     "names the module": true
    }
   },
   {
    "cause": "transformers",
    "pass": true,
    "checks": {
     "503": true,
     "JSON": true,
     "error": true,
     "message identical, not empty": true,
     "exactly one new line": true,
     "reason/http_status": true,
     "fields filled": true,
     "error_type exact": true,
     "names the module": true
    }
   },
   {
    "cause": "bad model name",
    "pass": true,
    "checks": {
     "503": true,
     "JSON": true,
     "error": true,
     "message identical, not empty": true,
     "exactly one new line": true,
     "reason/http_status": true,
     "fields filled": true,
     "error_type exact": true,
     "names the module": true
    }
   }
  ]
 }
}
```
#### Linux (Python 3.12.16)
```json
{
 "machine": "Linux",
 "python": "3.12.16",
 "commit": "519dfdaf25ebb623f904f731fb24c446f890ba90",
 "run_id": "44196649907",
 "started": "2026-11-17T23:10:13+00:00",
 "c1": {
  "pass": true,
  "attempts": 1,
  "cold_span_ms": 4355.947,
  "content_id": "e21daca8-4336-4a76-bdbe-8b4ecdda20ef",
  "evidence": [
   {
    "status": 200,
    "json": {
     "confidence": 0.9275,
     "content_id": "e21daca8-4336-4a76-bdbe-8b4ecdda20ef",
     "guess": "ai",
     "label": "This is starting to be similar to AI text.",
     "model_score": 0.8551,
     "style_score": 1.0
    },
    "wait_ms": 4355.861,
    "problem": null,
    "body_start": null,
    "attempt": 1,
    "entry": {
     "timestamp": "2026-11-17T23:10:18+00:00",
     "content_id": "e21daca8-4336-4a76-bdbe-8b4ecdda20ef",
     "creator_id": "cap-a",
     "guess": "ai",
     "model_score": 0.8551,
     "style_score": 1.0,
     "combined_score": 0.9275,
     "label": "This is starting to be similar to AI text.",
     "status": "decided",
     "input": {
      "sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5",
      "words": 164
     },
     "output": {
      "guess": "ai",
      "label": "This is starting to be similar to AI text."
     },
     "duration_ms": 4353.015,
     "cold": true
    }
   }
  ]
 },
 "c4": {
  "pass": false,
  "cold_ms": 4355.947,
  "warm": [
   {
    "status": 200,
    "duration_ms": 375.517,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 378.055,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 406.997,
    "attempts": 1
   }
  ],
  "warm_under": 3,
  "memory_mb": 1653.49,
  "c1_pass": true
 },
 "c5": {
  "pass": true,
  "required_pass": 13,
  "all_pass": 15,
  "checks": {
   "#1": {
    "label": "valid /submit",
    "pass": true,
    "status": 200,
    "error": null
   },
   "#2": {
    "label": "not JSON",
    "pass": true,
    "status": 400,
    "error": "invalid_json"
   },
   "#3": {
    "label": "no text field",
    "pass": true,
    "status": 422,
    "error": "missing_field"
   },
   "#4": {
    "label": "empty text",
    "pass": true,
    "status": 400,
    "error": "empty_text"
   },
   "#5": {
    "label": "punctuation only",
    "pass": true,
    "status": 400,
    "error": "no_words"
   },
   "#6": {
    "label": "492 words",
    "pass": true,
    "status": 413,
    "error": "text_too_long"
   },
   "#7": {
    "label": "Hi.",
    "pass": true,
    "status": 400,
    "error": "text_too_short"
   },
   "#8": {
    "label": "appeal",
    "pass": true,
    "status": 200,
    "error": null
   },
   "#9": {
    "label": "appeal again",
    "pass": true,
    "status": 409,
    "error": "already_appealed"
   },
   "#10": {
    "label": "made-up id",
    "pass": true,
    "status": 404,
    "error": "unknown_content_id"
   },
   "#11": {
    "label": "GET /health",
    "pass": true,
    "status": 200
   },
   "#12": {
    "label": "python test.py",
    "pass": true,
    "summary": "9 passed, 0 failed, 0 to look at, 0 skipped"
   },
   "(a)": {
    "label": "error while GPT-2 scores the text",
    "pass": true,
    "status": 500,
    "json": false,
    "new_lines": 0
   },
   "(b)": {
    "label": "error while combining and labelling",
    "pass": true,
    "status": 500,
    "json": false,
    "new_lines": 0
   },
   "(c)": {
    "label": "error while writing the log",
    "pass": true,
    "status": 500,
    "json": false,
    "new_lines": 0
   }
  }
 }
}
```
#### Windows (Python 3.12.10)
```json
{
 "machine": "Windows",
 "python": "3.12.10",
 "commit": "519dfdaf25ebb623f904f731fb24c446f890ba90",
 "run_id": "44196649907",
 "started": "2026-11-17T23:09:56+00:00",
 "c1": {
  "pass": true,
  "attempts": 1,
  "cold_span_ms": 6253.829,
  "content_id": "7132730a-c92a-4daf-86c2-e8a82904396d",
  "evidence": [
   {
    "status": 200,
    "json": {
     "confidence": 0.9275,
     "content_id": "7132730a-c92a-4daf-86c2-e8a82904396d",
     "guess": "ai",
     "label": "This is starting to be similar to AI text.",
     "model_score": 0.8551,
     "style_score": 1.0
    },
    "wait_ms": 6253.722,
    "problem": null,
    "body_start": null,
    "attempt": 1,
    "entry": {
     "timestamp": "2026-11-17T23:10:02+00:00",
     "content_id": "7132730a-c92a-4daf-86c2-e8a82904396d",
     "creator_id": "cap-a",
     "guess": "ai",
     "model_score": 0.8551,
     "style_score": 1.0,
     "combined_score": 0.9275,
     "label": "This is starting to be similar to AI text.",
     "status": "decided",
     "input": {
      "sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5",
      "words": 164
     },
     "output": {
      "guess": "ai",
      "label": "This is starting to be similar to AI text."
     },
     "duration_ms": 6248.803,
     "cold": true
    }
   }
  ]
 },
 "c4": {
  "pass": false,
  "cold_ms": 6253.829,
  "warm": [
   {
    "status": 200,
    "duration_ms": 482.554,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 470.663,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 450.262,
    "attempts": 1
   }
  ],
  "warm_under": 3,
  "memory_mb": 1045.987,
  "c1_pass": true
 },
 "c5": {
  "pass": true,
  "required_pass": 13,
  "all_pass": 15,
  "checks": {
   "#1": {
    "label": "valid /submit",
    "pass": true,
    "status": 200,
    "error": null
   },
   "#2": {
    "label": "not JSON",
    "pass": true,
    "status": 400,
    "error": "invalid_json"
   },
   "#3": {
    "label": "no text field",
    "pass": true,
    "status": 422,
    "error": "missing_field"
   },
   "#4": {
    "label": "empty text",
    "pass": true,
    "status": 400,
    "error": "empty_text"
   },
   "#5": {
    "label": "punctuation only",
    "pass": true,
    "status": 400,
    "error": "no_words"
   },
   "#6": {
    "label": "492 words",
    "pass": true,
    "status": 413,
    "error": "text_too_long"
   },
   "#7": {
    "label": "Hi.",
    "pass": true,
    "status": 400,
    "error": "text_too_short"
   },
   "#8": {
    "label": "appeal",
    "pass": true,
    "status": 200,
    "error": null
   },
   "#9": {
    "label": "appeal again",
    "pass": true,
    "status": 409,
    "error": "already_appealed"
   },
   "#10": {
    "label": "made-up id",
    "pass": true,
    "status": 404,
    "error": "unknown_content_id"
   },
   "#11": {
    "label": "GET /health",
    "pass": true,
    "status": 200
   },
   "#12": {
    "label": "python test.py",
    "pass": true,
    "summary": "9 passed, 0 failed, 0 to look at, 0 skipped"
   },
   "(a)": {
    "label": "error while GPT-2 scores the text",
    "pass": true,
    "status": 500,
    "json": false,
    "new_lines": 0
   },
   "(b)": {
    "label": "error while combining and labelling",
    "pass": true,
    "status": 500,
    "json": false,
    "new_lines": 0
   },
   "(c)": {
    "label": "error while writing the log",
    "pass": true,
    "status": 500,
    "json": false,
    "new_lines": 0
   }
  }
 }
}
```

