# Capstone run: after

- Produced by: `run_capstone.py::cmd_run` on each GitHub machine (workflow `.github/workflows/capstone.yml`); this file by `run_capstone.py::cmd_report` from the runs' pages (`gh run view --log`)
- Date: 2026-11-17
- Git commit tested: b6298c3
- Workflow runs (trials): 44211042368, 44211062395, 44211083234
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

### Run 44211042368, copied from the run's page (step "Capstone run")

Every request, its response, the caller's wait and the new lines of `logs/audit.jsonl`, as printed by `run_capstone.py::cmd_run` (Capstone 1 `capstone_1`, 4 `capstone_4`, 5 `capstone_5`, 3 `capstone_3`, 2 `capstone_2`). The tracebacks under Capstone 5 are the three errors it makes happen on purpose.

#### capstone (macos-latest)
```text
﻿2026-11-18T00:50:54.2088260Z ##[group]Run if [ -f .venv/Scripts/activate ]; then source .venv/Scripts/activate; else source .venv/bin/activate; fi
2026-11-18T00:50:54.2089060Z ^[[36;1mif [ -f .venv/Scripts/activate ]; then source .venv/Scripts/activate; else source .venv/bin/activate; fi^[[0m
2026-11-18T00:50:54.2089510Z ^[[36;1mpython run_capstone.py run^[[0m
2026-11-18T00:50:54.2155450Z shell: /bin/bash --noprofile --norc -e -o pipefail {0}
2026-11-18T00:50:54.2156580Z env:
2026-11-18T00:50:54.2156750Z   PYTHONUTF8: 1
2026-11-18T00:50:54.2157020Z   pythonLocation: /Users/runner/hostedtoolcache/Python/3.12.10/arm64
2026-11-18T00:50:54.2157690Z   PKG_CONFIG_PATH: /Users/runner/hostedtoolcache/Python/3.12.10/arm64/lib/pkgconfig
2026-11-18T00:50:54.2158230Z   Python_ROOT_DIR: /Users/runner/hostedtoolcache/Python/3.12.10/arm64
2026-11-18T00:50:54.2158730Z   Python2_ROOT_DIR: /Users/runner/hostedtoolcache/Python/3.12.10/arm64
2026-11-18T00:50:54.2159110Z   Python3_ROOT_DIR: /Users/runner/hostedtoolcache/Python/3.12.10/arm64
2026-11-18T00:50:54.2159660Z ##[endgroup]
2026-11-18T00:50:54.3342390Z Capstone run on Darwin (Python 3.12.10), commit b6298c3, run 44211042368
2026-11-18T00:51:30.4297050Z [start #1] server up on port 5050 (pid 2446); /health answers
2026-11-18T00:51:30.4298050Z 
2026-11-18T00:51:30.4298390Z == Capstone 1: first start (cap-a) ==
2026-11-18T00:51:32.9345080Z   attempt 1: status 200, caller's wait 2501.618 ms
2026-11-18T00:51:32.9346020Z     response: {"confidence": 0.9275, "content_id": "e5f29a6a-ad46-4cab-b186-ade3d8ada61f", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-18T00:51:32.9348090Z     log entry: {"timestamp": "2026-11-18T00:51:32+00:00", "content_id": "e5f29a6a-ad46-4cab-b186-ade3d8ada61f", "creator_id": "cap-a", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 2496.942, "cold": true}
2026-11-18T00:51:32.9350030Z   -> Capstone 1 on this machine: PASS (attempts used: 1; caller's span 2501.677 ms)
2026-11-18T00:51:32.9350340Z 
2026-11-18T00:51:32.9350480Z == Capstone 4: cost and speed (cap-d) ==
2026-11-18T00:51:32.9350880Z   cold (caller's clock, Capstone 1 attempt 1 start -> passing attempt end): 2501.677 ms
2026-11-18T00:51:33.0865720Z   warm 1 (attempts 1): status 200, caller's wait 150.535 ms
2026-11-18T00:51:33.0866710Z     response: {"confidence": 0.9275, "content_id": "585437b9-ffc9-4a54-af66-451005acd597", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-18T00:51:33.0868640Z     log entry: {"timestamp": "2026-11-18T00:51:33+00:00", "content_id": "585437b9-ffc9-4a54-af66-451005acd597", "creator_id": "cap-d", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 147.711}
2026-11-18T00:51:33.2384090Z   warm 2 (attempts 1): status 200, caller's wait 150.23 ms
2026-11-18T00:51:33.2384980Z     response: {"confidence": 0.9275, "content_id": "ecc3bcb8-5390-4653-be9f-03c9cb28c486", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-18T00:51:33.2387000Z     log entry: {"timestamp": "2026-11-18T00:51:33+00:00", "content_id": "ecc3bcb8-5390-4653-be9f-03c9cb28c486", "creator_id": "cap-d", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 147.538}
2026-11-18T00:51:33.3890760Z   warm 3 (attempts 1): status 200, caller's wait 149.305 ms
2026-11-18T00:51:33.3891570Z     response: {"confidence": 0.9275, "content_id": "07a08afc-dbeb-4334-bcde-f2746cff71a0", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-18T00:51:33.3893810Z     log entry: {"timestamp": "2026-11-18T00:51:33+00:00", "content_id": "07a08afc-dbeb-4334-bcde-f2746cff71a0", "creator_id": "cap-d", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 146.704}
2026-11-18T00:51:33.3967360Z   memory right after the third warm answer: 1052.541 MB (psutil memory_info().rss of pid 2446, 1 MB = 1,000,000 bytes)
2026-11-18T00:51:33.3967990Z   -> Capstone 4 on this machine: FAIL (cold 2501.677 ms vs 45000; warm at most 5000 ms: 3 of 3; memory 1052.541 MB vs 900)
2026-11-18T00:51:33.3968340Z 
2026-11-18T00:51:33.3968500Z == Capstone 5: the old behaviour and the boundary (cap-e) ==
2026-11-18T00:51:33.5450460Z   #1 valid /submit: status 200, caller's wait 148.049 ms
2026-11-18T00:51:33.5451240Z     response: {"confidence": 0.9275, "content_id": "69d25ef7-ce2f-4f0b-b180-ac44733a11cc", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-18T00:51:33.5475660Z   #2 not JSON: status 400, caller's wait 2.48 ms
2026-11-18T00:51:33.5476700Z     response: {"error": "invalid_json", "message": "The request body must be JSON."}
2026-11-18T00:51:33.5493880Z   #3 no text field: status 422, caller's wait 1.811 ms
2026-11-18T00:51:33.5494320Z     response: {"error": "missing_field", "message": "Both text and creator_id are required."}
2026-11-18T00:51:33.5511040Z   #4 empty text: status 400, caller's wait 1.659 ms
2026-11-18T00:51:33.5511400Z     response: {"error": "empty_text", "message": "The text is empty."}
2026-11-18T00:51:33.5531520Z   #5 punctuation only: status 400, caller's wait 2.005 ms
2026-11-18T00:51:33.5532120Z     response: {"error": "no_words", "message": "The text has no words to score."}
2026-11-18T00:51:33.5550040Z   #6 492 words: status 413, caller's wait 1.76 ms
2026-11-18T00:51:33.5550580Z     response: {"error": "text_too_long", "message": "The text is too long to score. Please send at most 350 words."}
2026-11-18T00:51:33.5569560Z   #7 Hi.: status 400, caller's wait 1.869 ms
2026-11-18T00:51:33.5570090Z     response: {"error": "text_too_short", "message": "The text is too short to score. Please send at least a few sentences."}
2026-11-18T00:51:33.5601250Z   #8 appeal: status 200, caller's wait 3.104 ms
2026-11-18T00:51:33.5602000Z     response: {"content_id": "69d25ef7-ce2f-4f0b-b180-ac44733a11cc", "message": "Your appeal has been recorded next to the original decision.", "status": "under_review"}
2026-11-18T00:51:33.5631330Z   #9 appeal again: status 409, caller's wait 2.946 ms
2026-11-18T00:51:33.5631810Z     response: {"error": "already_appealed", "message": "This decision has already been appealed."}
2026-11-18T00:51:33.5663030Z   #10 made-up id: status 404, caller's wait 3.043 ms
2026-11-18T00:51:33.5664020Z     response: {"error": "unknown_content_id", "message": "No decision was found for that content_id."}
2026-11-18T00:51:33.5691020Z   #11 GET /health: {"detector_loaded": true, "detector_model": "gpt2", "log_entries": 407, "ok": true, "rate_limiting": true}
2026-11-18T00:51:35.3407480Z   #12 python test.py: '9 passed, 0 failed, 0 to look at, 0 skipped'
2026-11-18T00:51:35.4157300Z [2026-11-18 00:51:35,412] ERROR in app: Exception on /submit [POST]
2026-11-18T00:51:35.4157720Z Traceback (most recent call last):
2026-11-18T00:51:35.4163030Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 1511, in wsgi_app
2026-11-18T00:51:35.4163660Z     response = self.full_dispatch_request()
2026-11-18T00:51:35.4163850Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:35.4164500Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 919, in full_dispatch_request
2026-11-18T00:51:35.4165480Z     rv = self.handle_user_exception(e)
2026-11-18T00:51:35.4165660Z          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:35.4166360Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 917, in full_dispatch_request
2026-11-18T00:51:35.4166980Z     rv = self.dispatch_request()
2026-11-18T00:51:35.4167150Z          ^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:35.4167770Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 902, in dispatch_request
2026-11-18T00:51:35.4168530Z     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
2026-11-18T00:51:35.4169040Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:35.4169870Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask_limiter/extension.py", line 1314, in __inner
2026-11-18T00:51:35.4170650Z     return cast(R, flask.current_app.ensure_sync(obj)(*a, **k))
2026-11-18T00:51:35.4171200Z                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:35.4171790Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/app.py", line 305, in submit
2026-11-18T00:51:35.4172450Z     model_score = detector.model_signal(text)
2026-11-18T00:51:35.4178400Z                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:35.4178920Z   File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py", line 1139, in __call__
2026-11-18T00:51:35.4179300Z     return self._mock_call(*args, **kwargs)
2026-11-18T00:51:35.4179490Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:35.4179930Z   File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py", line 1143, in _mock_call
2026-11-18T00:51:35.4180380Z     return self._execute_mock_call(*args, **kwargs)
2026-11-18T00:51:35.4180580Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:35.4181010Z   File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py", line 1198, in _execute_mock_call
2026-11-18T00:51:35.4181480Z     raise effect
2026-11-18T00:51:35.4181660Z RuntimeError: capstone boundary check (a)
2026-11-18T00:51:35.4182090Z   (a) RuntimeError in detector.model_signal (while GPT-2 scores the text): status 500, JSON body: False, new log lines: 0 (lines 407 -> 407)
2026-11-18T00:51:38.0396030Z `loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.
2026-11-18T00:51:38.0508150Z [2026-11-18 00:51:38,050] ERROR in app: Exception on /submit [POST]
2026-11-18T00:51:38.0508470Z Traceback (most recent call last):
2026-11-18T00:51:38.0509230Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 1511, in wsgi_app
2026-11-18T00:51:38.0510000Z     response = self.full_dispatch_request()
2026-11-18T00:51:38.0510230Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:38.0511130Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 919, in full_dispatch_request
2026-11-18T00:51:38.0512610Z     rv = self.handle_user_exception(e)
2026-11-18T00:51:38.0512830Z          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:38.0513590Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 917, in full_dispatch_request
2026-11-18T00:51:38.0514480Z     rv = self.dispatch_request()
2026-11-18T00:51:38.0514640Z          ^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:38.0515300Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 902, in dispatch_request
2026-11-18T00:51:38.0516140Z     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
2026-11-18T00:51:38.0516510Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:38.0517220Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask_limiter/extension.py", line 1314, in __inner
2026-11-18T00:51:38.0518000Z     return cast(R, flask.current_app.ensure_sync(obj)(*a, **k))
2026-11-18T00:51:38.0518260Z                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:38.0518770Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/app.py", line 326, in submit
2026-11-18T00:51:38.0519380Z     combined_score = scoring.combine_signals(model_score, style_score)
2026-11-18T00:51:38.0519730Z                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:38.0520240Z   File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py", line 1139, in __call__
2026-11-18T00:51:38.0520620Z     return self._mock_call(*args, **kwargs)
2026-11-18T00:51:38.0520840Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:38.0521290Z   File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py", line 1143, in _mock_call
2026-11-18T00:51:38.0521720Z     return self._execute_mock_call(*args, **kwargs)
2026-11-18T00:51:38.0522000Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:38.0522420Z   File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py", line 1198, in _execute_mock_call
2026-11-18T00:51:38.0522800Z     raise effect
2026-11-18T00:51:38.0522950Z RuntimeError: capstone boundary check (b)
2026-11-18T00:51:38.0534480Z   (b) RuntimeError in scoring.combine_signals (while combining and labelling): status 500, JSON body: False, new log lines: 0 (lines 407 -> 407)
2026-11-18T00:51:38.2064900Z [2026-11-18 00:51:38,205] ERROR in app: Exception on /submit [POST]
2026-11-18T00:51:38.2065360Z Traceback (most recent call last):
2026-11-18T00:51:38.2066220Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 1511, in wsgi_app
2026-11-18T00:51:38.2066850Z     response = self.full_dispatch_request()
2026-11-18T00:51:38.2067040Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:38.2067700Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 919, in full_dispatch_request
2026-11-18T00:51:38.2068340Z     rv = self.handle_user_exception(e)
2026-11-18T00:51:38.2068520Z          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:38.2069140Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 917, in full_dispatch_request
2026-11-18T00:51:38.2070320Z     rv = self.dispatch_request()
2026-11-18T00:51:38.2070480Z          ^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:38.2071080Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 902, in dispatch_request
2026-11-18T00:51:38.2071850Z     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
2026-11-18T00:51:38.2072470Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:38.2073280Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask_limiter/extension.py", line 1314, in __inner
2026-11-18T00:51:38.2074000Z     return cast(R, flask.current_app.ensure_sync(obj)(*a, **k))
2026-11-18T00:51:38.2074240Z                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:38.2074780Z   File "/Users/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/app.py", line 342, in submit
2026-11-18T00:51:38.2075260Z     audit.log_decision(
2026-11-18T00:51:38.2075600Z   File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py", line 1139, in __call__
2026-11-18T00:51:38.2075990Z     return self._mock_call(*args, **kwargs)
2026-11-18T00:51:38.2076190Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:38.2076570Z   File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py", line 1143, in _mock_call
2026-11-18T00:51:38.2076950Z     return self._execute_mock_call(*args, **kwargs)
2026-11-18T00:51:38.2077160Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:38.2077600Z   File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py", line 1198, in _execute_mock_call
2026-11-18T00:51:38.2078070Z     raise effect
2026-11-18T00:51:38.2078260Z RuntimeError: capstone boundary check (c)
2026-11-18T00:51:38.2078670Z   (c) RuntimeError in audit.log_decision (while writing the log): status 500, JSON body: False, new log lines: 0 (lines 407 -> 407)
2026-11-18T00:51:38.2079180Z   -> Capstone 5 on this machine: PASS (13 of the 13 required; 15 of 15 overall; #11 True, #12 True)
2026-11-18T00:51:39.3056760Z 
2026-11-18T00:51:39.3058180Z == Capstone 3: every log entry is complete ==
2026-11-18T00:51:39.3121550Z   log lines before: 407
2026-11-18T00:52:15.1394680Z [start #2] server up on port 5050 (pid 3032); /health answers
2026-11-18T00:52:56.7265780Z [start #3 (bad model name)] server up on port 5050 (pid 3711); /health answers
2026-11-18T00:52:59.8758430Z   requests sent: 19; new log lines: 19 (expected 19 each)
2026-11-18T00:52:59.8759160Z   1 decision: status 200, caller's wait 2779.392 ms
2026-11-18T00:52:59.8760470Z     response: {"confidence": 0.9275, "content_id": "0daf2e11-0140-42f8-a869-c4bdc50f8467", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-18T00:52:59.8764310Z     log entry: {"timestamp": "2026-11-18T00:52:17+00:00", "content_id": "0daf2e11-0140-42f8-a869-c4bdc50f8467", "creator_id": "cap-c-decision", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 2776.807, "cold": true}
2026-11-18T00:52:59.8767380Z     duration_ms 2776.807 vs caller's wait 2779.392: complete
2026-11-18T00:52:59.8767980Z   2 repeat 1: status 200, caller's wait 169.209 ms
2026-11-18T00:52:59.8769260Z     response: {"confidence": 0.9275, "content_id": "af4e2d0f-cb76-462a-a957-007f5b97b451", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-18T00:52:59.8774230Z     log entry: {"timestamp": "2026-11-18T00:52:18+00:00", "content_id": "af4e2d0f-cb76-462a-a957-007f5b97b451", "creator_id": "cap-c-repeat", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 166.142}
2026-11-18T00:52:59.8777990Z     duration_ms 166.142 vs caller's wait 169.209: complete
2026-11-18T00:52:59.8778540Z   2 repeat 2: status 200, caller's wait 147.707 ms
2026-11-18T00:52:59.8779890Z     response: {"confidence": 0.9275, "content_id": "e98e6d1f-1e85-4e4c-9baf-c0d55a8d7206", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-18T00:52:59.8783640Z     log entry: {"timestamp": "2026-11-18T00:52:18+00:00", "content_id": "e98e6d1f-1e85-4e4c-9baf-c0d55a8d7206", "creator_id": "cap-c-repeat", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 145.438}
2026-11-18T00:52:59.8786640Z     duration_ms 145.438 vs caller's wait 147.707: complete
2026-11-18T00:52:59.8787310Z   2 repeat 3: status 200, caller's wait 139.833 ms
2026-11-18T00:52:59.8789180Z     response: {"confidence": 0.9275, "content_id": "d81bbc21-8ef4-4e9b-8a46-4978a1463dba", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-18T00:52:59.8794340Z     log entry: {"timestamp": "2026-11-18T00:52:18+00:00", "content_id": "d81bbc21-8ef4-4e9b-8a46-4978a1463dba", "creator_id": "cap-c-repeat", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 137.434}
2026-11-18T00:52:59.8798610Z     duration_ms 137.434 vs caller's wait 139.833: complete
2026-11-18T00:52:59.8799400Z   2 repeat 4: status 200, caller's wait 155.132 ms
2026-11-18T00:52:59.8801200Z     response: {"confidence": 0.9275, "content_id": "7822227c-4cc4-47a7-ad97-7e3a6772c052", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-18T00:52:59.8806310Z     log entry: {"timestamp": "2026-11-18T00:52:18+00:00", "content_id": "7822227c-4cc4-47a7-ad97-7e3a6772c052", "creator_id": "cap-c-repeat", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 152.48}
2026-11-18T00:52:59.8810510Z     duration_ms 152.48 vs caller's wait 155.132: complete
2026-11-18T00:52:59.8811310Z   2 repeat 5: status 200, caller's wait 167.16 ms
2026-11-18T00:52:59.8813060Z     response: {"confidence": 0.9275, "content_id": "1b16c108-3c92-4ff1-9de0-7718f69f54e1", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-18T00:52:59.8817970Z     log entry: {"timestamp": "2026-11-18T00:52:18+00:00", "content_id": "1b16c108-3c92-4ff1-9de0-7718f69f54e1", "creator_id": "cap-c-repeat", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 163.847}
2026-11-18T00:52:59.8822630Z     duration_ms 163.847 vs caller's wait 167.16: complete
2026-11-18T00:52:59.8823380Z   2 repeat 6: status 200, caller's wait 157.674 ms
2026-11-18T00:52:59.8825570Z     response: {"confidence": 0.9275, "content_id": "82318b99-863f-4c91-9088-4f4e52fb0a6b", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-18T00:52:59.8830620Z     log entry: {"timestamp": "2026-11-18T00:52:18+00:00", "content_id": "82318b99-863f-4c91-9088-4f4e52fb0a6b", "creator_id": "cap-c-repeat", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 154.822}
2026-11-18T00:52:59.8834540Z     duration_ms 154.822 vs caller's wait 157.674: complete
2026-11-18T00:52:59.8835210Z   2 repeat 7: status 200, caller's wait 141.319 ms
2026-11-18T00:52:59.8836760Z     response: {"confidence": 0.9275, "content_id": "eb85d077-7db2-4af5-953f-1b435bd308e6", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-18T00:52:59.8841270Z     log entry: {"timestamp": "2026-11-18T00:52:18+00:00", "content_id": "eb85d077-7db2-4af5-953f-1b435bd308e6", "creator_id": "cap-c-repeat", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 138.849}
2026-11-18T00:52:59.8844950Z     duration_ms 138.849 vs caller's wait 141.319: complete
2026-11-18T00:52:59.8845640Z   2 repeat 8: status 200, caller's wait 139.625 ms
2026-11-18T00:52:59.8847250Z     response: {"confidence": 0.9275, "content_id": "2739c740-410f-4ecb-861d-ee0c0a302260", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-18T00:52:59.8851730Z     log entry: {"timestamp": "2026-11-18T00:52:19+00:00", "content_id": "2739c740-410f-4ecb-861d-ee0c0a302260", "creator_id": "cap-c-repeat", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 137.313}
2026-11-18T00:52:59.8855680Z     duration_ms 137.313 vs caller's wait 139.625: complete
2026-11-18T00:52:59.8856380Z   2 repeat 9: status 200, caller's wait 143.103 ms
2026-11-18T00:52:59.8858040Z     response: {"confidence": 0.9275, "content_id": "99402d1b-db39-4ee0-a958-9c638ae854a5", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-18T00:52:59.8862490Z     log entry: {"timestamp": "2026-11-18T00:52:19+00:00", "content_id": "99402d1b-db39-4ee0-a958-9c638ae854a5", "creator_id": "cap-c-repeat", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 140.47}
2026-11-18T00:52:59.8866040Z     duration_ms 140.47 vs caller's wait 143.103: complete
2026-11-18T00:52:59.8866700Z   2 repeat 10: status 200, caller's wait 159.879 ms
2026-11-18T00:52:59.8868700Z     response: {"confidence": 0.9275, "content_id": "9a572b6b-7db2-4f92-81ea-7723de1afd0f", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-18T00:52:59.8873070Z     log entry: {"timestamp": "2026-11-18T00:52:19+00:00", "content_id": "9a572b6b-7db2-4f92-81ea-7723de1afd0f", "creator_id": "cap-c-repeat", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 157.071}
2026-11-18T00:52:59.8876810Z     duration_ms 157.071 vs caller's wait 159.879: complete
2026-11-18T00:52:59.8877480Z   2 repeat 11: status 200, caller's wait 149.323 ms
2026-11-18T00:52:59.8879170Z     response: {"confidence": 0.9275, "content_id": "91511d3e-e370-43b4-b88f-0a822a0403e5", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-18T00:52:59.8883290Z     log entry: {"timestamp": "2026-11-18T00:52:19+00:00", "content_id": "91511d3e-e370-43b4-b88f-0a822a0403e5", "creator_id": "cap-c-repeat", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 146.594}
2026-11-18T00:52:59.8886440Z     duration_ms 146.594 vs caller's wait 149.323: complete
2026-11-18T00:52:59.8887030Z   2 repeat 12: status 200, caller's wait 134.381 ms
2026-11-18T00:52:59.8888420Z     response: {"confidence": 0.9275, "content_id": "76d83a63-4a81-4104-b8e0-e755781656bc", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-18T00:52:59.8892390Z     log entry: {"timestamp": "2026-11-18T00:52:19+00:00", "content_id": "76d83a63-4a81-4104-b8e0-e755781656bc", "creator_id": "cap-c-repeat", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 132.024}
2026-11-18T00:52:59.8895550Z     duration_ms 132.024 vs caller's wait 134.381: complete
2026-11-18T00:52:59.8905950Z   2 repeat 13: status 429, caller's wait 2.091 ms
2026-11-18T00:52:59.8906940Z     response: {"error": "rate_limited", "limit": "12 per 1 minute", "message": "Too many submissions. Try again shortly."}
2026-11-18T00:52:59.8910180Z     log entry: {"timestamp": "2026-11-18T00:52:19+00:00", "content_id": null, "creator_id": "cap-c-repeat", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "rate_limited", "limit": "12 per 1 minute", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"reason": "rate_limited", "http_status": 429}, "duration_ms": 0.376}
2026-11-18T00:52:59.8913090Z     duration_ms 0.376 vs caller's wait 2.091: complete
2026-11-18T00:52:59.8913650Z   3 no text: status 422, caller's wait 1.803 ms
2026-11-18T00:52:59.8914400Z     response: {"error": "missing_field", "message": "Both text and creator_id are required."}
2026-11-18T00:52:59.8916940Z     log entry: {"timestamp": "2026-11-18T00:52:19+00:00", "content_id": null, "creator_id": "cap-c-missing", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "missing_field", "http_status": 422, "input": null, "output": {"reason": "missing_field", "http_status": 422}, "duration_ms": 0.006}
2026-11-18T00:52:59.8919810Z     duration_ms 0.006 vs caller's wait 1.803: complete
2026-11-18T00:52:59.8920370Z   4 appeal: status 200, caller's wait 2.667 ms
2026-11-18T00:52:59.8921580Z     response: {"content_id": "0daf2e11-0140-42f8-a869-c4bdc50f8467", "message": "Your appeal has been recorded next to the original decision.", "status": "under_review"}
2026-11-18T00:52:59.8925630Z     log entry: {"timestamp": "2026-11-18T00:52:19+00:00", "content_id": "0daf2e11-0140-42f8-a869-c4bdc50f8467", "creator_id": "cap-c-decision", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "under_review", "event": "appeal", "reasoning": "I wrote this myself.", "input": {"sha256": "da3ec48b7a7f8e0915fee0a032a004826bacd3e05c9a3916a301e9ffca7a7d1c", "words": 4}, "output": {"status": "under_review", "http_status": 200}, "duration_ms": 1.295}
2026-11-18T00:52:59.8928650Z     duration_ms 1.295 vs caller's wait 2.667: complete
2026-11-18T00:52:59.8929230Z   4 appeal again: status 409, caller's wait 2.232 ms
2026-11-18T00:52:59.8930130Z     response: {"error": "already_appealed", "message": "This decision has already been appealed."}
2026-11-18T00:52:59.8933100Z     log entry: {"timestamp": "2026-11-18T00:52:19+00:00", "content_id": null, "creator_id": "cap-c-decision", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "already_appealed", "http_status": 409, "input": {"sha256": "63b20b566dab38bcad7ce239b9e4e0193eff60470968281b0577391f7a809020", "words": 2}, "output": {"reason": "already_appealed", "http_status": 409}, "duration_ms": 0.988}
2026-11-18T00:52:59.8935810Z     duration_ms 0.988 vs caller's wait 2.232: complete
2026-11-18T00:52:59.8936340Z   4 made-up id: status 404, caller's wait 2.263 ms
2026-11-18T00:52:59.8937100Z     response: {"error": "unknown_content_id", "message": "No decision was found for that content_id."}
2026-11-18T00:52:59.8940080Z     log entry: {"timestamp": "2026-11-18T00:52:19+00:00", "content_id": null, "creator_id": "unknown", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "unknown_content_id", "http_status": 404, "input": {"sha256": "df91ca48d8fa30eecb786ffa4401e9a2bbc8a7ca2df52b8a452f2fcb61513070", "words": 4}, "output": {"reason": "unknown_content_id", "http_status": 404}, "duration_ms": 1.067}
2026-11-18T00:52:59.8942830Z     duration_ms 1.067 vs caller's wait 2.263: complete
2026-11-18T00:52:59.8943360Z   5 bad model: status 503, caller's wait 2060.141 ms
2026-11-18T00:52:59.8947300Z     response: {"error": "detector_could_not_load", "message": "Couldn't load 'no-such-model-capstone': no-such-model-capstone is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<your_token>`\nThe first run downloads about 550 MB — check your connection and that you have disk space free."}
2026-11-18T00:52:59.8956060Z     log entry: {"timestamp": "2026-11-18T00:52:58+00:00", "content_id": null, "creator_id": "cap-c-503", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "detector_could_not_load", "http_status": 503, "message": "Couldn't load 'no-such-model-capstone': no-such-model-capstone is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<your_token>`\nThe first run downloads about 550 MB — check your connection and that you have disk space free.", "model": "no-such-model-capstone", "error_type": "OSError", "failed_at": "model_load", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"reason": "detector_could_not_load", "http_status": 503}, "duration_ms": 2055.949}
2026-11-18T00:52:59.8960220Z     duration_ms 2055.949 vs caller's wait 2060.141: complete
2026-11-18T00:52:59.8960980Z   -> Capstone 3: PASS (19 of 19 complete)
2026-11-18T00:52:59.8961120Z 
2026-11-18T00:52:59.8961200Z == Capstone 2: the model can't load (cap-b) ==
2026-11-18T00:52:59.8961400Z   cause: torch
2026-11-18T00:53:37.2853370Z [cause torch] server up on port 5050 (pid 4370); /health answers
2026-11-18T00:53:38.3605700Z   cause torch: status 503, caller's wait 5.679 ms
2026-11-18T00:53:38.3607780Z     response: {"error": "detector_could_not_load", "message": "transformers or torch isn't installed (No module named 'torch').\nRun: pip install -r requirements.txt"}
2026-11-18T00:53:38.3614450Z     log entry: {"timestamp": "2026-11-18T00:53:37+00:00", "content_id": null, "creator_id": "cap-b", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "detector_could_not_load", "http_status": 503, "message": "transformers or torch isn't installed (No module named 'torch').\nRun: pip install -r requirements.txt", "model": "gpt2", "error_type": "ModuleNotFoundError", "failed_at": "model_load", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"reason": "detector_could_not_load", "http_status": 503}, "duration_ms": 0.646}
2026-11-18T00:53:38.3621650Z     checks: {"503": true, "JSON": true, "error": true, "message identical, not empty": true, "exactly one new line": true, "reason/http_status": true, "fields filled": true, "error_type exact": true, "names the module": true}  -> PASS
2026-11-18T00:53:46.9857840Z   cause: transformers
2026-11-18T00:54:22.9344940Z [cause transformers] server up on port 5050 (pid 5299); /health answers
2026-11-18T00:54:24.7238570Z   cause transformers: status 503, caller's wait 606.929 ms
2026-11-18T00:54:24.7242370Z     response: {"error": "detector_could_not_load", "message": "transformers or torch isn't installed (No module named 'transformers').\nRun: pip install -r requirements.txt"}
2026-11-18T00:54:24.7254640Z     log entry: {"timestamp": "2026-11-18T00:54:23+00:00", "content_id": null, "creator_id": "cap-b", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "detector_could_not_load", "http_status": 503, "message": "transformers or torch isn't installed (No module named 'transformers').\nRun: pip install -r requirements.txt", "model": "gpt2", "error_type": "ModuleNotFoundError", "failed_at": "model_load", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"reason": "detector_could_not_load", "http_status": 503}, "duration_ms": 602.089}
2026-11-18T00:54:24.7267710Z     checks: {"503": true, "JSON": true, "error": true, "message identical, not empty": true, "exactly one new line": true, "reason/http_status": true, "fields filled": true, "error_type exact": true, "names the module": true}  -> PASS
2026-11-18T00:54:29.9818170Z   cause: bad model name
2026-11-18T00:55:05.2878830Z [cause bad model name] server up on port 5050 (pid 6100); /health answers
2026-11-18T00:55:08.3932860Z   cause bad model name: status 503, caller's wait 2059.462 ms
2026-11-18T00:55:08.3942120Z     response: {"error": "detector_could_not_load", "message": "Couldn't load 'no-such-model-capstone': no-such-model-capstone is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<your_token>`\nThe first run downloads about 550 MB — check your connection and that you have disk space free."}
2026-11-18T00:55:08.3963130Z     log entry: {"timestamp": "2026-11-18T00:55:07+00:00", "content_id": null, "creator_id": "cap-b", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "detector_could_not_load", "http_status": 503, "message": "Couldn't load 'no-such-model-capstone': no-such-model-capstone is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<your_token>`\nThe first run downloads about 550 MB — check your connection and that you have disk space free.", "model": "no-such-model-capstone", "error_type": "OSError", "failed_at": "model_load", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"reason": "detector_could_not_load", "http_status": 503}, "duration_ms": 2054.835}
2026-11-18T00:55:08.3978690Z     checks: {"503": true, "JSON": true, "error": true, "message identical, not empty": true, "exactly one new line": true, "reason/http_status": true, "fields filled": true, "error_type exact": true, "names the module": true}  -> PASS
2026-11-18T00:55:08.3981420Z   -> Capstone 2: PASS (3 of 3 causes)
2026-11-18T00:55:08.3981880Z 
```

#### capstone (ubuntu-latest)
```text
﻿2026-11-18T00:51:12.8119089Z ##[group]Run if [ -f .venv/Scripts/activate ]; then source .venv/Scripts/activate; else source .venv/bin/activate; fi
2026-11-18T00:51:12.8119948Z ^[[36;1mif [ -f .venv/Scripts/activate ]; then source .venv/Scripts/activate; else source .venv/bin/activate; fi^[[0m
2026-11-18T00:51:12.8120478Z ^[[36;1mpython run_capstone.py run^[[0m
2026-11-18T00:51:12.8173663Z shell: /usr/bin/bash --noprofile --norc -e -o pipefail {0}
2026-11-18T00:51:12.8174023Z env:
2026-11-18T00:51:12.8174218Z   PYTHONUTF8: 1
2026-11-18T00:51:12.8174498Z   pythonLocation: /opt/hostedtoolcache/Python/3.12.16/x64
2026-11-18T00:51:12.8174936Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.12.16/x64/lib/pkgconfig
2026-11-18T00:51:12.8175363Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.16/x64
2026-11-18T00:51:12.8175772Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.16/x64
2026-11-18T00:51:12.8176177Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.16/x64
2026-11-18T00:51:12.8176589Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.12.16/x64/lib
2026-11-18T00:51:12.8176973Z ##[endgroup]
2026-11-18T00:51:12.9134710Z Capstone run on Linux (Python 3.12.16), commit b6298c3, run 44211042368
2026-11-18T00:51:13.4829500Z [start #1] server up on port 5050 (pid 2725); /health answers
2026-11-18T00:51:13.4829831Z 
2026-11-18T00:51:13.4829945Z == Capstone 1: first start (cap-a) ==
2026-11-18T00:51:17.7083851Z   attempt 1: status 200, caller's wait 4221.1 ms
2026-11-18T00:51:17.7085322Z     response: {"confidence": 0.9275, "content_id": "cc53634b-5b2f-4715-9f44-d8f8f29d5b7f", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-18T00:51:17.7088507Z     log entry: {"timestamp": "2026-11-18T00:51:17+00:00", "content_id": "cc53634b-5b2f-4715-9f44-d8f8f29d5b7f", "creator_id": "cap-a", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 4217.549, "cold": true}
2026-11-18T00:51:17.7091307Z   -> Capstone 1 on this machine: PASS (attempts used: 1; caller's span 4221.206 ms)
2026-11-18T00:51:17.7092122Z 
2026-11-18T00:51:17.7092504Z == Capstone 4: cost and speed (cap-d) ==
2026-11-18T00:51:17.7093702Z   cold (caller's clock, Capstone 1 attempt 1 start -> passing attempt end): 4221.206 ms
2026-11-18T00:51:18.1124477Z   warm 1 (attempts 1): status 200, caller's wait 400.393 ms
2026-11-18T00:51:18.1126066Z     response: {"confidence": 0.9275, "content_id": "c9fc2907-8d85-4f54-ab01-6431161e7e14", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-18T00:51:18.1130378Z     log entry: {"timestamp": "2026-11-18T00:51:18+00:00", "content_id": "c9fc2907-8d85-4f54-ab01-6431161e7e14", "creator_id": "cap-d", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 397.306}
2026-11-18T00:51:18.5178960Z   warm 2 (attempts 1): status 200, caller's wait 401.814 ms
2026-11-18T00:51:18.5180803Z     response: {"confidence": 0.9275, "content_id": "8bb1b27b-c437-407c-a3b9-ff0603c97608", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-18T00:51:18.5185251Z     log entry: {"timestamp": "2026-11-18T00:51:18+00:00", "content_id": "8bb1b27b-c437-407c-a3b9-ff0603c97608", "creator_id": "cap-d", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 398.662}
2026-11-18T00:51:18.9254171Z   warm 3 (attempts 1): status 200, caller's wait 403.286 ms
2026-11-18T00:51:18.9255327Z     response: {"confidence": 0.9275, "content_id": "ffbbe6de-7e6a-4cf8-ab0f-d3fe5a99b7cf", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-18T00:51:18.9257475Z     log entry: {"timestamp": "2026-11-18T00:51:18+00:00", "content_id": "ffbbe6de-7e6a-4cf8-ab0f-d3fe5a99b7cf", "creator_id": "cap-d", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 400.129}
2026-11-18T00:51:18.9377679Z   memory right after the third warm answer: 1058.898 MB (psutil memory_info().rss of pid 2725, 1 MB = 1,000,000 bytes)
2026-11-18T00:51:18.9379081Z   -> Capstone 4 on this machine: FAIL (cold 4221.206 ms vs 45000; warm at most 5000 ms: 3 of 3; memory 1058.898 MB vs 900)
2026-11-18T00:51:18.9379857Z 
2026-11-18T00:51:18.9380141Z == Capstone 5: the old behaviour and the boundary (cap-e) ==
2026-11-18T00:51:19.3391589Z   #1 valid /submit: status 200, caller's wait 401.206 ms
2026-11-18T00:51:19.3393635Z     response: {"confidence": 0.9275, "content_id": "6274c38a-889e-4317-8a0b-6e12fa3ac0c2", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-18T00:51:19.3423145Z   #2 not JSON: status 400, caller's wait 3.067 ms
2026-11-18T00:51:19.3424061Z     response: {"error": "invalid_json", "message": "The request body must be JSON."}
2026-11-18T00:51:19.3445197Z   #3 no text field: status 422, caller's wait 2.13 ms
2026-11-18T00:51:19.3445781Z     response: {"error": "missing_field", "message": "Both text and creator_id are required."}
2026-11-18T00:51:19.3465765Z   #4 empty text: status 400, caller's wait 1.932 ms
2026-11-18T00:51:19.3466467Z     response: {"error": "empty_text", "message": "The text is empty."}
2026-11-18T00:51:19.3486310Z   #5 punctuation only: status 400, caller's wait 1.935 ms
2026-11-18T00:51:19.3487076Z     response: {"error": "no_words", "message": "The text has no words to score."}
2026-11-18T00:51:19.3508706Z   #6 492 words: status 413, caller's wait 2.119 ms
2026-11-18T00:51:19.3509676Z     response: {"error": "text_too_long", "message": "The text is too long to score. Please send at most 350 words."}
2026-11-18T00:51:19.3533892Z   #7 Hi.: status 400, caller's wait 2.365 ms
2026-11-18T00:51:19.3534698Z     response: {"error": "text_too_short", "message": "The text is too short to score. Please send at least a few sentences."}
2026-11-18T00:51:19.3575931Z   #8 appeal: status 200, caller's wait 4.08 ms
2026-11-18T00:51:19.3577358Z     response: {"content_id": "6274c38a-889e-4317-8a0b-6e12fa3ac0c2", "message": "Your appeal has been recorded next to the original decision.", "status": "under_review"}
2026-11-18T00:51:19.3612427Z   #9 appeal again: status 409, caller's wait 3.519 ms
2026-11-18T00:51:19.3613351Z     response: {"error": "already_appealed", "message": "This decision has already been appealed."}
2026-11-18T00:51:19.3650852Z   #10 made-up id: status 404, caller's wait 3.692 ms
2026-11-18T00:51:19.3651830Z     response: {"error": "unknown_content_id", "message": "No decision was found for that content_id."}
2026-11-18T00:51:19.3686314Z   #11 GET /health: {"detector_loaded": true, "detector_model": "gpt2", "log_entries": 407, "ok": true, "rate_limiting": true}
2026-11-18T00:51:22.4736237Z   #12 python test.py: '9 passed, 0 failed, 0 to look at, 0 skipped'
2026-11-18T00:51:22.5864702Z [2026-11-18 00:51:22,584] ERROR in app: Exception on /submit [POST]
2026-11-18T00:51:22.5865363Z Traceback (most recent call last):
2026-11-18T00:51:22.5873356Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 1511, in wsgi_app
2026-11-18T00:51:22.5874608Z     response = self.full_dispatch_request()
2026-11-18T00:51:22.5874988Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:22.5876274Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 919, in full_dispatch_request
2026-11-18T00:51:22.5877515Z     rv = self.handle_user_exception(e)
2026-11-18T00:51:22.5877854Z          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:22.5879062Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 917, in full_dispatch_request
2026-11-18T00:51:22.5880251Z     rv = self.dispatch_request()
2026-11-18T00:51:22.5880504Z          ^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:22.5881331Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 902, in dispatch_request
2026-11-18T00:51:22.5882377Z     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
2026-11-18T00:51:22.5883015Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:22.5883941Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask_limiter/extension.py", line 1314, in __inner
2026-11-18T00:51:22.5884879Z     return cast(R, flask.current_app.ensure_sync(obj)(*a, **k))
2026-11-18T00:51:22.5885230Z                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:22.5885922Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/app.py", line 305, in submit
2026-11-18T00:51:22.5886650Z     model_score = detector.model_signal(text)
2026-11-18T00:51:22.5886928Z                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:22.5887400Z   File "/opt/hostedtoolcache/Python/3.12.16/x64/lib/python3.12/unittest/mock.py", line 1139, in __call__
2026-11-18T00:51:22.5887889Z     return self._mock_call(*args, **kwargs)
2026-11-18T00:51:22.5888164Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:22.5888638Z   File "/opt/hostedtoolcache/Python/3.12.16/x64/lib/python3.12/unittest/mock.py", line 1143, in _mock_call
2026-11-18T00:51:22.5889433Z     return self._execute_mock_call(*args, **kwargs)
2026-11-18T00:51:22.5889738Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:22.5890279Z   File "/opt/hostedtoolcache/Python/3.12.16/x64/lib/python3.12/unittest/mock.py", line 1198, in _execute_mock_call
2026-11-18T00:51:22.5890777Z     raise effect
2026-11-18T00:51:22.5891004Z RuntimeError: capstone boundary check (a)
2026-11-18T00:51:22.5892286Z   (a) RuntimeError in detector.model_signal (while GPT-2 scores the text): status 500, JSON body: False, new log lines: 0 (lines 407 -> 407)
2026-11-18T00:51:26.7713865Z `loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.
2026-11-18T00:51:26.7903664Z [2026-11-18 00:51:26,789] ERROR in app: Exception on /submit [POST]
2026-11-18T00:51:26.7904542Z Traceback (most recent call last):
2026-11-18T00:51:26.7915464Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 1511, in wsgi_app
2026-11-18T00:51:26.7923856Z     response = self.full_dispatch_request()
2026-11-18T00:51:26.7924390Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:26.7925621Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 919, in full_dispatch_request
2026-11-18T00:51:26.7926951Z     rv = self.handle_user_exception(e)
2026-11-18T00:51:26.7927234Z          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:26.7928206Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 917, in full_dispatch_request
2026-11-18T00:51:26.7929224Z     rv = self.dispatch_request()
2026-11-18T00:51:26.7929504Z          ^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:26.7930484Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 902, in dispatch_request
2026-11-18T00:51:26.7931733Z     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
2026-11-18T00:51:26.7932323Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:26.7933717Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask_limiter/extension.py", line 1314, in __inner
2026-11-18T00:51:26.7934830Z     return cast(R, flask.current_app.ensure_sync(obj)(*a, **k))
2026-11-18T00:51:26.7935231Z                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:26.7936066Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/app.py", line 326, in submit
2026-11-18T00:51:26.7936951Z     combined_score = scoring.combine_signals(model_score, style_score)
2026-11-18T00:51:26.7937397Z                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:26.7937987Z   File "/opt/hostedtoolcache/Python/3.12.16/x64/lib/python3.12/unittest/mock.py", line 1139, in __call__
2026-11-18T00:51:26.7938568Z     return self._mock_call(*args, **kwargs)
2026-11-18T00:51:26.7938882Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:26.7939404Z   File "/opt/hostedtoolcache/Python/3.12.16/x64/lib/python3.12/unittest/mock.py", line 1143, in _mock_call
2026-11-18T00:51:26.7939932Z     return self._execute_mock_call(*args, **kwargs)
2026-11-18T00:51:26.7940231Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:26.7940769Z   File "/opt/hostedtoolcache/Python/3.12.16/x64/lib/python3.12/unittest/mock.py", line 1198, in _execute_mock_call
2026-11-18T00:51:26.7941284Z     raise effect
2026-11-18T00:51:26.7941507Z RuntimeError: capstone boundary check (b)
2026-11-18T00:51:26.7954985Z   (b) RuntimeError in scoring.combine_signals (while combining and labelling): status 500, JSON body: False, new log lines: 0 (lines 407 -> 407)
2026-11-18T00:51:27.2040315Z [2026-11-18 00:51:27,203] ERROR in app: Exception on /submit [POST]
2026-11-18T00:51:27.2041041Z Traceback (most recent call last):
2026-11-18T00:51:27.2042679Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 1511, in wsgi_app
2026-11-18T00:51:27.2044477Z     response = self.full_dispatch_request()
2026-11-18T00:51:27.2044967Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:27.2046610Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 919, in full_dispatch_request
2026-11-18T00:51:27.2048242Z     rv = self.handle_user_exception(e)
2026-11-18T00:51:27.2048708Z          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:27.2050309Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 917, in full_dispatch_request
2026-11-18T00:51:27.2051928Z     rv = self.dispatch_request()
2026-11-18T00:51:27.2052844Z          ^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:27.2054652Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask/app.py", line 902, in dispatch_request
2026-11-18T00:51:27.2056705Z     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
2026-11-18T00:51:27.2057649Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:27.2059498Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/.venv/lib/python3.12/site-packages/flask_limiter/extension.py", line 1314, in __inner
2026-11-18T00:51:27.2061299Z     return cast(R, flask.current_app.ensure_sync(obj)(*a, **k))
2026-11-18T00:51:27.2061961Z                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:27.2063456Z   File "/home/runner/work/ai201-project4-provenance-guard-starter-v2026/ai201-project4-provenance-guard-starter-v2026/app.py", line 342, in submit
2026-11-18T00:51:27.2064761Z     audit.log_decision(
2026-11-18T00:51:27.2065590Z   File "/opt/hostedtoolcache/Python/3.12.16/x64/lib/python3.12/unittest/mock.py", line 1139, in __call__
2026-11-18T00:51:27.2066509Z     return self._mock_call(*args, **kwargs)
2026-11-18T00:51:27.2066997Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:27.2067889Z   File "/opt/hostedtoolcache/Python/3.12.16/x64/lib/python3.12/unittest/mock.py", line 1143, in _mock_call
2026-11-18T00:51:27.2068830Z     return self._execute_mock_call(*args, **kwargs)
2026-11-18T00:51:27.2069369Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:51:27.2070325Z   File "/opt/hostedtoolcache/Python/3.12.16/x64/lib/python3.12/unittest/mock.py", line 1198, in _execute_mock_call
2026-11-18T00:51:27.2071099Z     raise effect
2026-11-18T00:51:27.2071446Z RuntimeError: capstone boundary check (c)
2026-11-18T00:51:27.2078525Z   (c) RuntimeError in audit.log_decision (while writing the log): status 500, JSON body: False, new log lines: 0 (lines 407 -> 407)
2026-11-18T00:51:27.2079831Z   -> Capstone 5 on this machine: PASS (13 of the 13 required; 15 of 15 overall; #11 True, #12 True)
2026-11-18T00:51:28.2437464Z 
```

#### capstone (windows-latest)
```text
﻿2026-11-18T00:51:58.6820529Z ##[group]Run if [ -f .venv/Scripts/activate ]; then source .venv/Scripts/activate; else source .venv/bin/activate; fi
2026-11-18T00:51:58.6821423Z ^[[36;1mif [ -f .venv/Scripts/activate ]; then source .venv/Scripts/activate; else source .venv/bin/activate; fi^[[0m
2026-11-18T00:51:58.6821931Z ^[[36;1mpython run_capstone.py run^[[0m
2026-11-18T00:51:58.6839738Z shell: C:\Program Files\Git\bin\bash.EXE --noprofile --norc -e -o pipefail {0}
2026-11-18T00:51:58.6840176Z env:
2026-11-18T00:51:58.6840363Z   PYTHONUTF8: 1
2026-11-18T00:51:58.6840639Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-18T00:51:58.6841103Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
2026-11-18T00:51:58.6841560Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-18T00:51:58.6841957Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-18T00:51:58.6842351Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-18T00:51:58.6842704Z ##[endgroup]
2026-11-18T00:51:58.9656152Z Capstone run on Windows (Python 3.12.10), commit b6298c3, run 44211042368
2026-11-18T00:51:59.5977314Z [start #1] server up on port 5050 (pid 9196); /health answers
2026-11-18T00:51:59.5977783Z 
2026-11-18T00:51:59.5977935Z == Capstone 1: first start (cap-a) ==
2026-11-18T00:52:05.1799430Z   attempt 1: status 200, caller's wait 5578.721 ms
2026-11-18T00:52:05.1800767Z     response: {"confidence": 0.9275, "content_id": "c16024b1-0c25-4c9d-b774-c67f7407b88b", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-18T00:52:05.1804158Z     log entry: {"timestamp": "2026-11-18T00:52:05+00:00", "content_id": "c16024b1-0c25-4c9d-b774-c67f7407b88b", "creator_id": "cap-a", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 5548.707, "cold": true}
2026-11-18T00:52:05.1807038Z   -> Capstone 1 on this machine: PASS (attempts used: 1; caller's span 5578.825 ms)
2026-11-18T00:52:05.1807502Z 
2026-11-18T00:52:05.1807692Z == Capstone 4: cost and speed (cap-d) ==
2026-11-18T00:52:05.1808317Z   cold (caller's clock, Capstone 1 attempt 1 start -> passing attempt end): 5578.825 ms
2026-11-18T00:52:05.6637731Z   warm 1 (attempts 1): status 200, caller's wait 480.706 ms
2026-11-18T00:52:05.6638850Z     response: {"confidence": 0.9275, "content_id": "088e6aa1-5628-472e-b96e-327ad203cb4f", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-18T00:52:05.6641168Z     log entry: {"timestamp": "2026-11-18T00:52:05+00:00", "content_id": "088e6aa1-5628-472e-b96e-327ad203cb4f", "creator_id": "cap-d", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 476.509}
2026-11-18T00:52:06.1026478Z   warm 2 (attempts 1): status 200, caller's wait 436.018 ms
2026-11-18T00:52:06.1028021Z     response: {"confidence": 0.9275, "content_id": "b015a2d7-5c20-471a-866a-801ae2a7824f", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-18T00:52:06.1031940Z     log entry: {"timestamp": "2026-11-18T00:52:06+00:00", "content_id": "b015a2d7-5c20-471a-866a-801ae2a7824f", "creator_id": "cap-d", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 421.835}
2026-11-18T00:52:06.5547200Z   warm 3 (attempts 1): status 200, caller's wait 449.041 ms
2026-11-18T00:52:06.5548838Z     response: {"confidence": 0.9275, "content_id": "032adc4f-9289-4044-98de-9efb3af13cd6", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-18T00:52:06.5552743Z     log entry: {"timestamp": "2026-11-18T00:52:06+00:00", "content_id": "032adc4f-9289-4044-98de-9efb3af13cd6", "creator_id": "cap-d", "guess": "ai", "model_score": 0.8551, "style_score": 1.0, "combined_score": 0.9275, "label": "This is starting to be similar to AI text.", "status": "decided", "input": {"sha256": "8e8f070f04dcac106ea105a3031298632f108fc0bffab45ac1adb7ec5fd72eb5", "words": 164}, "output": {"guess": "ai", "label": "This is starting to be similar to AI text."}, "duration_ms": 433.615}
2026-11-18T00:52:06.5686305Z   memory right after the third warm answer: 1083.04 MB (psutil memory_info().rss of pid 8368, 1 MB = 1,000,000 bytes)
2026-11-18T00:52:06.5687598Z   -> Capstone 4 on this machine: FAIL (cold 5578.825 ms vs 45000; warm at most 5000 ms: 3 of 3; memory 1083.04 MB vs 900)
2026-11-18T00:52:06.5688017Z 
2026-11-18T00:52:06.5688181Z == Capstone 5: the old behaviour and the boundary (cap-e) ==
2026-11-18T00:52:07.0397756Z   #1 valid /submit: status 200, caller's wait 470.953 ms
2026-11-18T00:52:07.0399218Z     response: {"confidence": 0.9275, "content_id": "4c74746e-17ba-4c47-b932-1d41e6b95256", "guess": "ai", "label": "This is starting to be similar to AI text.", "model_score": 0.8551, "style_score": 1.0}
2026-11-18T00:52:07.0626484Z   #2 not JSON: status 400, caller's wait 22.747 ms
2026-11-18T00:52:07.0627589Z     response: {"error": "invalid_json", "message": "The request body must be JSON."}
2026-11-18T00:52:07.0780709Z   #3 no text field: status 422, caller's wait 15.325 ms
2026-11-18T00:52:07.0782127Z     response: {"error": "missing_field", "message": "Both text and creator_id are required."}
2026-11-18T00:52:07.0812091Z   #4 empty text: status 400, caller's wait 3.024 ms
2026-11-18T00:52:07.0812750Z     response: {"error": "empty_text", "message": "The text is empty."}
2026-11-18T00:52:07.0843924Z   #5 punctuation only: status 400, caller's wait 3.017 ms
2026-11-18T00:52:07.0844778Z     response: {"error": "no_words", "message": "The text has no words to score."}
2026-11-18T00:52:07.1108593Z   #6 492 words: status 413, caller's wait 26.297 ms
2026-11-18T00:52:07.1110080Z     response: {"error": "text_too_long", "message": "The text is too long to score. Please send at most 350 words."}
2026-11-18T00:52:07.1265405Z   #7 Hi.: status 400, caller's wait 15.511 ms
2026-11-18T00:52:07.1266729Z     response: {"error": "text_too_short", "message": "The text is too short to score. Please send at least a few sentences."}
2026-11-18T00:52:07.1322472Z   #8 appeal: status 200, caller's wait 5.63 ms
2026-11-18T00:52:07.1323921Z     response: {"content_id": "4c74746e-17ba-4c47-b932-1d41e6b95256", "message": "Your appeal has been recorded next to the original decision.", "status": "under_review"}
2026-11-18T00:52:07.1594737Z   #9 appeal again: status 409, caller's wait 27.016 ms
2026-11-18T00:52:07.1596193Z     response: {"error": "already_appealed", "message": "This decision has already been appealed."}
2026-11-18T00:52:07.1664491Z   #10 made-up id: status 404, caller's wait 6.873 ms
2026-11-18T00:52:07.1665338Z     response: {"error": "unknown_content_id", "message": "No decision was found for that content_id."}
2026-11-18T00:52:07.1711957Z   #11 GET /health: {"detector_loaded": true, "detector_model": "gpt2", "log_entries": 407, "ok": true, "rate_limiting": true}
2026-11-18T00:52:10.9681824Z   #12 python test.py: '9 passed, 0 failed, 0 to look at, 0 skipped'
2026-11-18T00:52:11.1200963Z [2026-11-18 00:52:11,117] ERROR in app: Exception on /submit [POST]
2026-11-18T00:52:11.1203218Z Traceback (most recent call last):
2026-11-18T00:52:11.1209940Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
2026-11-18T00:52:11.1211033Z     response = self.full_dispatch_request()
2026-11-18T00:52:11.1211344Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:52:11.1212300Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
2026-11-18T00:52:11.1213216Z     rv = self.handle_user_exception(e)
2026-11-18T00:52:11.1213485Z          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:52:11.1214365Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
2026-11-18T00:52:11.1215268Z     rv = self.dispatch_request()
2026-11-18T00:52:11.1215526Z          ^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:52:11.1216374Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
2026-11-18T00:52:11.1218678Z     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
2026-11-18T00:52:11.1219252Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:52:11.1220233Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask_limiter\extension.py", line 1314, in __inner
2026-11-18T00:52:11.1221444Z     return cast(R, flask.current_app.ensure_sync(obj)(*a, **k))
2026-11-18T00:52:11.1221793Z                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:52:11.1222449Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\app.py", line 305, in submit
2026-11-18T00:52:11.1223100Z     model_score = detector.model_signal(text)
2026-11-18T00:52:11.1223367Z                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:52:11.1223827Z   File "C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\unittest\mock.py", line 1139, in __call__
2026-11-18T00:52:11.1224289Z     return self._mock_call(*args, **kwargs)
2026-11-18T00:52:11.1224544Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:52:11.1224981Z   File "C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\unittest\mock.py", line 1143, in _mock_call
2026-11-18T00:52:11.1225455Z     return self._execute_mock_call(*args, **kwargs)
2026-11-18T00:52:11.1225738Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:52:11.1226231Z   File "C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\unittest\mock.py", line 1198, in _execute_mock_call
2026-11-18T00:52:11.1226695Z     raise effect
2026-11-18T00:52:11.1226905Z RuntimeError: capstone boundary check (a)
2026-11-18T00:52:11.1232132Z   (a) RuntimeError in detector.model_signal (while GPT-2 scores the text): status 500, JSON body: False, new log lines: 0 (lines 407 -> 407)
2026-11-18T00:52:16.5733621Z `loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.
2026-11-18T00:52:16.5914177Z [2026-11-18 00:52:16,588] ERROR in app: Exception on /submit [POST]
2026-11-18T00:52:16.5914817Z Traceback (most recent call last):
2026-11-18T00:52:16.5915811Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
2026-11-18T00:52:16.5916591Z     response = self.full_dispatch_request()
2026-11-18T00:52:16.5916878Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:52:16.5918303Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
2026-11-18T00:52:16.5920140Z     rv = self.handle_user_exception(e)
2026-11-18T00:52:16.5920544Z          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:52:16.5921939Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
2026-11-18T00:52:16.5923392Z     rv = self.dispatch_request()
2026-11-18T00:52:16.5923798Z          ^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:52:16.5925459Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
2026-11-18T00:52:16.5927265Z     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
2026-11-18T00:52:16.5928189Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:52:16.5929753Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask_limiter\extension.py", line 1314, in __inner
2026-11-18T00:52:16.5931676Z     return cast(R, flask.current_app.ensure_sync(obj)(*a, **k))
2026-11-18T00:52:16.5932281Z                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:52:16.5933472Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\app.py", line 326, in submit
2026-11-18T00:52:16.5934821Z     combined_score = scoring.combine_signals(model_score, style_score)
2026-11-18T00:52:16.5935473Z                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:52:16.5936337Z   File "C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\unittest\mock.py", line 1139, in __call__
2026-11-18T00:52:16.5937128Z     return self._mock_call(*args, **kwargs)
2026-11-18T00:52:16.5937581Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:52:16.5938399Z   File "C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\unittest\mock.py", line 1143, in _mock_call
2026-11-18T00:52:16.5959542Z     return self._execute_mock_call(*args, **kwargs)
2026-11-18T00:52:16.5960117Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:52:16.5961044Z   File "C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\unittest\mock.py", line 1198, in _execute_mock_call
2026-11-18T00:52:16.5961890Z     raise effect
2026-11-18T00:52:16.5962248Z RuntimeError: capstone boundary check (b)
2026-11-18T00:52:16.5963282Z   (b) RuntimeError in scoring.combine_signals (while combining and labelling): status 500, JSON body: False, new log lines: 0 (lines 407 -> 407)
2026-11-18T00:52:17.0212449Z [2026-11-18 00:52:17,019] ERROR in app: Exception on /submit [POST]
2026-11-18T00:52:17.0212902Z Traceback (most recent call last):
2026-11-18T00:52:17.0213766Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
2026-11-18T00:52:17.0214574Z     response = self.full_dispatch_request()
2026-11-18T00:52:17.0214852Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:52:17.0215685Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
2026-11-18T00:52:17.0216491Z     rv = self.handle_user_exception(e)
2026-11-18T00:52:17.0216958Z          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:52:17.0218306Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
2026-11-18T00:52:17.0219643Z     rv = self.dispatch_request()
2026-11-18T00:52:17.0220019Z          ^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:52:17.0221262Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
2026-11-18T00:52:17.0222889Z     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
2026-11-18T00:52:17.0223416Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:52:17.0224936Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\.venv\Lib\site-packages\flask_limiter\extension.py", line 1314, in __inner
2026-11-18T00:52:17.0226532Z     return cast(R, flask.current_app.ensure_sync(obj)(*a, **k))
2026-11-18T00:52:17.0227185Z                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:52:17.0227912Z   File "D:\a\ai201-project4-provenance-guard-starter-v2026\ai201-project4-provenance-guard-starter-v2026\app.py", line 342, in submit
2026-11-18T00:52:17.0228541Z     audit.log_decision(
2026-11-18T00:52:17.0228968Z   File "C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\unittest\mock.py", line 1139, in __call__
2026-11-18T00:52:17.0229743Z     return self._mock_call(*args, **kwargs)
2026-11-18T00:52:17.0230214Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:52:17.0231404Z   File "C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\unittest\mock.py", line 1143, in _mock_call
2026-11-18T00:52:17.0232305Z     return self._execute_mock_call(*args, **kwargs)
2026-11-18T00:52:17.0232836Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-18T00:52:17.0233429Z   File "C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\unittest\mock.py", line 1198, in _execute_mock_call
2026-11-18T00:52:17.0233902Z     raise effect
2026-11-18T00:52:17.0234115Z RuntimeError: capstone boundary check (c)
2026-11-18T00:52:17.0257296Z   (c) RuntimeError in audit.log_decision (while writing the log): status 500, JSON body: False, new log lines: 0 (lines 407 -> 407)
2026-11-18T00:52:17.0258676Z   -> Capstone 5 on this machine: PASS (13 of the 13 required; 15 of 15 overall; #11 True, #12 True)
2026-11-18T00:52:18.0327936Z 
```

## Machine-readable results, all three runs

The last line of each machine's output (`CAPSTONE-RESULT`), per run.

### Run 44211042368
#### Darwin (Python 3.12.10)
```json
{
 "machine": "Darwin",
 "python": "3.12.10",
 "commit": "b6298c3a934e17972417e814d84f6476c6a7ab92",
 "run_id": "44211042368",
 "started": "2026-11-18T00:50:54+00:00",
 "c1": {
  "pass": true,
  "attempts": 1,
  "cold_span_ms": 2501.677,
  "content_id": "e5f29a6a-ad46-4cab-b186-ade3d8ada61f",
  "evidence": [
   {
    "status": 200,
    "json": {
     "confidence": 0.9275,
     "content_id": "e5f29a6a-ad46-4cab-b186-ade3d8ada61f",
     "guess": "ai",
     "label": "This is starting to be similar to AI text.",
     "model_score": 0.8551,
     "style_score": 1.0
    },
    "wait_ms": 2501.618,
    "problem": null,
    "body_start": null,
    "attempt": 1,
    "entry": {
     "timestamp": "2026-11-18T00:51:32+00:00",
     "content_id": "e5f29a6a-ad46-4cab-b186-ade3d8ada61f",
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
     "duration_ms": 2496.942,
     "cold": true
    }
   }
  ]
 },
 "c4": {
  "pass": false,
  "cold_ms": 2501.677,
  "warm": [
   {
    "status": 200,
    "duration_ms": 147.711,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 147.538,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 146.704,
    "attempts": 1
   }
  ],
  "warm_under": 3,
  "memory_mb": 1052.541,
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
    "wait_ms": 2779.392,
    "duration_ms": 2776.807,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 1",
    "status": 200,
    "wait_ms": 169.209,
    "duration_ms": 166.142,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 2",
    "status": 200,
    "wait_ms": 147.707,
    "duration_ms": 145.438,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 3",
    "status": 200,
    "wait_ms": 139.833,
    "duration_ms": 137.434,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 4",
    "status": 200,
    "wait_ms": 155.132,
    "duration_ms": 152.48,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 5",
    "status": 200,
    "wait_ms": 167.16,
    "duration_ms": 163.847,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 6",
    "status": 200,
    "wait_ms": 157.674,
    "duration_ms": 154.822,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 7",
    "status": 200,
    "wait_ms": 141.319,
    "duration_ms": 138.849,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 8",
    "status": 200,
    "wait_ms": 139.625,
    "duration_ms": 137.313,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 9",
    "status": 200,
    "wait_ms": 143.103,
    "duration_ms": 140.47,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 10",
    "status": 200,
    "wait_ms": 159.879,
    "duration_ms": 157.071,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 11",
    "status": 200,
    "wait_ms": 149.323,
    "duration_ms": 146.594,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 12",
    "status": 200,
    "wait_ms": 134.381,
    "duration_ms": 132.024,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 13",
    "status": 429,
    "wait_ms": 2.091,
    "duration_ms": 0.376,
    "complete": true,
    "problems": []
   },
   {
    "label": "3 no text",
    "status": 422,
    "wait_ms": 1.803,
    "duration_ms": 0.006,
    "complete": true,
    "problems": []
   },
   {
    "label": "4 appeal",
    "status": 200,
    "wait_ms": 2.667,
    "duration_ms": 1.295,
    "complete": true,
    "problems": []
   },
   {
    "label": "4 appeal again",
    "status": 409,
    "wait_ms": 2.232,
    "duration_ms": 0.988,
    "complete": true,
    "problems": []
   },
   {
    "label": "4 made-up id",
    "status": 404,
    "wait_ms": 2.263,
    "duration_ms": 1.067,
    "complete": true,
    "problems": []
   },
   {
    "label": "5 bad model",
    "status": 503,
    "wait_ms": 2060.141,
    "duration_ms": 2055.949,
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
 "commit": "b6298c3a934e17972417e814d84f6476c6a7ab92",
 "run_id": "44211042368",
 "started": "2026-11-18T00:51:12+00:00",
 "c1": {
  "pass": true,
  "attempts": 1,
  "cold_span_ms": 4221.206,
  "content_id": "cc53634b-5b2f-4715-9f44-d8f8f29d5b7f",
  "evidence": [
   {
    "status": 200,
    "json": {
     "confidence": 0.9275,
     "content_id": "cc53634b-5b2f-4715-9f44-d8f8f29d5b7f",
     "guess": "ai",
     "label": "This is starting to be similar to AI text.",
     "model_score": 0.8551,
     "style_score": 1.0
    },
    "wait_ms": 4221.1,
    "problem": null,
    "body_start": null,
    "attempt": 1,
    "entry": {
     "timestamp": "2026-11-18T00:51:17+00:00",
     "content_id": "cc53634b-5b2f-4715-9f44-d8f8f29d5b7f",
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
     "duration_ms": 4217.549,
     "cold": true
    }
   }
  ]
 },
 "c4": {
  "pass": false,
  "cold_ms": 4221.206,
  "warm": [
   {
    "status": 200,
    "duration_ms": 397.306,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 398.662,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 400.129,
    "attempts": 1
   }
  ],
  "warm_under": 3,
  "memory_mb": 1058.898,
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
 "commit": "b6298c3a934e17972417e814d84f6476c6a7ab92",
 "run_id": "44211042368",
 "started": "2026-11-18T00:51:58+00:00",
 "c1": {
  "pass": true,
  "attempts": 1,
  "cold_span_ms": 5578.825,
  "content_id": "c16024b1-0c25-4c9d-b774-c67f7407b88b",
  "evidence": [
   {
    "status": 200,
    "json": {
     "confidence": 0.9275,
     "content_id": "c16024b1-0c25-4c9d-b774-c67f7407b88b",
     "guess": "ai",
     "label": "This is starting to be similar to AI text.",
     "model_score": 0.8551,
     "style_score": 1.0
    },
    "wait_ms": 5578.721,
    "problem": null,
    "body_start": null,
    "attempt": 1,
    "entry": {
     "timestamp": "2026-11-18T00:52:05+00:00",
     "content_id": "c16024b1-0c25-4c9d-b774-c67f7407b88b",
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
     "duration_ms": 5548.707,
     "cold": true
    }
   }
  ]
 },
 "c4": {
  "pass": false,
  "cold_ms": 5578.825,
  "warm": [
   {
    "status": 200,
    "duration_ms": 476.509,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 421.835,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 433.615,
    "attempts": 1
   }
  ],
  "warm_under": 3,
  "memory_mb": 1083.04,
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

### Run 44211062395
#### Darwin (Python 3.12.10)
```json
{
 "machine": "Darwin",
 "python": "3.12.10",
 "commit": "b6298c3a934e17972417e814d84f6476c6a7ab92",
 "run_id": "44211062395",
 "started": "2026-11-18T00:51:34+00:00",
 "c1": {
  "pass": true,
  "attempts": 1,
  "cold_span_ms": 10141.761,
  "content_id": "0fdf803d-605d-42b0-83b8-cbb7a45c9d01",
  "evidence": [
   {
    "status": 200,
    "json": {
     "confidence": 0.9275,
     "content_id": "0fdf803d-605d-42b0-83b8-cbb7a45c9d01",
     "guess": "ai",
     "label": "This is starting to be similar to AI text.",
     "model_score": 0.8551,
     "style_score": 1.0
    },
    "wait_ms": 10141.191,
    "problem": null,
    "body_start": null,
    "attempt": 1,
    "entry": {
     "timestamp": "2026-11-18T00:52:20+00:00",
     "content_id": "0fdf803d-605d-42b0-83b8-cbb7a45c9d01",
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
     "duration_ms": 10119.626,
     "cold": true
    }
   }
  ]
 },
 "c4": {
  "pass": false,
  "cold_ms": 10141.761,
  "warm": [
   {
    "status": 200,
    "duration_ms": 356.996,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 209.044,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 169.629,
    "attempts": 1
   }
  ],
  "warm_under": 3,
  "memory_mb": 1032.159,
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
    "wait_ms": 11312.143,
    "duration_ms": 11289.849,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 1",
    "status": 200,
    "wait_ms": 416.525,
    "duration_ms": 378.397,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 2",
    "status": 200,
    "wait_ms": 383.1,
    "duration_ms": 375.818,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 3",
    "status": 200,
    "wait_ms": 416.684,
    "duration_ms": 408.247,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 4",
    "status": 200,
    "wait_ms": 342.233,
    "duration_ms": 335.423,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 5",
    "status": 200,
    "wait_ms": 393.182,
    "duration_ms": 390.306,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 6",
    "status": 200,
    "wait_ms": 368.84,
    "duration_ms": 364.304,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 7",
    "status": 200,
    "wait_ms": 327.395,
    "duration_ms": 321.487,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 8",
    "status": 200,
    "wait_ms": 402.553,
    "duration_ms": 396.827,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 9",
    "status": 200,
    "wait_ms": 446.277,
    "duration_ms": 437.054,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 10",
    "status": 200,
    "wait_ms": 317.134,
    "duration_ms": 308.206,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 11",
    "status": 200,
    "wait_ms": 347.478,
    "duration_ms": 332.946,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 12",
    "status": 200,
    "wait_ms": 357.017,
    "duration_ms": 344.632,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 13",
    "status": 429,
    "wait_ms": 10.861,
    "duration_ms": 1.47,
    "complete": true,
    "problems": []
   },
   {
    "label": "3 no text",
    "status": 422,
    "wait_ms": 4.499,
    "duration_ms": 0.043,
    "complete": true,
    "problems": []
   },
   {
    "label": "4 appeal",
    "status": 200,
    "wait_ms": 8.07,
    "duration_ms": 2.0,
    "complete": true,
    "problems": []
   },
   {
    "label": "4 appeal again",
    "status": 409,
    "wait_ms": 3.879,
    "duration_ms": 1.461,
    "complete": true,
    "problems": []
   },
   {
    "label": "4 made-up id",
    "status": 404,
    "wait_ms": 9.308,
    "duration_ms": 6.001,
    "complete": true,
    "problems": []
   },
   {
    "label": "5 bad model",
    "status": 503,
    "wait_ms": 3049.333,
    "duration_ms": 3045.169,
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
 "commit": "b6298c3a934e17972417e814d84f6476c6a7ab92",
 "run_id": "44211062395",
 "started": "2026-11-18T00:51:17+00:00",
 "c1": {
  "pass": true,
  "attempts": 1,
  "cold_span_ms": 4033.887,
  "content_id": "715edb64-611b-47bd-aa8d-4096ccdf2323",
  "evidence": [
   {
    "status": 200,
    "json": {
     "confidence": 0.9275,
     "content_id": "715edb64-611b-47bd-aa8d-4096ccdf2323",
     "guess": "ai",
     "label": "This is starting to be similar to AI text.",
     "model_score": 0.8551,
     "style_score": 1.0
    },
    "wait_ms": 4033.784,
    "problem": null,
    "body_start": null,
    "attempt": 1,
    "entry": {
     "timestamp": "2026-11-18T00:51:21+00:00",
     "content_id": "715edb64-611b-47bd-aa8d-4096ccdf2323",
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
     "duration_ms": 4030.782,
     "cold": true
    }
   }
  ]
 },
 "c4": {
  "pass": false,
  "cold_ms": 4033.887,
  "warm": [
   {
    "status": 200,
    "duration_ms": 385.352,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 383.282,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 380.288,
    "attempts": 1
   }
  ],
  "warm_under": 3,
  "memory_mb": 1058.611,
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
 "commit": "b6298c3a934e17972417e814d84f6476c6a7ab92",
 "run_id": "44211062395",
 "started": "2026-11-18T00:51:49+00:00",
 "c1": {
  "pass": true,
  "attempts": 1,
  "cold_span_ms": 6014.263,
  "content_id": "9dc76379-9bda-4d88-b799-e6a36656d187",
  "evidence": [
   {
    "status": 200,
    "json": {
     "confidence": 0.9275,
     "content_id": "9dc76379-9bda-4d88-b799-e6a36656d187",
     "guess": "ai",
     "label": "This is starting to be similar to AI text.",
     "model_score": 0.8551,
     "style_score": 1.0
    },
    "wait_ms": 6014.157,
    "problem": null,
    "body_start": null,
    "attempt": 1,
    "entry": {
     "timestamp": "2026-11-18T00:51:56+00:00",
     "content_id": "9dc76379-9bda-4d88-b799-e6a36656d187",
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
     "duration_ms": 5986.626,
     "cold": true
    }
   }
  ]
 },
 "c4": {
  "pass": false,
  "cold_ms": 6014.263,
  "warm": [
   {
    "status": 200,
    "duration_ms": 463.633,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 468.465,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 448.19,
    "attempts": 1
   }
  ],
  "warm_under": 3,
  "memory_mb": 1045.291,
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

### Run 44211083234
#### Darwin (Python 3.12.10)
```json
{
 "machine": "Darwin",
 "python": "3.12.10",
 "commit": "b6298c3a934e17972417e814d84f6476c6a7ab92",
 "run_id": "44211083234",
 "started": "2026-11-18T00:51:42+00:00",
 "c1": {
  "pass": true,
  "attempts": 1,
  "cold_span_ms": 6553.556,
  "content_id": "7c0b0065-1269-4bbf-855f-920536c6dacf",
  "evidence": [
   {
    "status": 200,
    "json": {
     "confidence": 0.9275,
     "content_id": "7c0b0065-1269-4bbf-855f-920536c6dacf",
     "guess": "ai",
     "label": "This is starting to be similar to AI text.",
     "model_score": 0.8551,
     "style_score": 1.0
    },
    "wait_ms": 6553.164,
    "problem": null,
    "body_start": null,
    "attempt": 1,
    "entry": {
     "timestamp": "2026-11-18T00:52:24+00:00",
     "content_id": "7c0b0065-1269-4bbf-855f-920536c6dacf",
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
     "duration_ms": 6542.251,
     "cold": true
    }
   }
  ]
 },
 "c4": {
  "pass": false,
  "cold_ms": 6553.556,
  "warm": [
   {
    "status": 200,
    "duration_ms": 188.018,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 155.445,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 141.996,
    "attempts": 1
   }
  ],
  "warm_under": 3,
  "memory_mb": 1024.147,
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
    "wait_ms": 8088.743,
    "duration_ms": 8068.221,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 1",
    "status": 200,
    "wait_ms": 283.113,
    "duration_ms": 276.737,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 2",
    "status": 200,
    "wait_ms": 257.051,
    "duration_ms": 252.974,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 3",
    "status": 200,
    "wait_ms": 301.947,
    "duration_ms": 296.584,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 4",
    "status": 200,
    "wait_ms": 298.235,
    "duration_ms": 293.402,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 5",
    "status": 200,
    "wait_ms": 231.687,
    "duration_ms": 227.349,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 6",
    "status": 200,
    "wait_ms": 264.215,
    "duration_ms": 260.488,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 7",
    "status": 200,
    "wait_ms": 289.244,
    "duration_ms": 284.525,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 8",
    "status": 200,
    "wait_ms": 232.263,
    "duration_ms": 228.719,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 9",
    "status": 200,
    "wait_ms": 236.193,
    "duration_ms": 232.928,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 10",
    "status": 200,
    "wait_ms": 239.89,
    "duration_ms": 237.004,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 11",
    "status": 200,
    "wait_ms": 243.819,
    "duration_ms": 237.205,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 12",
    "status": 200,
    "wait_ms": 333.272,
    "duration_ms": 329.393,
    "complete": true,
    "problems": []
   },
   {
    "label": "2 repeat 13",
    "status": 429,
    "wait_ms": 5.36,
    "duration_ms": 1.04,
    "complete": true,
    "problems": []
   },
   {
    "label": "3 no text",
    "status": 422,
    "wait_ms": 2.958,
    "duration_ms": 0.012,
    "complete": true,
    "problems": []
   },
   {
    "label": "4 appeal",
    "status": 200,
    "wait_ms": 5.532,
    "duration_ms": 2.931,
    "complete": true,
    "problems": []
   },
   {
    "label": "4 appeal again",
    "status": 409,
    "wait_ms": 5.948,
    "duration_ms": 2.52,
    "complete": true,
    "problems": []
   },
   {
    "label": "4 made-up id",
    "status": 404,
    "wait_ms": 4.457,
    "duration_ms": 1.725,
    "complete": true,
    "problems": []
   },
   {
    "label": "5 bad model",
    "status": 503,
    "wait_ms": 3186.803,
    "duration_ms": 3183.04,
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
 "commit": "b6298c3a934e17972417e814d84f6476c6a7ab92",
 "run_id": "44211083234",
 "started": "2026-11-18T00:51:28+00:00",
 "c1": {
  "pass": true,
  "attempts": 1,
  "cold_span_ms": 4410.67,
  "content_id": "c89ad698-ec11-423a-b372-489d85c357d0",
  "evidence": [
   {
    "status": 200,
    "json": {
     "confidence": 0.9275,
     "content_id": "c89ad698-ec11-423a-b372-489d85c357d0",
     "guess": "ai",
     "label": "This is starting to be similar to AI text.",
     "model_score": 0.8551,
     "style_score": 1.0
    },
    "wait_ms": 4410.585,
    "problem": null,
    "body_start": null,
    "attempt": 1,
    "entry": {
     "timestamp": "2026-11-18T00:51:33+00:00",
     "content_id": "c89ad698-ec11-423a-b372-489d85c357d0",
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
     "duration_ms": 4407.152,
     "cold": true
    }
   }
  ]
 },
 "c4": {
  "pass": false,
  "cold_ms": 4410.67,
  "warm": [
   {
    "status": 200,
    "duration_ms": 239.451,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 232.417,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 235.598,
    "attempts": 1
   }
  ],
  "warm_under": 3,
  "memory_mb": 1042.186,
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
 "commit": "b6298c3a934e17972417e814d84f6476c6a7ab92",
 "run_id": "44211083234",
 "started": "2026-11-18T00:51:36+00:00",
 "c1": {
  "pass": true,
  "attempts": 1,
  "cold_span_ms": 3687.478,
  "content_id": "6c00fb8d-e185-4452-b7e0-7fc65da27628",
  "evidence": [
   {
    "status": 200,
    "json": {
     "confidence": 0.9275,
     "content_id": "6c00fb8d-e185-4452-b7e0-7fc65da27628",
     "guess": "ai",
     "label": "This is starting to be similar to AI text.",
     "model_score": 0.8551,
     "style_score": 1.0
    },
    "wait_ms": 3687.386,
    "problem": null,
    "body_start": null,
    "attempt": 1,
    "entry": {
     "timestamp": "2026-11-18T00:51:40+00:00",
     "content_id": "6c00fb8d-e185-4452-b7e0-7fc65da27628",
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
     "duration_ms": 3672.895,
     "cold": true
    }
   }
  ]
 },
 "c4": {
  "pass": false,
  "cold_ms": 3687.478,
  "warm": [
   {
    "status": 200,
    "duration_ms": 379.648,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 371.628,
    "attempts": 1
   },
   {
    "status": 200,
    "duration_ms": 333.205,
    "attempts": 1
   }
  ],
  "warm_under": 3,
  "memory_mb": 1082.397,
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

