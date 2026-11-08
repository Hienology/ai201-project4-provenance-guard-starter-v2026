# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-08 16:57
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `0af8faf9-3f0d-4e4a-a230-5d3c96814784` | unsure | 0.500 | HELD |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `37502c3a-9675-42a7-b651-0e44c4deefa9` | unsure | 0.622 | HELD |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `5b7cfd5f-d08a-4a64-9649-6a47e4a5e519` | unsure | 0.749 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `f3fb7fb8-9784-43ec-84a8-8a2421f93ed4` | unsure | 0.806 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `56778843-37a1-40a0-8818-a507ff6bd881` | unsure | 0.500 | HELD |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `cc467237-da16-4fa7-b1aa-79459d91d232` | unsure | 0.562 | HELD |
| EV07 | evasion | signal two: padding with punctuation | 200 | `c354acec-0511-41f2-952e-5387fa3e4ca6` | unsure | 0.543 | HELD |
| EV08 | evasion | signal one: text below the token window | 200 | `6b3510d4-ef91-4e1a-8630-30566273260b` | unsure | 0.500 | HELD |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `d4b3660b-3a57-4a04-920d-b602a77fdb8d` | unsure | 0.754 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `b42543f0-a534-4c48-b383-84231089f72f` | unsure | 0.500 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `b64b6892-ecb6-4f43-8a13-364607acb9e5` | unsure | 0.614 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `64a056d6-d8a9-4253-b3b5-b604df96a05c` | unsure | 0.620 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `4e7e7dda-3652-461a-85af-1a60edaf51b8` | unsure | 0.777 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `b9c990c7-132d-43cb-828a-2bc4895312c1` | unsure | 0.802 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `059415a3-f269-4653-b063-619773cfc952` | unsure | 0.500 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `46fa4b2b-233b-40a1-a536-63f4f48aecca` | unsure | 0.500 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `88d82c36-5fe0-4f5e-bcc5-17b71500edee` | unsure | 0.500 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `edc50e79-ba6b-4ff1-8855-3d2cb46033f6` | unsure | 0.500 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `0f1d510a-c008-42f5-83cc-12626932ce9f` | unsure | 0.500 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `1a279c9b-3d84-43df-9d2e-38a773f51d07` | unsure | 0.500 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `d7a33824-83b5-47da-852b-5b74838553b6` | unsure | 0.772 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `7dd22069-6e7f-4843-93cc-4da83df5a687` | unsure | 0.500 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `bee624de-edb6-43ce-bc2f-3ba7ba032da9` | unsure | 0.720 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `377e3ac4-4df6-493a-900c-f052ae2edda3` | unsure | 0.629 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `e6eadc43-e6e6-4724-bcf1-af34832f6694` | human | 0.250 | BROKE |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — | HELD |
| MF05 | malformed | text is a very long single word | 200 | `9b2c4f5e-a783-43e1-9e7a-efedd89e4ea7` | unsure | 0.749 | HELD |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1b6b252d-528a-4aa1-8005-a169347c593d` | human | 0.264 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `fab420a2-4431-4491-bd72-03e6d0c55f78` | human | 0.264 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `23c0d597-d359-4b40-a8b0-138747cbb5ae` | human | 0.264 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `15cc7c9c-e1ff-4161-908c-6bb6b15c233f` | human | 0.264 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e55b1f17-7790-4d88-83bd-bb78bae416a3` | human | 0.264 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `35e24754-548e-4121-879e-fd5a7f568d79` | human | 0.264 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c184fc43-f3de-487c-84fb-153d1981522d` | human | 0.264 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `449edee3-193f-4e23-8403-d11a8b53f726` | human | 0.264 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6dc8fb1d-8b41-4a31-997e-d5ecfbf82078` | human | 0.264 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d7ae672a-0c60-4950-bd42-b6d52e28af3e` | human | 0.264 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a030f745-5e5d-4e4a-9ceb-a7549d2f3a48` | human | 0.264 | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7b4f1097-6a9b-44e4-834d-65721a847e28` | human | 0.264 | HELD |

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
  "content_id": "0af8faf9-3f0d-4e4a-a230-5d3c96814784",
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
  "content_id": "37502c3a-9675-42a7-b651-0e44c4deefa9",
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
  "content_id": "5b7cfd5f-d08a-4a64-9649-6a47e4a5e519",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.7494,
  "model_score": 0.6662,
  "style_score": 0.8327,
  "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: towards AI. How much sentence lengths vary and how many different words are used: towards AI.",
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
  "content_id": "f3fb7fb8-9784-43ec-84a8-8a2421f93ed4",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.8057,
  "model_score": 0.6114,
  "style_score": 1.0,
  "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: towards AI. How much sentence lengths vary and how many different words are used: towards AI.",
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
  "content_id": "56778843-37a1-40a0-8818-a507ff6bd881",
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
  "content_id": "cc467237-da16-4fa7-b1aa-79459d91d232",
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
  "content_id": "c354acec-0511-41f2-952e-5387fa3e4ca6",
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
  "content_id": "6b3510d4-ef91-4e1a-8630-30566273260b",
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
  "content_id": "d4b3660b-3a57-4a04-920d-b602a77fdb8d",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.7544,
  "model_score": 0.7042,
  "style_score": 0.8045,
  "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: towards AI. How much sentence lengths vary and how many different words are used: towards AI.",
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
  "content_id": "b42543f0-a534-4c48-b383-84231089f72f",
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
  "content_id": "b64b6892-ecb6-4f43-8a13-364607acb9e5",
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
  "content_id": "64a056d6-d8a9-4253-b3b5-b604df96a05c",
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
  "content_id": "4e7e7dda-3652-461a-85af-1a60edaf51b8",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.7767,
  "model_score": 0.8051,
  "style_score": 0.7483,
  "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: towards AI. How much sentence lengths vary and how many different words are used: towards AI.",
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
  "content_id": "b9c990c7-132d-43cb-828a-2bc4895312c1",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.8024,
  "model_score": 0.8329,
  "style_score": 0.772,
  "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: towards AI. How much sentence lengths vary and how many different words are used: towards AI.",
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
  "content_id": "059415a3-f269-4653-b063-619773cfc952",
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
  "content_id": "46fa4b2b-233b-40a1-a536-63f4f48aecca",
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
  "content_id": "88d82c36-5fe0-4f5e-bcc5-17b71500edee",
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
  "content_id": "edc50e79-ba6b-4ff1-8855-3d2cb46033f6",
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
  "content_id": "0f1d510a-c008-42f5-83cc-12626932ce9f",
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
  "content_id": "1a279c9b-3d84-43df-9d2e-38a773f51d07",
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
  "content_id": "d7a33824-83b5-47da-852b-5b74838553b6",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.7721,
  "model_score": 0.5943,
  "style_score": 0.9498,
  "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: in the middle. How much sentence lengths vary and how many different words are used: towards AI.",
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
  "content_id": "7dd22069-6e7f-4843-93cc-4da83df5a687",
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
  "content_id": "bee624de-edb6-43ce-bc2f-3ba7ba032da9",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.7201,
  "model_score": 0.6401,
  "style_score": 0.8,
  "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: towards AI. How much sentence lengths vary and how many different words are used: towards AI.",
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
  "content_id": "377e3ac4-4df6-493a-900c-f052ae2edda3",
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
  "content_id": "e6eadc43-e6e6-4724-bcf1-af34832f6694",
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
  "content_id": "9b2c4f5e-a783-43e1-9e7a-efedd89e4ea7",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.7488,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: towards AI. How much sentence lengths vary and how many different words are used: in the middle. Text should be longer and have multiple sentences.",
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
  "content_id": "1b6b252d-528a-4aa1-8005-a169347c593d",
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
  "content_id": "fab420a2-4431-4491-bd72-03e6d0c55f78",
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
  "content_id": "23c0d597-d359-4b40-a8b0-138747cbb5ae",
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
  "content_id": "15cc7c9c-e1ff-4161-908c-6bb6b15c233f",
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
  "content_id": "e55b1f17-7790-4d88-83bd-bb78bae416a3",
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
  "content_id": "35e24754-548e-4121-879e-fd5a7f568d79",
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
  "content_id": "c184fc43-f3de-487c-84fb-153d1981522d",
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
  "content_id": "449edee3-193f-4e23-8403-d11a8b53f726",
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
  "content_id": "6dc8fb1d-8b41-4a31-997e-d5ecfbf82078",
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
  "content_id": "d7ae672a-0c60-4950-bd42-b6d52e28af3e",
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
  "content_id": "a030f745-5e5d-4e4a-9ceb-a7549d2f3a48",
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
  "content_id": "7b4f1097-6a9b-44e4-834d-65721a847e28",
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
