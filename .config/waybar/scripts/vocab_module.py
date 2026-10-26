#!/usr/bin/env python3
import json, os, sys, time

WORDS_FILE = os.path.expanduser("~/.config/waybar/words.json")
STATE_FILE = "/tmp/vocab_state.json"
ROTATE_EVERY = 10

def load_words():
    try:
        with open(WORDS_FILE, encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

words = load_words()
keys = list(words.keys())
n = len(keys)

if n == 0:
    print(json.dumps({"text": "No Vocab"}))
    sys.exit(0)

try:
    with open(STATE_FILE) as f:
        s = json.load(f)
    index     = s.get("index", 0) % n
    revealed  = s.get("revealed", False)
    timestamp = s.get("timestamp", 0)
except:
    index, revealed, timestamp = 0, False, 0

now = time.time()
action = sys.argv[1] if len(sys.argv) > 1 else "status"

if action == "click":
    revealed = not revealed
    if not revealed:                 # just hid the meaning → restart the timer
        timestamp = now

elif action == "next":
    index = (index + 1) % n
    revealed = False
    timestamp = now

elif action == "prev":
    index = (index - 1) % n
    revealed = False
    timestamp = now

else:  # status / interval
    # Only rotate when the meaning is HIDDEN
    if not revealed and (now - timestamp >= ROTATE_EVERY):
        index = (index + 1) % n
        timestamp = now

with open(STATE_FILE, "w") as f:
    json.dump({"index": index, "revealed": revealed, "timestamp": timestamp}, f)

word = keys[index]
if revealed:
    text = f"{word}  <span>{words[word]}</span>"
else:
    text = word

print(json.dumps({"text": text}, ensure_ascii=False))
