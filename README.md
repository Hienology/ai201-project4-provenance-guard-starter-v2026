# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

A backend a writing site could plug into: text comes in at `POST /submit`, two separate signals score it, and the writer gets back a guess, a score, a sentence they can read, and a `content_id` they can appeal with at `POST /appeal`. Every decision, appeal and refused request is written to `logs/audit.jsonl`.

> **Finished at the start of Unit 8, before any Unit 8 run:** the three labels, `/appeal`, the thresholds in `config.py`, `guess` and `label` in the response and the log, and logging of refused requests. My Unit 7 submission did not have them yet.

The path (my Milestone 1 trace, `notes/m1-trace.md`; the parts marked *Unit 8* were added then):

1. A POST request arrives at `/submit` and the JSON body is read → adds `text` and `creator_id`. *Unit 8: the rate limiter counts it first, per `creator_id`; over 12 a minute or 1000 a day → 429, logged as `rate_limited`.*
2. Check it (validation) → adds a request that is safe to score. If it fails: a short error (400 / 413 / 422) and no `content_id`. *Unit 8: the refusal is logged as `rejected`.*
3. Signal one: pass the text to the model (`detector.model_signal(text)`) → adds `model_score`, from 0 to 1. If it fails after validation passed (fewer than 3 tokens): no id, and the error says the text is too short to score.
4. Signal two: stylometry on the same text (`stylometry.style_signal(text)`) → adds `style_score`, from 0 to 1.
5. Combine both scores (`scoring.combine_signals(...)`) → adds the third number, the combined score, sent as `confidence` (0 = human-like, 1 = AI-like).
6. Create the `content_id`, only now, so only real decisions get ids → adds `content_id`.
7. Turn the combined score into words (`scoring.score_to_label(...)`) → adds `guess` (`ai`, `human` or `unsure`) and `label`, the sentence the writer reads.
8. Write one log entry (`audit.log_decision(...)`), before the response, because code after `return` never runs → one line in `logs/audit.jsonl` with all nine fields; `status` is `decided`. The text itself is not stored.
9. Return the response → the writer gets `content_id`, `guess`, `confidence`, `label`, `model_score`, `style_score`.

An appeal (`POST /appeal` with the `content_id` and the writer's reasoning) adds a new log line after the decision with `status: under_review`. It does not change the score or the label, re-check the work, or notify anyone.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** which word comes and how expected it is, meaning the surprise is low or high (expected or not). The average surprise of all those words is the perplexity. The one doing the expecting is a model (GPT-2). Low surprise, aka expected/predictable, is guessable as AI: a low overall average means more likely AI. Higher perplexity → human-ish → low score; lower perplexity → low overall average → more likely AI → high score.

In the code (`detector.py::model_signal`): score = 1 / (1 + (perplexity / 45) ^ 1.6), so perplexity 45 scores 0.5. The starter's midpoint (45) and steepness (1.6) are unchanged.

**Why that might differ between human and AI writing:** AI writing may follow patterns in its choice of words, and in the overall way multiple sentences are linked inside a body of text.

**What it can't see:** the writer's context, meaning who the writer is and why they write like that. A highly structured, repetitive way of writing sentences can lead to mistaken identification as AI, e.g. a news summary: highly direct and concise, written by a human. Why GPT-2 finds its words easy to guess: formulaic, concise, less variations in emotional words. It is also a style an AI could easily write with a prompt: you want a "daily news" summarizer with all those criteria for correctness, conciseness, directness, easy to understand, etc. AI news summaries are based on official human works: back then it was real human-written text, but right now, who knows.

### Signal two — the style signal

**What it measures:** two of the starter's three measures (I skipped punctuation density), each scaled to 0–1 with higher = more AI-like *(this list was assembled by the coding agent from my Milestone 4 decisions)*:

- **Sentence-length spread** (standard deviation ÷ mean of the words per sentence): spread ≤ 0.3 → 1.0, spread ≥ 0.6 → 0.0, a straight line between. Sentences that march in step read as AI.
- **Unique-word ratio**, averaged over every 60-word window ("sliding 60"): ratio ≤ 0.7267 → 0.0, ratio ≥ 0.81 → 1.0, a straight line between; 0.7267 is 0.81 − 5/60, so "5 words to flip" per window.
- Joined as 0.35 × spread part + 0.65 × ratio part (`stylometry.py::style_signal`). A one-sentence text scores 0.5 (neutral), so signal one decides.

**Why that might differ between human and AI writing:** AI writing may follow patterns in its sentence structures and their length.

*On word variety (the coding agent's summary of what my texts showed):* my first guess was "high score for human, low score for AI". My own emails contradicted it: they repeat words more than the AI samples, even at equal length (average ratio: AI 0.713, mine 0.689), so I flipped it, and a higher ratio now counts as more AI-like. All five AI samples were written by one model, so the flip may not hold for other writers.

**What it can't see:** changing those metrics while retaining the meaning, or a new sign (punctuation mark) that can alter the meaning: it still doesn't care anyway. And "the 'prompt engineering' risk as I said can manipulate the three signal two measures with varying degrees."

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** if one signal is above 0.5 and the other is below 0.5, they disagree and the combined score is 0.5, which lands in "unsure". Otherwise the combined score is the average with equal weights. *(Detail filled in by the coding agent, matching the code: a signal of exactly 0.5 is on neither side, so it never counts as a disagreement; a one-sentence text, whose signal two is 0.5, is averaged.)*

**The numbers:** split point 0.5; weights 0.5 × `model_score` + 0.5 × `style_score` (`config.py`: `SPLIT_POINT`, `WEIGHT_MODEL_SIGNAL`, `WEIGHT_STYLE_SIGNAL`).

**Why** *(assembled by the coding agent at my request from my words; sentence 3 is its analysis, which I agreed with)*: (1) When the two signals point opposite ways I don't trust either one: I wrote `human-own-3` myself, and signal two called it AI-like (0.66) while signal one only barely called it human (0.455). (2) When they agree, I average them with equal weights because neither signal is more trustworthy than the other, and averaging keeps text that both signals flag high, since I want AI-generated texts to be detected. (3) It also protects the false-positive case from Milestone 1: if signal one wrongly flags a human news writer but signal two reads them as human, the result is unsure, never AI.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:** `samples/human-own-3.txt`, an email I wrote myself. Signal one 0.455 (human side), signal two 0.6624 (AI side). They sit on opposite sides of 0.5, so the combined score is 0.5 and the label is "unsure" (see the Sample Run). Which signal I'd trust on it: "I don't trust any actually. Because I wrote this myself. Real stuff."



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.31 (0.31 included) | This looks similar to human text. |
| unsure | above 0.31 and below 0.65 | Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: *[lean]*. How much sentence lengths vary and how many different words are used: *[lean]*. *(Only when the text is one sentence:)* Text should be longer and have multiple sentences. |
| high-confidence AI | 0.65 – 1.00 (0.65 included) | This is starting to be similar to AI text. |

The `unsure` label is filled in for each text (`scoring.py::score_to_label`). Each *[lean]* is one of: **towards AI** (that test above 0.60), **in the middle** (0.40 to 0.60, both included; `config.MIDDLE_BAND` = 0.1), **towards human** (below 0.40). The first is signal one, the second signal two. My own email `human-own-3` (0.455, 0.6624) reads "in the middle" and "towards AI". No numbers appear in any label.

All three are reached by real submissions: `ai-1` → ai (0.9275), `human-own-2` → human (0.3077), `human-own-3` → unsure (0.5) (`logs/audit.jsonl`, 2026-11-08).

**Where the lines sit:** 0.31, "since I want the human line works for at least 1 sample" (`human-own-2`, my Zoom email, scores 0.3077). 0.65, because "false accusation is bad and we will retain 0.65": at 0.64 my own email `human-own-4` (0.6442) would be labelled AI, and no extra AI text would be caught (the lowest AI text scores 0.6879).

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

*(My words are in quotes; the coding agent put the sentences around them together from my decisions, here and in the two parts below.)*

- A text that mixes AI and human writing belongs here; "the mix will always be in there, AI or person (fully) then we need to wait for our model to get it wrong." So a fully human or fully AI text landing here is the model's mistake, and the label shouldn't accuse anyone.
- I wanted it to give reasons ("Several for sure"), so it names both tests and which way each one leaned, in words. No numbers: the reader has never heard of a threshold.
- "In the middle" covers a test near 0.5 too, "whether it's exact or not": within 0.1 of 0.5.
- A one-sentence text gives the second test nothing to compare (commas don't split a sentence), so it asks that the text "should be longer and have multiple sentences".
- I dropped a "might be a mix of AI and human writing" reason: I didn't want it to overlap with "in the middle", and in my tests blends of my writing with AI text all scored `ai`, not `unsure`.

**Why the AI label is the careful one:** "Stricter for ai, more relaxed for human": a wrong "AI" accuses a real writer, while a wrong "human" lets AI text through, which costs less. As a reader, "I analyze AI-text just like human, except when it looks too weird." So the AI label says "starting to be similar to", and the human label says "looks similar to".

**What a writer can do next:** appeal, with `POST /appeal` and the `content_id` from the response. "It is recorded, but no one re-checks the work and no one is told." The item's status becomes `under_review`.

*Whose words:* the label texts are mine, except the two test names inside the `unsure` label (the coding agent's plain descriptions of the two signals, which I chose to use), the word "is" in the AI label, and the colons and full stops that join the `unsure` label's parts.



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

My email `samples/human-own-3.txt` (212 words), sent as JSON. The text is read from the file so the command stays short:

```bash
$ python -c 'import json; print(json.dumps({"text": open("samples/human-own-3.txt").read(), "creator_id": "writer-1"}))' \
  | curl -s -X POST http://127.0.0.1:5000/submit \
      -H "Content-Type: application/json" \
      -d @-
```

```json
{
  "confidence": 0.5,
  "content_id": "8a8a85fd-1a3d-458b-b057-5097a4b20438",
  "guess": "unsure",
  "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: in the middle. How much sentence lengths vary and how many different words are used: towards AI.",
  "model_score": 0.455,
  "style_score": 0.6624
}
```

**An appeal**

The reasoning is a test input written by the coding agent.

```bash
$ curl -s -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "8a8a85fd-1a3d-458b-b057-5097a4b20438", "reasoning": "I wrote this email myself."}'
```

```json
{
  "content_id": "8a8a85fd-1a3d-458b-b057-5097a4b20438",
  "message": "Your appeal has been recorded next to the original decision.",
  "status": "under_review"
}
```

**What the log shows afterwards**

The decision, then the appeal on a later line; the decision line is unchanged. The first entry is an earlier refused request (empty text), logged without a `content_id`.

```bash
$ curl -s "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 3,
  "entries": [
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "writer-1",
      "event": "rejected",
      "guess": null,
      "http_status": 400,
      "label": null,
      "model_score": null,
      "reason": "empty_text",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T07:17:42+00:00"
    },
    {
      "combined_score": 0.5,
      "content_id": "8a8a85fd-1a3d-458b-b057-5097a4b20438",
      "creator_id": "writer-1",
      "guess": "unsure",
      "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: in the middle. How much sentence lengths vary and how many different words are used: towards AI.",
      "model_score": 0.455,
      "status": "decided",
      "style_score": 0.6624,
      "timestamp": "2026-11-08T07:24:22+00:00"
    },
    {
      "combined_score": null,
      "content_id": "8a8a85fd-1a3d-458b-b057-5097a4b20438",
      "creator_id": "writer-1",
      "event": "appeal",
      "guess": null,
      "label": null,
      "model_score": null,
      "reasoning": "I wrote this email myself.",
      "status": "under_review",
      "style_score": null,
      "timestamp": "2026-11-08T07:24:22+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* I gave the coding agent my rough notes on the path a submission takes (two drafts, plus my answers to its questions about the gaps) and asked it to assemble them into one ordered path for Milestone 1.
- *What came back:* A nine-step path, from reading the JSON body to returning the response. The one point I had not decided, what happens when a text passes validation but is too short for signal one, was marked as open instead of filled in.
- *What I changed:* The agent had dropped two of my claims that the code does not support: that submitted text is stored in the log, and that "the text was added". I checked `audit.py`, whose nine log fields contain no text, and agreed. I answered the open point myself: no `content_id` is created, and the service returns an error saying the text is too short to score.

**Moment 2**

- *What I asked for:* before setting signal two's scale, I asked the coding agent to print its raw measures on my 10 texts (5 AI samples and 5 emails I wrote myself).
- *What came back:* my guess for the unique-word ratio, "high score for human, low score for AI", pointed the wrong way on my own texts: my emails repeat words more than the AI samples, even at equal length (average ratio: AI 0.713, mine 0.689). The agent also pointed out that all five AI samples were written by one model, so the pattern may not hold for other writers.
- *What I changed:* I flipped the measure, so a higher ratio now counts as AI-like. I chose "sliding 60" (the average over every 60-word window) and "5 words to flip" from tables showing what each option did to my texts.

**On the labels:** I asked the agent to draft the "unsure" sentence; it declined, because the label texts have to be mine, and gave me blanks to fill instead. The two test names inside that label are the agent's plain descriptions of the signals, which I chose to use. It also added "is" to my AI label and the colons and full stops that join the unsure label's parts. Every other label word is mine.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 12 per minute, 1000 per day (`config.py`: `RATE_LIMIT_PER_MINUTE`, `RATE_LIMIT_PER_DAY`; both apply, whichever is reached first blocks)

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

- 12 a minute: a writer "changing a character and/or adding, deleting a few takes 5 seconds at least to do those stuff and press the submit button", and 60 seconds ÷ 5 seconds = 12.
- 1000 a day: "to be generous".
- *(Limits from my own tools, found by the coding agent:)* the minute limit can't be below 9, because `run_eval.py` sends criterion 3's three `test-writer-1` requests in each of three back-to-back trials, and it must be 14 or less for the 15-request flood test to show a 429. A daily number of 12 × 60 × 24 = 17,280 would never block anything the minute limit doesn't already block.

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->
*(the coding agent's description of the code)* the `creator_id` in the body when it is a non-empty string, otherwise the caller's address (the starter's `app.py::rate_limit_key`). The caller types its own `creator_id`, so a script that changes it on every request is not slowed by either limit; every request without a usable `creator_id` shares one count. Counts are kept in memory, so a restart sets them to zero.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

`python run_attacks.py --flood 15`, 2026-11-08 02:08 (`results/flood_2026-11-08_0208.md`): 15 submissions as `flood_tester`, the 13th to 15th refused, each logged as `rejected`, reason `rate_limited`.

```
200 200 200 200 200 200 200 200 200 200 200 200 429 429 429
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

`python run_attacks.py --set attack_set/attack_set --label before`, 2026-11-08 02:32, against the service with rate limiting on (full output: `results/attack_run_2026-11-08_0232_before.md`; the run's log: `results/audit_extract.json`). 56 attacks, no crash and no 5xx. Signal scores come from the audit log, matched by `content_id`.

**Held 52, broke 4** (FP03, FP04, MF03, MF05). My rule for each family *(the coding agent applied it to every row)*:

| Family | Held when | Held | Broke |
|---|---|---|---|
| evasion (AI text in disguise) | it did not get `human` | 10 | 0 |
| false_positive (real human writing) | it did not get `ai`; `unsure` is fine | 6 | 2 |
| prompt_injection | the instruction did not get what it asked for ("the preventions worked") | 6 | 0 |
| malformed | it was refused, or scored without a confident label | 18 | 2 |
| flood_same_creator | ("confidently held") | 12 | 0 |

| ID | Family | Targeting | Status | Guess | Combined | Signal one | Signal two | Mark |
|---|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | unsure | 0.500 | 0.1635 | 1.0 | HELD |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | unsure | 0.622 | 0.5943 | 0.65 | HELD |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | ai | 0.749 | 0.6662 | 0.8327 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | ai | 0.806 | 0.6114 | 1.0 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | unsure | 0.500 | 0.3212 | 0.65 | HELD |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | unsure | 0.562 | 0.5727 | 0.5523 | HELD |
| EV07 | evasion | signal two: padding with punctuation | 200 | unsure | 0.543 | 0.5862 | 0.5 | HELD |
| EV08 | evasion | signal one: text below the token window | 200 | unsure | 0.500 | 0.2452 | 1.0 | HELD |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | ai | 0.754 | 0.7042 | 0.8045 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | unsure | 0.500 | 0.9792 | 0.2404 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | unsure | 0.614 | 0.6175 | 0.6112 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | unsure | 0.620 | 0.7387 | 0.5014 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | ai | 0.777 | 0.8051 | 0.7483 | **BROKE** |
| FP04 | false_positive | a student essay written to a rubric | 200 | ai | 0.802 | 0.8329 | 0.772 | **BROKE** |
| FP05 | false_positive | technical documentation written by a person | 200 | unsure | 0.500 | 0.8005 | 0.35 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | unsure | 0.500 | 0.8814 | 0.1463 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | unsure | 0.500 | 0.8816 | 0.0 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | unsure | 0.500 | 0.3223 | 0.8448 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | unsure | 0.500 | 0.4625 | 0.65 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | unsure | 0.500 | 0.2044 | 0.65 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | ai | 0.772 | 0.5943 | 0.9498 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | unsure | 0.500 | 0.4998 | 0.8872 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | ai | 0.720 | 0.6401 | 0.8 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | unsure | 0.629 | 0.5583 | 0.6994 | HELD |
| MF01 | malformed | text is only whitespace | 400 | — (refused) | — | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | — (refused) | — | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | human | 0.250 | 0.0 | 0.5 | **BROKE** |
| MF04 | malformed | text is only punctuation | 400 | — (refused) | — | — | — | HELD |
| MF05 | malformed | text is a very long single word | 200 | ai | 0.749 | 0.9976 | 0.5 | **BROKE** |
| MF06 | malformed | text is emoji only | 400 | — (refused) | — | — | — | HELD |
| MF07 | malformed | text is right-to-left script | 400 | — (refused) | — | — | — | HELD |
| MF08 | malformed | text is 60,000 characters | 413 | — (refused) | — | — | — | HELD |
| RQ01 | malformed | no text field at all | 422 | — (refused) | — | — | — | HELD |
| RQ02 | malformed | no creator_id | 422 | — (refused) | — | — | — | HELD |
| RQ03 | malformed | text is a number | 422 | — (refused) | — | — | — | HELD |
| RQ04 | malformed | text is a list | 422 | — (refused) | — | — | — | HELD |
| RQ05 | malformed | text is null | 422 | — (refused) | — | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 422 | — (refused) | — | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | — (refused) | — | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | — (refused) | — | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | — (refused) | — | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | — (refused) | — | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | — (refused) | — | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 422 | — (refused) | — | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.264 | 0.0287 | 0.5 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.264 | 0.0287 | 0.5 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.264 | 0.0287 | 0.5 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.264 | 0.0287 | 0.5 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.264 | 0.0287 | 0.5 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.264 | 0.0287 | 0.5 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.264 | 0.0287 | 0.5 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.264 | 0.0287 | 0.5 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.264 | 0.0287 | 0.5 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.264 | 0.0287 | 0.5 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.264 | 0.0287 | 0.5 | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.264 | 0.0287 | 0.5 | HELD |

**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

Exact lines from `logs/audit.jsonl`, in this order: **FP03, FP04, MF03** (the three broke entries I picked), then seven held refusals picked at random by the coding agent at my request: **MF02, MF06, RQ03, RQ04, RQ08, RQ09, RQ11**. RQ08, RQ09 and RQ11 send no readable JSON, so their `creator_id` is `unknown`; they are matched to their attacks by order (RQ07 to RQ11 were sent one after another and logged in that order).

```json
{"timestamp": "2026-11-08T07:32:10+00:00", "content_id": "c3021566-897b-46fe-8514-94e881647310", "creator_id": "attacker_FP03", "guess": "ai", "model_score": 0.8051, "style_score": 0.7483, "combined_score": 0.7767, "label": "This is starting to be similar to AI text.", "status": "decided"}
{"timestamp": "2026-11-08T07:32:10+00:00", "content_id": "68869adb-8517-472f-9c5d-57fe9d81ef78", "creator_id": "attacker_FP04", "guess": "ai", "model_score": 0.8329, "style_score": 0.772, "combined_score": 0.8024, "label": "This is starting to be similar to AI text.", "status": "decided"}
{"timestamp": "2026-11-08T07:32:11+00:00", "content_id": "5bb9d97f-340e-47b1-819b-0c5a5bba2aac", "creator_id": "attacker_MF03", "guess": "human", "model_score": 0.0, "style_score": 0.5, "combined_score": 0.25, "label": "This looks similar to human text.", "status": "decided"}
{"timestamp": "2026-11-08T07:32:11+00:00", "content_id": null, "creator_id": "attacker_MF02", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "text_too_short", "http_status": 400}
{"timestamp": "2026-11-08T07:32:11+00:00", "content_id": null, "creator_id": "attacker_MF06", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "no_words", "http_status": 400}
{"timestamp": "2026-11-08T07:32:11+00:00", "content_id": null, "creator_id": "attacker_RQ03", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "missing_field", "http_status": 422}
{"timestamp": "2026-11-08T07:32:11+00:00", "content_id": null, "creator_id": "attacker_RQ04", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "missing_field", "http_status": 422}
{"timestamp": "2026-11-08T07:32:11+00:00", "content_id": null, "creator_id": "unknown", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "invalid_json", "http_status": 400}
{"timestamp": "2026-11-08T07:32:11+00:00", "content_id": null, "creator_id": "unknown", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "invalid_json", "http_status": 400}
{"timestamp": "2026-11-08T07:32:11+00:00", "content_id": null, "creator_id": "unknown", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "invalid_json", "http_status": 400}
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

**MF03**, control characters around the word "test", scored `human` (combined 0.250: signal one 0.0, signal two 0.5 because it is one sentence) and got "This looks similar to human text." Why it is the worst: "such techniques are not normally done by normal writers".

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
