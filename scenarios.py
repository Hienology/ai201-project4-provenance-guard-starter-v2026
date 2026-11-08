"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

from pathlib import Path

_SAMPLES = Path(__file__).parent / "samples"


def _read(name: str) -> str:
    return (_SAMPLES / name).read_text(encoding="utf-8")


# The inputs criteria.md names: 5 AI texts and the 5 texts I wrote, in samples/.
AI_TEXTS = [_read(f"ai-{i}.txt") for i in range(1, 6)]
MY_TEXTS = [_read(f"human-own-{i}.txt") for i in range(1, 6)]

# Each name's first 12 characters differ, so each criterion gets its own
# creator_ids (run_eval.py builds them from the name).
SCENARIOS = [
    {
        "name": "c1 score spread",
        "criterion": 1,
        # Read: model_score. Pass: AI average − my average ≥ 0.3, every trial.
        "texts": AI_TEXTS + MY_TEXTS,
    },
    {
        "name": "c2 false positives",
        "criterion": 2,
        # Read: guess. Flagged = ai or unsure. Pass: at most 2 of 5, every trial.
        "texts": MY_TEXTS,
    },
    {
        "name": "c5 label coverage",
        "criterion": 5,
        # Read: guess. Pass: ≥ 3 of the 5 AI get ai, ≥ 1 of 10 unsure,
        # ≥ 2 of 10 human, every trial.
        "texts": AI_TEXTS + MY_TEXTS,
    },
    # Criteria 3 and 4 are run by hand, three times each, not from here:
    #   3 (bad input): `bash samples/bad_input.sh`. One of its five requests is
    #     not JSON, which run_eval.py can't send, and run_eval.py doesn't record
    #     the `error` field the criterion reads.
    #   4 (appeal path): `bash samples/appeal_check.sh`. It needs a submission,
    #     then appeals against the content_id that came back, then GET /log.
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
