# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-08 02:32
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `b66b32de-fda6-495f-9889-8498cccef43c` | unsure | 0.500 | HELD |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `456c118c-4c4a-4406-9c35-545250c95173` | unsure | 0.622 | HELD |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `24404469-a875-4293-ac0a-4f23d5c1b6b8` | ai | 0.749 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `6e3c734a-c836-45d2-88fc-cdc02ff714ef` | ai | 0.806 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `e459a3a7-85fb-48ee-a124-9c9a7f96a070` | unsure | 0.500 | HELD |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `c9e1bbbc-a37d-4710-be6c-d450d2a492c8` | unsure | 0.562 | HELD |
| EV07 | evasion | signal two: padding with punctuation | 200 | `76d18719-8892-461c-b329-e9b92642ed44` | unsure | 0.543 | HELD |
| EV08 | evasion | signal one: text below the token window | 200 | `ce08b925-4f30-4503-8369-ce324d0c31b3` | unsure | 0.500 | HELD |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `3a8279c4-e236-49a2-ad13-d8219822e868` | ai | 0.754 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `6597cec8-c166-4f4d-a829-beff2b07f814` | unsure | 0.500 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `2d367115-8c3f-4b4b-9590-e78951703caa` | unsure | 0.614 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `670a56eb-0f62-43d4-b771-8d372beb5917` | unsure | 0.620 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `c3021566-897b-46fe-8514-94e881647310` | ai | 0.777 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `68869adb-8517-472f-9c5d-57fe9d81ef78` | ai | 0.802 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `2a852077-1022-44a8-936e-38b446c69a36` | unsure | 0.500 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `65ed8cae-1102-4186-ba24-35d4b76cb2a0` | unsure | 0.500 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `30804a29-111a-495d-bfb0-ca66860fab4b` | unsure | 0.500 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `1fbd72c4-ce41-4b8f-8ebc-28e5f6db40ba` | unsure | 0.500 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `cecfe664-8ba2-4f33-a345-2454544bd67b` | unsure | 0.500 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `dbbcb8bd-04a6-4503-9878-616e77355483` | unsure | 0.500 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `520e6087-99ea-4b36-bd4f-142760935efb` | ai | 0.772 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `7f434955-d80b-481d-9f6b-96ad89437772` | unsure | 0.500 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `49a7fff4-0bce-49cf-9a52-10345b302c75` | ai | 0.720 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `24d9b970-d685-44fb-86e7-e9a7a3ce3e89` | unsure | 0.629 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `5bb9d97f-340e-47b1-819b-0c5a5bba2aac` | human | 0.250 | BROKE |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — | HELD |
| MF05 | malformed | text is a very long single word | 200 | `0876cde3-6b4e-4ef6-a4a2-bc28e79653a9` | ai | 0.749 | BROKE |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — | HELD |
| MF07 | malformed | text is right-to-left script | 400 | `—` | — | — | HELD |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 422 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 422 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 422 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 422 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 422 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 422 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 422 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3eb517e4-9b02-4dd9-9e2f-33feb9875d1c` | human | 0.264 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `13920892-b55f-41ac-bc17-e29a1b73088c` | human | 0.264 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `486fe674-1b6c-4696-95e0-97def7424c22` | human | 0.264 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `923834b7-ce16-4d31-9bd9-4bf1f0ce097f` | human | 0.264 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7a3ad3fc-0ca0-4532-ba9b-60878a02d330` | human | 0.264 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `dcb1decf-3ba0-4f27-bc6b-9d48d732b966` | human | 0.264 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `79bad29d-6dae-4cf6-85d1-a20e43e1e460` | human | 0.264 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `953f7a22-d0d8-49d3-bb6e-29d20bfd2f5f` | human | 0.264 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `fc9b39ab-2ee0-4bfc-b722-e889e67a93b4` | human | 0.264 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e941bcd0-267d-4d3f-97a9-85a20a65fd70` | human | 0.264 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 200 | `053a4449-f7e4-4401-a51b-2ff951d11c44` | human | 0.264 | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 200 | `25031039-c2ec-4ed5-91d9-60e3ecf290a3` | human | 0.264 | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "b66b32de-fda6-495f-9889-8498cccef43c",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.1635,
  "style_score": 1.0,
  "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: towards human. How much sentence lengths vary and how many different words are used: towards AI.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "456c118c-4c4a-4406-9c35-545250c95173",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.6221,
  "model_score": 0.5943,
  "style_score": 0.65,
  "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: in the middle. How much sentence lengths vary and how many different words are used: towards AI.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "24404469-a875-4293-ac0a-4f23d5c1b6b8",
  "creator_id": "attacker_EV03",
  "guess": "ai",
  "confidence": 0.7494,
  "model_score": 0.6662,
  "style_score": 0.8327,
  "label": "This is starting to be similar to AI text.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "6e3c734a-c836-45d2-88fc-cdc02ff714ef",
  "creator_id": "attacker_EV04",
  "guess": "ai",
  "confidence": 0.8057,
  "model_score": 0.6114,
  "style_score": 1.0,
  "label": "This is starting to be similar to AI text.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "e459a3a7-85fb-48ee-a124-9c9a7f96a070",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.3212,
  "style_score": 0.65,
  "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: towards human. How much sentence lengths vary and how many different words are used: towards AI.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "c9e1bbbc-a37d-4710-be6c-d450d2a492c8",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.5625,
  "model_score": 0.5727,
  "style_score": 0.5523,
  "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: in the middle. How much sentence lengths vary and how many different words are used: in the middle.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "76d18719-8892-461c-b329-e9b92642ed44",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5431,
  "model_score": 0.5862,
  "style_score": 0.5,
  "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: in the middle. How much sentence lengths vary and how many different words are used: in the middle. Text should be longer and have multiple sentences.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "ce08b925-4f30-4503-8369-ce324d0c31b3",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.2452,
  "style_score": 1.0,
  "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: towards human. How much sentence lengths vary and how many different words are used: towards AI.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "3a8279c4-e236-49a2-ad13-d8219822e868",
  "creator_id": "attacker_EV09",
  "guess": "ai",
  "confidence": 0.7544,
  "model_score": 0.7042,
  "style_score": 0.8045,
  "label": "This is starting to be similar to AI text.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "6597cec8-c166-4f4d-a829-beff2b07f814",
  "creator_id": "attacker_EV10",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.9792,
  "style_score": 0.2404,
  "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: towards AI. How much sentence lengths vary and how many different words are used: towards human.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "2d367115-8c3f-4b4b-9590-e78951703caa",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.6143,
  "model_score": 0.6175,
  "style_score": 0.6112,
  "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: towards AI. How much sentence lengths vary and how many different words are used: towards AI.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "670a56eb-0f62-43d4-b771-8d372beb5917",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.62,
  "model_score": 0.7387,
  "style_score": 0.5014,
  "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: towards AI. How much sentence lengths vary and how many different words are used: in the middle.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "c3021566-897b-46fe-8514-94e881647310",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7767,
  "model_score": 0.8051,
  "style_score": 0.7483,
  "label": "This is starting to be similar to AI text.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "68869adb-8517-472f-9c5d-57fe9d81ef78",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.8024,
  "model_score": 0.8329,
  "style_score": 0.772,
  "label": "This is starting to be similar to AI text.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "2a852077-1022-44a8-936e-38b446c69a36",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.8005,
  "style_score": 0.35,
  "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: towards AI. How much sentence lengths vary and how many different words are used: towards human.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "65ed8cae-1102-4186-ba24-35d4b76cb2a0",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.8814,
  "style_score": 0.1463,
  "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: towards AI. How much sentence lengths vary and how many different words are used: towards human.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "30804a29-111a-495d-bfb0-ca66860fab4b",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.8816,
  "style_score": 0.0,
  "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: towards AI. How much sentence lengths vary and how many different words are used: towards human.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "1fbd72c4-ce41-4b8f-8ebc-28e5f6db40ba",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.3223,
  "style_score": 0.8448,
  "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: towards human. How much sentence lengths vary and how many different words are used: towards AI.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "cecfe664-8ba2-4f33-a345-2454544bd67b",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.4625,
  "style_score": 0.65,
  "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: in the middle. How much sentence lengths vary and how many different words are used: towards AI.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "dbbcb8bd-04a6-4503-9878-616e77355483",
  "creator_id": "attacker_PI02",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.2044,
  "style_score": 0.65,
  "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: towards human. How much sentence lengths vary and how many different words are used: towards AI.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "520e6087-99ea-4b36-bd4f-142760935efb",
  "creator_id": "attacker_PI03",
  "guess": "ai",
  "confidence": 0.7721,
  "model_score": 0.5943,
  "style_score": 0.9498,
  "label": "This is starting to be similar to AI text.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "7f434955-d80b-481d-9f6b-96ad89437772",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.4998,
  "style_score": 0.8872,
  "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: in the middle. How much sentence lengths vary and how many different words are used: towards AI.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "49a7fff4-0bce-49cf-9a52-10345b302c75",
  "creator_id": "attacker_PI05",
  "guess": "ai",
  "confidence": 0.7201,
  "model_score": 0.6401,
  "style_score": 0.8,
  "label": "This is starting to be similar to AI text.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "24d9b970-d685-44fb-86e7-e9a7a3ce3e89",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.6289,
  "model_score": 0.5583,
  "style_score": 0.6994,
  "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: in the middle. How much sentence lengths vary and how many different words are used: towards AI.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "5bb9d97f-340e-47b1-819b-0c5a5bba2aac",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.25,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "This looks similar to human text.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "0876cde3-6b4e-4ef6-a4a2-bc28e79653a9",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.7488,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "This is starting to be similar to AI text.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF07",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 422,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 422,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "3eb517e4-9b02-4dd9-9e2f-33feb9875d1c",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This looks similar to human text.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "13920892-b55f-41ac-bc17-e29a1b73088c",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This looks similar to human text.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "486fe674-1b6c-4696-95e0-97def7424c22",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This looks similar to human text.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "923834b7-ce16-4d31-9bd9-4bf1f0ce097f",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This looks similar to human text.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "7a3ad3fc-0ca0-4532-ba9b-60878a02d330",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This looks similar to human text.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "dcb1decf-3ba0-4f27-bc6b-9d48d732b966",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This looks similar to human text.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "79bad29d-6dae-4cf6-85d1-a20e43e1e460",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This looks similar to human text.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "953f7a22-d0d8-49d3-bb6e-29d20bfd2f5f",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This looks similar to human text.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "fc9b39ab-2ee0-4bfc-b722-e889e67a93b4",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This looks similar to human text.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "e941bcd0-267d-4d3f-97a9-85a20a65fd70",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This looks similar to human text.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 200,
  "content_id": "053a4449-f7e4-4401-a51b-2ff951d11c44",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This looks similar to human text.",
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 200,
  "content_id": "25031039-c2ec-4ed5-91d9-60e3ecf290a3",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This looks similar to human text.",
  "error": null,
  "verdict": ""
}
```
