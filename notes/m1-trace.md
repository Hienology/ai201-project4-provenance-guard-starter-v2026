# Milestone 1: tracing a submission

## 1. The path a submission takes

**Draft 3 (2026-10-31, current; assembled by the agent from my answers below; reviewed and confirmed by me):**

1. A POST request arrives at `/submit` and the JSON body is read → adds `text` and `creator_id`.
2. Check it (validation) → adds a request that is safe to score. If it fails: catch it and respond gracefully, with no id created. What the response says: Part 4.
3. Signal one: pass the text to the model (`detector.model_signal(text)`) → adds `model_score`, from 0 to 1.
   - If it fails after validation passed (fewer than 3 tokens raises `ValueError`): no id has been created yet. My answer: no id, and return the error of not enough tokens and need more to pass to our models, that's it.
4. Signal two: stylometry on the same text (`stylometry.style_signal(text)`) → adds `style_score`, from 0 to 1.
5. Combine both scores (`scoring.combine_signals(...)`) → adds the third number, the combined score, sent as `confidence`. What that number means: Part 4.
6. Create the `content_id`, only now, so only real decisions get ids → adds `content_id`.
7. Turn the combined score into words (`scoring.score_to_label(...)`) → adds `guess` (`ai`, `human` or `unsure`) and `label`, the sentence the writer reads.
8. Write one log entry (`audit.log_decision(...)`), before the response, because code after `return` never runs → adds one line to `logs/audit.jsonl` with all nine fields. The logger fills in `timestamp`; `status` is `decided`. The text itself is not stored.
9. Return the response: success → the writer gets `content_id`, `guess`, `confidence`, `label`, `model_score`, `style_score`.

**Draft 1 (2026-10-31):**

1. POST to `/submit`
2. The body is passed in JSON
3. Check it
4. Put it to the part it is needed
5. Before it can succeed, it must pass all those validations (try/catch, fallbacks, validations, etc.)
6. Good: then we pass. Not: then catch + fallbacks must do it gracefully

Open question: the primary key (`content_id`). I think it is automatically generated, but at which stage?

**Draft 2 (2026-10-31):**

1. Take the text and `creator_id` being passed (POST request's body in JSON)
2. Pass to the model by a signal with our text
3. All text being submitted are stored in central logs
4. Another signal of the same text to mark stylometry, which provides a second score
5. Then we combined both scores for the same text, three scores in total for the response
6. Then return our response while acknowledging the POST request was successful, the text was added

**Gap 2, where the `content_id` is created (2026-10-31):** after the combined score is done and before returning the whole response, which is end of M4 and before start of M5?

**Gap 3, where the log goes (2026-10-31):** after step 8, because step 8 generates the label before putting them in the response.

**Decision (2026-10-31):** `content_id` is created by my handler only after validation passes, so only real decisions get ids. Why: failed ids, then save them for what? And showing potential case errors/alerts associated with faulty ids can aid attacks.

## 2. The two signals

**Draft 2 (2026-10-31; the agent joined my Draft 1 fragments into sentences, one signal at a time, with no new ideas; I then answered every gap myself):**

**Signal one, the model signal (`detector.py`)**

- What it measures: which word comes and how expected it is, meaning the surprise is low or high (expected or not). The average surprise of all those words is the perplexity. The one doing the expecting is a model (GPT-2). Low surprise, aka expected/predictable, is guessable as AI: a low overall average means more likely AI. Higher perplexity → human-ish → low score; lower perplexity → low overall average → more likely AI → high score.
- Why it might differ between human and AI writing: AI writing may follow patterns in its choice of words, and in the overall way multiple sentences are linked inside a body of text.
- What it can't see: the writer's context, meaning who the writer is and why they write like that. A highly structured, repetitive way of writing sentences can lead to mistaken identification as AI, e.g. a news summary: highly direct and concise, written by a human. Why GPT-2 finds its words easy to guess: formulaic, concise, less variations in emotional words. It is also a style an AI could easily write with a prompt: you want a "daily news" summarizer with all those criteria for correctness, conciseness, directness, easy to understand, etc. AI news summaries are based on official human works: back then it was real human-written text, but right now, who knows.

**Signal two, the style signal (`stylometry.py`)**

- What it measures (the starter's three candidate measures; which ones I use is decided in M4): `sentence_length_spread`, do sentences vary in length, or march in step? `type_token_ratio`, how much of the vocabulary repeats? `punctuation_density`, how much punctuation, and how varied?
- Why it might differ between human and AI writing: AI writing may follow patterns in its sentence structures and their length.
- What it can't see: changing those metrics while retaining the meaning, or a new sign (punctuation mark) that can alter the meaning: it still doesn't care anyway.

**Draft 1 (2026-10-31; covers both signals at once, to be split):**

- Why it might differ: for AI writing, I guess it follows patterns in choice of words, sentence and grammar structures with regards to its length, plus the overall way multiple sentences are linked inside a body of text given.
- What it can't see: context, I guess.

## 3. The false-positive trace

**Draft 1 (2026-10-31):**

1. The writer: a human writing a news summary (my example from Part 2): highly direct and concise.
2. Signal one: a high score.
3. Signal two: the score can vary, depending on several patterns that are taken into the metrics.
4. Combined score: the average of those two scores (the starter's placeholder rule; mine comes in M4).
5. Which label: I expect it lands more on AI, but I'll trace the unsure case.
6. What that label would mean to them (assembled by the agent from my earlier words; confirmed by me): "unsure" says the service can't tell whether I or an AI wrote it; right now, who knows. My readers might not care, as long as it is correct, all factors are fairly covered, plus the context.
7. What they can do about it: appeal. It is recorded, but no one re-checks the work and no one is told. That sounds like a fair risk.
8. The cost, in one sentence: it varies a lot. As a reader, would I trust a news analysis written entirely by AI? Yes, therefore the question will vary a lot based on the type of article for each text.

## Questions for later (M4 and M5)

- How much AI involvement counts as "AI"? Answering specific questions based on original stuff, a summary, or the whole article 100% AI, or partly with AI support? Where should AI-assisted text land among my three labels? (2026-10-31)

## 4. The endpoint contracts

### `POST /submit`, draft 1 (2026-11-01)

- What `confidence` means: **A, AI-likelihood.** It is the combined score from 0 to 1: 0 = human-like, 1 = AI-like, the same direction as `model_score` and `style_score`, and the same number as `combined_score` in the log. Why A: I want to proceed and save my time.
- Missing `text` or `creator_id` → 422
- Not JSON → 400
- Empty text → 400
- Too short (fewer than 3 tokens) → 400
- Enormous: over 350 words → reject with 413. Why: we can argue anyway, 300 is the fairest limit. (The 413 code was the agent's suggestion.)
- What each error message says (agent draft from my rules; confirmed by me; short on purpose, since showing error details can aid attacks):
  - not JSON → 400 `{"error": "invalid_json", "message": "The request body must be JSON."}`
  - missing (or not a string) `text` or `creator_id` → 422 `{"error": "missing_field", "message": "Both text and creator_id are required."}`
  - empty text → 400 `{"error": "empty_text", "message": "The text is empty."}`
  - too short → 400 `{"error": "text_too_short", "message": "The text is too short to score. Please send at least a few sentences."}`
  - too long → 413 `{"error": "text_too_long", "message": "The text is too long to score. Please send at most 350 words."}` (agent draft; confirmed by me, including that it states the limit)
  - No `content_id` is created for any of these.
- Success → 200 with `content_id`, `guess`, `confidence`, `label`, `model_score`, `style_score`

### `POST /appeal`, draft 1 (2026-11-01)

- In: JSON `{"content_id": "...", "reasoning": "..."}`
- Unknown `content_id` → 404
- Missing or empty `reasoning` → allowed, as normal
- Same item appealed a second time → reject (409, the agent's suggestion; confirmed by me)
- Not JSON, or missing `content_id` → same rules as `/submit`: 400 and 422 (the agent's assumption; confirmed by me)
- Messages (agent draft from my rules; confirmed by me):
  - unknown id → 404 `{"error": "unknown_content_id", "message": "No decision was found for that content_id."}`
  - second appeal → 409 `{"error": "already_appealed", "message": "This decision has already been appealed."}`
  - success → 200 `{"content_id": "...", "status": "under_review", "message": "Your appeal has been recorded next to the original decision."}`
- What an appeal does not do: it does not change the score or the label, re-check the work, or notify anyone.
