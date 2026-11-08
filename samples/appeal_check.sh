#!/usr/bin/env bash
# Criterion 4: the appeal path, one trial. Run it three times.
# Start the service first (python app.py), then from the repo root:
#
#   bash samples/appeal_check.sh

URL="http://127.0.0.1:5000"
TEXT_FILE="samples/human-own-1.txt"

echo "0. submit $TEXT_FILE fresh"
BODY=$(python3 -c 'import json, sys; print(json.dumps({"text": open(sys.argv[1]).read(), "creator_id": "appeal-check"}))' "$TEXT_FILE")
RESP=$(curl -s -X POST "$URL/submit" -H "Content-Type: application/json" -d "$BODY")
echo "$RESP"
ID=$(echo "$RESP" | python3 -c 'import json, sys; print(json.load(sys.stdin)["content_id"])')
echo

echo "1-2. first appeal (expect 200, status under_review)"
curl -s -w "HTTP %{http_code}\n\n" -X POST "$URL/appeal" -H "Content-Type: application/json" \
  -d "{\"content_id\": \"$ID\", \"reasoning\": \"I wrote this myself.\"}"

echo "3. GET /log: every entry for $ID, with its line number (expect the decision, then the appeal on a later line)"
curl -s "$URL/log" | python3 -c '
import json, sys
entries = json.load(sys.stdin)["entries"]
for n, e in enumerate(entries, 1):
    if e.get("content_id") == sys.argv[1]:
        kind = e.get("event", "decision")
        print("line", n, "event=" + kind, "status=" + e["status"])
' "$ID"
echo

echo "4. second appeal on the same id (expect 409 already_appealed)"
curl -s -w "HTTP %{http_code}\n\n" -X POST "$URL/appeal" -H "Content-Type: application/json" \
  -d "{\"content_id\": \"$ID\", \"reasoning\": \"Appealing again.\"}"

echo "5. made-up content_id (expect 404 unknown_content_id)"
curl -s -w "HTTP %{http_code}\n\n" -X POST "$URL/appeal" -H "Content-Type: application/json" \
  -d '{"content_id": "00000000-0000-0000-0000-000000000000", "reasoning": "Not a real id."}'
