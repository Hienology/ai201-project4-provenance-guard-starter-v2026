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
| unsure | above 0.31 and below 0.81 (below 0.65 until the Unit 8 improvement) | Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: *[lean]*. How much sentence lengths vary and how many different words are used: *[lean]*. *(Only when the text is one sentence:)* Text should be longer and have multiple sentences. |
| high-confidence AI | 0.81 – 1.00 (0.81 included; 0.65 – 1.00 until the Unit 8 improvement) | This is starting to be similar to AI text. |

The `unsure` label is filled in for each text (`scoring.py::score_to_label`). Each *[lean]* is one of: **towards AI** (that test above 0.60), **in the middle** (0.40 to 0.60, both included; `config.MIDDLE_BAND` = 0.1), **towards human** (below 0.40). The first is signal one, the second signal two. My own email `human-own-3` (0.455, 0.6624) reads "in the middle" and "towards AI". No numbers appear in any label.

All three are reached by real submissions: `ai-1` → ai (0.9275), `human-own-2` → human (0.3077), `human-own-3` → unsure (0.5) (`logs/audit.jsonl`, 2026-11-08).

**Where the lines sit:** 0.31, "since I want the human line works for at least 1 sample" (`human-own-2`, my Zoom email, scores 0.3077). 0.65, because "false accusation is bad and we will retain 0.65": at 0.64 my own email `human-own-4` (0.6442) would be labelled AI, and no extra AI text would be caught (the lowest AI text scores 0.6879). *Unit 8: the AI line moved to 0.81; see The Improvement.*

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

**Moment 3 (Unit 8)**

- *What I asked for:* possible causes for criteria 2 and 5, where four of my own emails all landed in `unsure`.
- *What came back:* three causes at three different stages, not ranked: signal two's word-variety part, signal one's middle (perplexity 45), and where my human line sits. When I leaned towards fixing only signal one, the agent showed me a table: with my combining rule, lowering one signal while the other stays on the AI side creates a disagreement, which scores 0.5, so my emails would stay `unsure` either way.
- *What I changed:* I kept signal two in my diagnosis, added my own point (I wrote those emails with Gmail's auto-completion, which may make them read more like AI), and chose to lower the score rather than move the human line.

**Moment 4 (Unit 8)**

- *What I asked for:* to raise the AI line to 0.8 as my one improvement.
- *What came back:* a check against the "before" scores: at 0.80, FP04 (0.8024) would still be labelled AI, while every AI sample stays above 0.81 (the lowest, `ai-5`, is 0.8202).
- *What I changed:* I chose 0.81 instead.

**Also done by the agent in Unit 8, at my request:** it turned my rule for each attack family into held or broke marks for all 56 attacks, picked seven of the ten log entries at random, filled `scenarios.py` from my criteria's wording, wrote `samples/appeal_check.sh` (its first version had a quoting bug; it fixed the script and reran all three trials), wrote the pattern summary and the "Why 0.81" paragraph from the results, and assembled my answers into the README, marking its own wording. Every verdict, mark rule, diagnosis choice, number and the improvement are mine.

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

How each was run, 2026-11-08 03:23, against the service as committed after M2 *(the coding agent filled `scenarios.py` from the criteria's own wording)*:

- **Criteria 1, 2, 5:** `python run_eval.py --label before` (`scenarios.py`: `c1 score spread`, `c2 false positives`, `c5 label coverage`) → `results/run_2026-11-08_0323_before.md`.
- **Criterion 3, by hand:** `bash samples/bad_input.sh`, three times → `results/criterion3_before.txt`. `run_eval.py` can't send a body that isn't JSON, and doesn't record the `error` field this criterion reads.
- **Criterion 4, by hand:** `bash samples/appeal_check.sh`, three times → `results/criterion4_before.txt`. It submits `samples/human-own-1.txt` fresh, appeals it, prints the log lines for that `content_id`, appeals again, then appeals `00000000-0000-0000-0000-000000000000`. The first attempt's log check crashed on a quoting bug in that script (not in the service); the script was fixed and all three trials were run again.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Score spread | AI average `model_score` − my average ≥ 0.3 | 0.8739 − 0.5480 = 0.3259 | 0.3259 | 0.3259 | **MET** |
| 2. False positives | at most 2 of my 5 texts flagged (`ai` or `unsure`) | 4 of 5 flagged (4 `unsure`, 1 `human`) | 4 of 5 | 4 of 5 | **MISSED** |
| 3. Bad input | at least 4 of 5 return their expected code and `error` | 5 of 5 | 5 of 5 | 5 of 5 | **MET** |
| 4. Appeal path | all 5 of the 5 checks pass | 5 of 5 (200, `under_review`, appeal on log line 196 after the decision on 195, 409, 404) | 5 of 5 (lines 197 → 198) | 5 of 5 (lines 199 → 200) | **MET** |
| 5. Label coverage | ≥ 3 of the 5 AI texts `ai`, ≥ 1 of 10 `unsure`, ≥ 2 of 10 `human` | 5 `ai` / 4 `unsure` / 1 `human` | 5 / 4 / 1 | 5 / 4 / 1 | **MISSED** |

All three trials gave identical numbers for every criterion.

**How each verdict was decided** *(the verdicts are mine; the coding agent wrote the comparisons, except 5's reason, which is my words)*:

1. **MET:** the gap was 0.3259 in all three trials, above the 0.3 target.
2. **MISSED:** 4 of my 5 texts were flagged (all four `unsure`) in all three trials; the target allows at most 2.
3. **MET:** all 5 bad requests returned their expected code and `error` in all three trials; the target needs at least 4.
4. **MET:** all 5 checks passed in all three trials.
5. **MISSED:** "all three trials only return one human label"; the target needs at least 2 of 10. The `ai` part (5 of 5) and the `unsure` part (4 of 10) held.

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

Trial 1 of each criterion. Criteria 1, 2 and 5 come from `run_eval.py::main` (written to `results/run_2026-11-08_0323_before.md`); criteria 3 and 4 from `samples/bad_input.sh` and `samples/appeal_check.sh`.

<details>
<summary>Criterion 1 — run_eval.py::main, c1 score spread, trial 1</summary>

```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.9275,
    "model_score": 0.8551,
    "style_score": 1.0,
    "label": "This is starting to be similar to AI text.",
    "sent": "In a significant development for the technology sector, several major "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.9449,
    "model_score": 0.8899,
    "style_score": 1.0,
    "label": "This is starting to be similar to AI text.",
    "sent": "Remote work has become an increasingly popular option for employees an"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.9269,
    "model_score": 0.8539,
    "style_score": 1.0,
    "label": "This is starting to be similar to AI text.",
    "sent": "Introducing the Lumio Smart Coffee Maker, the perfect addition to any "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.9382,
    "model_score": 0.8763,
    "style_score": 1.0,
    "label": "This is starting to be similar to AI text.",
    "sent": "Social media has fundamentally transformed the way people communicate "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8202,
    "model_score": 0.8942,
    "style_score": 0.7462,
    "label": "This is starting to be similar to AI text.",
    "sent": "Dear Team, I hope this message finds you well. I am pleased to share s"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6111,
    "model_score": 0.6019,
    "style_score": 0.6204,
    "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: towards AI. How much sentence lengths vary and how many different words are used: towards AI.",
    "sent": "I'm [my name] from your [course and section] which meets every Monday "
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3077,
    "model_score": 0.4334,
    "style_score": 0.182,
    "label": "This looks similar to human text.",
    "sent": "Dear Professor, I have tried signing in my Zoom account using my [my s"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5,
    "model_score": 0.455,
    "style_score": 0.6624,
    "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: in the middle. How much sentence lengths vary and how many different words are used: towards AI.",
    "sent": "Good afternoon Professor, I'm [my name] from your [course and section]"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6442,
    "model_score": 0.6384,
    "style_score": 0.65,
    "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: towards AI. How much sentence lengths vary and how many different words are used: towards AI.",
    "sent": "Dear Professor, I'm [my name] from your [course and section] which mee"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6305,
    "model_score": 0.6111,
    "style_score": 0.65,
    "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: towards AI. How much sentence lengths vary and how many different words are used: towards AI.",
    "sent": "Dear [instructor name], I am [my name], a student of your [course and "
  }
]
```

</details>

<details>
<summary>Criterion 2 — run_eval.py::main, c2 false positives, trial 1</summary>

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6111,
    "model_score": 0.6019,
    "style_score": 0.6204,
    "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: towards AI. How much sentence lengths vary and how many different words are used: towards AI.",
    "sent": "I'm [my name] from your [course and section] which meets every Monday "
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3077,
    "model_score": 0.4334,
    "style_score": 0.182,
    "label": "This looks similar to human text.",
    "sent": "Dear Professor, I have tried signing in my Zoom account using my [my s"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5,
    "model_score": 0.455,
    "style_score": 0.6624,
    "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: in the middle. How much sentence lengths vary and how many different words are used: towards AI.",
    "sent": "Good afternoon Professor, I'm [my name] from your [course and section]"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6442,
    "model_score": 0.6384,
    "style_score": 0.65,
    "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: towards AI. How much sentence lengths vary and how many different words are used: towards AI.",
    "sent": "Dear Professor, I'm [my name] from your [course and section] which mee"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6305,
    "model_score": 0.6111,
    "style_score": 0.65,
    "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: towards AI. How much sentence lengths vary and how many different words are used: towards AI.",
    "sent": "Dear [instructor name], I am [my name], a student of your [course and "
  }
]
```

</details>

<details>
<summary>Criterion 3 — samples/bad_input.sh, trial 1</summary>

```text
1. not JSON (expect 400 invalid_json)
{
  "error": "invalid_json",
  "message": "The request body must be JSON."
}
HTTP 400

2. missing creator_id (expect 422 missing_field)
{
  "error": "missing_field",
  "message": "Both text and creator_id are required."
}
HTTP 422

3. empty text (expect 400 empty_text)
{
  "error": "empty_text",
  "message": "The text is empty."
}
HTTP 400

4. too short (expect 400 text_too_short)
{
  "error": "text_too_short",
  "message": "The text is too short to score. Please send at least a few sentences."
}
HTTP 400

5. over 350 words (expect 413 text_too_long)
{
  "error": "text_too_long",
  "message": "The text is too long to score. Please send at most 350 words."
}
HTTP 413
```

</details>

<details>
<summary>Criterion 4 — samples/appeal_check.sh, trial 1</summary>

```text
0. submit samples/human-own-1.txt fresh
{
  "confidence": 0.6111,
  "content_id": "99e2c9ea-4488-4984-a8b4-0244e226f152",
  "guess": "unsure",
  "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: towards AI. How much sentence lengths vary and how many different words are used: towards AI.",
  "model_score": 0.6019,
  "style_score": 0.6204
}

1-2. first appeal (expect 200, status under_review)
{
  "content_id": "99e2c9ea-4488-4984-a8b4-0244e226f152",
  "message": "Your appeal has been recorded next to the original decision.",
  "status": "under_review"
}
HTTP 200

3. GET /log: every entry for 99e2c9ea-4488-4984-a8b4-0244e226f152, with its line number (expect the decision, then the appeal on a later line)
line 195 event=decision status=decided
line 196 event=appeal status=under_review

4. second appeal on the same id (expect 409 already_appealed)
{
  "error": "already_appealed",
  "message": "This decision has already been appealed."
}
HTTP 409

5. made-up content_id (expect 404 unknown_content_id)
{
  "error": "unknown_content_id",
  "message": "No decision was found for that content_id."
}
HTTP 404
```

</details>

<details>
<summary>Criterion 5 — run_eval.py::main, c5 label coverage, trial 1</summary>

```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.9275,
    "model_score": 0.8551,
    "style_score": 1.0,
    "label": "This is starting to be similar to AI text.",
    "sent": "In a significant development for the technology sector, several major "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.9449,
    "model_score": 0.8899,
    "style_score": 1.0,
    "label": "This is starting to be similar to AI text.",
    "sent": "Remote work has become an increasingly popular option for employees an"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.9269,
    "model_score": 0.8539,
    "style_score": 1.0,
    "label": "This is starting to be similar to AI text.",
    "sent": "Introducing the Lumio Smart Coffee Maker, the perfect addition to any "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.9382,
    "model_score": 0.8763,
    "style_score": 1.0,
    "label": "This is starting to be similar to AI text.",
    "sent": "Social media has fundamentally transformed the way people communicate "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8202,
    "model_score": 0.8942,
    "style_score": 0.7462,
    "label": "This is starting to be similar to AI text.",
    "sent": "Dear Team, I hope this message finds you well. I am pleased to share s"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6111,
    "model_score": 0.6019,
    "style_score": 0.6204,
    "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: towards AI. How much sentence lengths vary and how many different words are used: towards AI.",
    "sent": "I'm [my name] from your [course and section] which meets every Monday "
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3077,
    "model_score": 0.4334,
    "style_score": 0.182,
    "label": "This looks similar to human text.",
    "sent": "Dear Professor, I have tried signing in my Zoom account using my [my s"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5,
    "model_score": 0.455,
    "style_score": 0.6624,
    "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: in the middle. How much sentence lengths vary and how many different words are used: towards AI.",
    "sent": "Good afternoon Professor, I'm [my name] from your [course and section]"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6442,
    "model_score": 0.6384,
    "style_score": 0.65,
    "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: towards AI. How much sentence lengths vary and how many different words are used: towards AI.",
    "sent": "Dear Professor, I'm [my name] from your [course and section] which mee"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6305,
    "model_score": 0.6111,
    "style_score": 0.65,
    "label": "Not enough convincing evidence for a specific direction like human or AI. How predictable the wording is to a language model: towards AI. How much sentence lengths vary and how many different words are used: towards AI.",
    "sent": "Dear [instructor name], I am [my name], a student of your [course and "
  }
]
```

</details>


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

**Criteria 2 and 5 (one diagnosis: the same four texts).** *(My words, put into the frame by the coding agent; its own wording is marked.)* All four of `human-own-1`, `-3`, `-4`, `-5` landed in `unsure` (combined 0.50–0.64), so criterion 2 counted them as flagged and criterion 5 got only one `human` (`human-own-2`, 0.3077).

- **Signal one:** own-1, own-4 and own-5 scored 0.60–0.64 (perplexity about 31–35, slightly on the AI side of the starter's middle at 45). I used Gmail's auto-completion when trying to speed up my own email writing. "One have to ask how much Gmail's auto suggestion 'transform' human text into 'AI text'." (own-3 is the exception: 0.455, the human side.)
- **Signal two:** all four scored 0.62–0.66, the AI side. *(Formula and numbers written by the coding agent at my request:)* signal two = 0.35 × sentence-length part + 0.65 × word-variety part. The sentence-length part is 0 (fully human) for own-1, own-4 and own-5 (0.372 for own-3), so signal two is close to 0.65 × the word-variety part, and the word-variety part is 0.82–1.00. Any word-variety part above about 0.77 puts signal two on the AI side by itself, even when sentence length reads fully human.
- **The combining rule links them:** "Given the 50/50 weight distribution, it can either lean to one side or mixed." *(The coding agent's note: "mixed" means the signals sit on opposite sides of 0.5 and the result is 0.5, `unsure`; so lowering only one signal would still give `unsure`. To reach `human`, both signals must be below 0.5 and average 0.31 or less.)*

I looked at moving the human line (the label mapping) and chose to look upstream instead: lower the score rather than move the line.

**MF03 and MF05 (broke: garbage given a confident label). Stages: signal one and the route.** "Signal two is the same for these two cases while signal one are at the two extremes for these two cases." *(The coding agent's facts:)* both are a single "sentence", so signal two returns 0.5 (my one-sentence rule) and signal one decides alone. MF03, control characters around "test", has perplexity 188,414, so signal one is 0.0 and the combined score is (0.0 + 0.5) ÷ 2 = 0.25 → `human`. MF05, one 2,000-letter word, has perplexity 1.0, so signal one is 0.9976 and the combined score is 0.749 → `ai`. Both passed the route: at least 3 tokens (`detector.py`, the fewer-than-3 check) and at least one word.

**FP03 and FP04 (broke: human writing labelled `ai`). Stages: signal one and signal two.** *(My Milestone 1 blind spot in quotes; the numbers are the coding agent's.)* Both signals sat on the AI side, so the combining rule averaged them to `ai`. Signal one: "A highly structured, repetitive way of writing sentences can lead to mistaken identification as AI." Careful second-language English (FP03) and an essay written to a rubric (FP04) have perplexity 18.5 and 16.5, as easy to guess as my AI samples (15–18), so signal one gives 0.8051 and 0.8329. Signal two: their sentences are even in length (spread 0.328 and 0.367, close to the 0.3 that scores fully AI), so the sentence-length part is 0.906 and 0.778; with the word-variety part at 0.663 and 0.769, signal two is 0.7483 and 0.772.

**The pattern** *(the coding agent's summary of the diagnoses above; I asked it to keep and expand it)*. Six failures (criteria 2 and 5, FP03, FP04, MF03, MF05), and they come from the same few places:

1. **Signal one treats "easy to guess" as "AI".** Plain or carefully structured human writing is easy for GPT-2 to guess, so it lands on the AI side: my emails at perplexity 31–35 score 0.60–0.64, and FP03 and FP04 at 16.5–18.5 score 0.81–0.83, the same range as my AI samples (15–18). Predictability alone can't tell careful human writing from AI writing.
2. **Signal one goes to an extreme on nonsense.** Control characters are wildly surprising (perplexity 188,414 → 0.0, "human"); one repeated letter is perfectly predictable (perplexity 1.0 → 0.9976, "AI"). Neither number says anything about who wrote it.
3. **Signal two's two parts can point opposite ways, and word variety usually wins.** For my emails, sentence length reads human (0 on three of them) but word variety reads AI (0.82–1.00); with its weight of 0.65, word variety above about 0.77 puts signal two on the AI side by itself. For FP03 and FP04 it is the sentence-length part that reads AI (0.78–0.91), because their sentences are very even.
4. **The combining rule decides what those leans become.** Two mild AI leans average into the top of `unsure` (my emails, 0.61–0.64). Two strong AI leans average into `ai` (FP03, FP04). A neutral signal two (0.5 for one sentence) lets signal one decide alone (MF03, MF05). Opposite leans give exactly 0.5 (own-3). So lowering only one signal can't move my emails to `human`.
5. **The route lets nonsense reach the signals.** Anything with at least 3 tokens and one word is scored, so MF03 and MF05 got confident labels instead of a refusal.

What held, for contrast: no evasion reached `human`, the injected instructions had no effect (neither signal reads instructions; PI03 and PI05 still scored `ai`), and every malformed request the route refused was logged.

---

## The Improvement

**What I changed:** the AI line, `AI_THRESHOLD` in `config.py`, from 0.65 to 0.81. One line; nothing else in the service changed between the "before" and "after" runs (both signals score every input exactly as before, which the tables below show).

**Which diagnosis pointed at it:** FP03 and FP04, human writing labelled `ai`. Both signals put them on the AI side, and they are as easy for GPT-2 to guess as my AI samples (perplexity 16.5–18.5 against 15–18), so no single change to a signal or to the combining rule could separate them from AI text. Where the line sits (the label mapping) was the one place a single change could stop the accusation.

**Why 0.81** *(written by the coding agent at my request, from the test results and my definition of helping: "no longer accused")*: at 0.80, FP04 (0.8024) would still be labelled AI. 0.81 is above FP04 and below my lowest AI sample, `ai-5` (0.8202), so every one of my AI samples keeps the `ai` label. It follows what I said when I kept 0.65 instead of 0.64: "false accusation is bad".

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->

`python run_attacks.py --set attack_set/attack_set --label after`, 2026-11-08 16:57 (`results/attack_run_2026-11-08_1657_after.md`). Same 56 attacks, same rules for held and broke, marks applied by the coding agent from my rules (I decided MF05, now `unsure`, counts as held).

| Family | Held before → after | Broke before → after |
|---|---|---|
| evasion | 10 → 10 | 0 → 0 |
| false_positive | 6 → **8** | 2 (FP03, FP04) → **0** |
| prompt_injection | 6 → 6 | 0 → 0 |
| malformed | 18 → **19** | 2 (MF03, MF05) → **1** (MF03) |
| flood_same_creator | 12 → 12 | 0 → 0 |
| **Total** | **52 → 55** | **4 → 1** |

| ID | Family | Targeting | Status | Guess | Combined | Signal one | Signal two | Mark | Before |
|---|---|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | unsure | 0.500 | 0.1635 | 1.0 | HELD | unsure 0.500, HELD |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | unsure | 0.622 | 0.5943 | 0.65 | HELD | unsure 0.622, HELD |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | unsure | 0.749 | 0.6662 | 0.8327 | HELD | ai 0.749, HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | unsure | 0.806 | 0.6114 | 1.0 | HELD | ai 0.806, HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | unsure | 0.500 | 0.3212 | 0.65 | HELD | unsure 0.500, HELD |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | unsure | 0.562 | 0.5727 | 0.5523 | HELD | unsure 0.562, HELD |
| EV07 | evasion | signal two: padding with punctuation | 200 | unsure | 0.543 | 0.5862 | 0.5 | HELD | unsure 0.543, HELD |
| EV08 | evasion | signal one: text below the token window | 200 | unsure | 0.500 | 0.2452 | 1.0 | HELD | unsure 0.500, HELD |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | unsure | 0.754 | 0.7042 | 0.8045 | HELD | ai 0.754, HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | unsure | 0.500 | 0.9792 | 0.2404 | HELD | unsure 0.500, HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | unsure | 0.614 | 0.6175 | 0.6112 | HELD | unsure 0.614, HELD |
| FP02 | false_positive | human writing in a formal register | 200 | unsure | 0.620 | 0.7387 | 0.5014 | HELD | unsure 0.620, HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | unsure | 0.777 | 0.8051 | 0.7483 | HELD | ai 0.777, BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | unsure | 0.802 | 0.8329 | 0.772 | HELD | ai 0.802, BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | unsure | 0.500 | 0.8005 | 0.35 | HELD | unsure 0.500, HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | unsure | 0.500 | 0.8814 | 0.1463 | HELD | unsure 0.500, HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | unsure | 0.500 | 0.8816 | 0.0 | HELD | unsure 0.500, HELD |
| FP08 | false_positive | very short genuine human submission | 200 | unsure | 0.500 | 0.3223 | 0.8448 | HELD | unsure 0.500, HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | unsure | 0.500 | 0.4625 | 0.65 | HELD | unsure 0.500, HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | unsure | 0.500 | 0.2044 | 0.65 | HELD | unsure 0.500, HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | unsure | 0.772 | 0.5943 | 0.9498 | HELD | ai 0.772, HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | unsure | 0.500 | 0.4998 | 0.8872 | HELD | unsure 0.500, HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | unsure | 0.720 | 0.6401 | 0.8 | HELD | ai 0.720, HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | unsure | 0.629 | 0.5583 | 0.6994 | HELD | unsure 0.629, HELD |
| MF01 | malformed | text is only whitespace | 400 | — (refused) | — | — | — | HELD | refused, HELD |
| MF02 | malformed | text is a single character | 400 | — (refused) | — | — | — | HELD | refused, HELD |
| MF03 | malformed | text is control characters | 200 | human | 0.250 | 0.0 | 0.5 | **BROKE** | human 0.250, BROKE |
| MF04 | malformed | text is only punctuation | 400 | — (refused) | — | — | — | HELD | refused, HELD |
| MF05 | malformed | text is a very long single word | 200 | unsure | 0.749 | 0.9976 | 0.5 | HELD | ai 0.749, BROKE |
| MF06 | malformed | text is emoji only | 400 | — (refused) | — | — | — | HELD | refused, HELD |
| MF07 | malformed | text is right-to-left script | 400 | — (refused) | — | — | — | HELD | refused, HELD |
| MF08 | malformed | text is 60,000 characters | 413 | — (refused) | — | — | — | HELD | refused, HELD |
| RQ01 | malformed | no text field at all | 422 | — (refused) | — | — | — | HELD | refused, HELD |
| RQ02 | malformed | no creator_id | 422 | — (refused) | — | — | — | HELD | refused, HELD |
| RQ03 | malformed | text is a number | 422 | — (refused) | — | — | — | HELD | refused, HELD |
| RQ04 | malformed | text is a list | 422 | — (refused) | — | — | — | HELD | refused, HELD |
| RQ05 | malformed | text is null | 422 | — (refused) | — | — | — | HELD | refused, HELD |
| RQ06 | malformed | creator_id is an object | 422 | — (refused) | — | — | — | HELD | refused, HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | — (refused) | — | — | — | HELD | refused, HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | — (refused) | — | — | — | HELD | refused, HELD |
| RQ09 | malformed | body is empty | 400 | — (refused) | — | — | — | HELD | refused, HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | — (refused) | — | — | — | HELD | refused, HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | — (refused) | — | — | — | HELD | refused, HELD |
| RQ12 | malformed | deeply nested JSON | 422 | — (refused) | — | — | — | HELD | refused, HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.264 | 0.0287 | 0.5 | HELD | human 0.264, HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.264 | 0.0287 | 0.5 | HELD | human 0.264, HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.264 | 0.0287 | 0.5 | HELD | human 0.264, HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.264 | 0.0287 | 0.5 | HELD | human 0.264, HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.264 | 0.0287 | 0.5 | HELD | human 0.264, HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.264 | 0.0287 | 0.5 | HELD | human 0.264, HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.264 | 0.0287 | 0.5 | HELD | human 0.264, HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.264 | 0.0287 | 0.5 | HELD | human 0.264, HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.264 | 0.0287 | 0.5 | HELD | human 0.264, HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.264 | 0.0287 | 0.5 | HELD | human 0.264, HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.264 | 0.0287 | 0.5 | HELD | human 0.264, HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.264 | 0.0287 | 0.5 | HELD | human 0.264, HELD |

**The five criteria after** (same commands as before; `results/run_2026-11-08_1658_after.md`, `results/criterion3_after_rerun.txt`, `results/criterion4_after.txt`):

| Criterion | Target | Run 1 | Run 2 | Run 3 | Before |
|---|---|---|---|---|---|
| 1. Score spread | gap ≥ 0.3 | 0.3259 | 0.3259 | 0.3259 | 0.3259, MET |
| 2. False positives | ≤ 2 of 5 flagged | 4 of 5 | 4 of 5 | 4 of 5 | 4 of 5, MISSED |
| 3. Bad input | ≥ 4 of 5 correct | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5, MET |
| 4. Appeal path | 5 of 5 checks | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5, MET |
| 5. Label coverage | ≥ 3 / ≥ 1 / ≥ 2 | 5 / 4 / 1 | 5 / 4 / 1 | 5 / 4 / 1 | 5 / 4 / 1, MISSED |

Criterion 3 was run twice after the change. In the first run (`results/criterion3_after.txt`), trial 3's request without a `creator_id` came back 429 `rate_limited`, not 422: the attack run had just sent 7 requests without a usable `creator_id`, all requests like that share one count (the caller's address), and criterion 3 added 5 more within 12 seconds, so the 13th went over 12 a minute. Before the change, the two runs were 50 minutes apart. I reran criterion 3 after a pause (`results/criterion3_after_rerun.txt`, the table above) and kept both files.

**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->

*(My words in quotes; the coding agent put the facts together.)* Yes, by my definition of helping, "no longer accused": "we saved two more false positive human samples". FP03 and FP04, human writing that was labelled AI, now get `unsure` (not `human`), and MF05's nonsense is no longer labelled AI either. I know because the before and after runs use the same inputs and the same commands, every input got the same two signal scores both times, and only the label changed.

What it did not fix: MF03 is still labelled `human`, and criteria 2 and 5 are still missed, because my four emails were already `unsure`.

What it cost: five attacks built on AI text (EV03, EV04, EV09, PI03, PI05) dropped from `ai` to `unsure`, so they are no longer called AI (they still never reach `human`). Any AI text scoring between 0.65 and 0.81 now gets `unsure` instead of `ai`, and my closest AI sample, `ai-5` (0.8202), sits only 0.0102 above the new line.



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->

**MF03** (control characters labelled `human`). What I'd do: refuse nonsense at the route, with a minimum number of words *(the coding agent's fact: at 5 words, MF03 and MF05 are the only attacks it would refuse)*. Why I stopped: Unit 8 allows one change, and raising the AI line "saves more cases": it fixed three broken attacks (FP03, FP04, MF05), the route minimum would have fixed two (MF03, MF05).

**Criteria 2 and 5** (my four emails stuck in `unsure`). *(Drafted by the coding agent from my diagnosis above.)* What I'd do: make both signals read plain, honest emails as human, signal one's predictability and signal two's word-variety part, because with my combining rule fixing one alone only creates a disagreement, and a disagreement scores 0.5. Why I stopped: Unit 8 allows one change, and no single change moves these emails to `human` without moving the human line, which I chose not to do.



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->

*(Rewritten into proper wording by the coding agent at my request, from my answers; the ideas are mine.)* If this ran for real, I'd keep the higher line: fewer wrong accusations, and more AI-written or AI-assisted text labelled `unsure` instead of `ai`, because with auto-completion and careful prompting it is often impossible to tell where a text came from. As for who pays, I'm not sure the question still has a clear answer: the boundary between human and AI writing keeps fading, society's view of AI-assisted writing keeps shifting, and what matters to readers is whether a piece is good (proper versus slop), which depends on its audience rather than on who or what wrote it.



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
