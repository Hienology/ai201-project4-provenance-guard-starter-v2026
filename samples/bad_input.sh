#!/usr/bin/env bash
# Criterion 3: the five bad requests to POST /submit, each printed with what it should return.
# Start the service first (python app.py), then in a second terminal:
#
#   bash samples/bad_input.sh

URL="http://127.0.0.1:5000/submit"
LONG_TEXT=$(printf 'word %.0s' $(seq 1 400))   # 400 words, over the 350-word limit

echo "1. not JSON (expect 400 invalid_json)"
curl -s -w "HTTP %{http_code}\n\n" -X POST "$URL" -H "Content-Type: application/json" \
  -d 'this is not json'

echo "2. missing creator_id (expect 422 missing_field)"
curl -s -w "HTTP %{http_code}\n\n" -X POST "$URL" -H "Content-Type: application/json" \
  -d '{"text": "A sentence with enough words in it to be scored."}'

echo "3. empty text (expect 400 empty_text)"
curl -s -w "HTTP %{http_code}\n\n" -X POST "$URL" -H "Content-Type: application/json" \
  -d '{"text": "   ", "creator_id": "test-writer-1"}'

echo "4. too short (expect 400 text_too_short)"
curl -s -w "HTTP %{http_code}\n\n" -X POST "$URL" -H "Content-Type: application/json" \
  -d '{"text": "Hi", "creator_id": "test-writer-1"}'

echo "5. over 350 words (expect 413 text_too_long)"
curl -s -w "HTTP %{http_code}\n\n" -X POST "$URL" -H "Content-Type: application/json" \
  -d "{\"text\": \"$LONG_TEXT\", \"creator_id\": \"test-writer-1\"}"
