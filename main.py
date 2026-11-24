"""Entry for make.fun: Two-Sentence Horror.

Writes the two-sentence story to /output/entry.txt (UTF-8, 1-400 chars).
Deterministic, stdlib only, no network.

The story is the whole entry: exactly two sentences, exactly as written below.
"""

import os

ENTRY = "The smart speaker finally answered a question I never asked, in my own voice. When I unplugged it, it whispered, 'That was never the power cord.'"

# The bounty gate allows 1-400 characters; refuse to write anything outside it.
# len() counts Unicode code points, which is what the gate counts as
# characters, so this check matches the sealed scorer exactly.
if not 1 <= len(ENTRY) <= 400:
    raise SystemExit(f"entry is {len(ENTRY)} characters, outside the 1-400 gate")

# The bounty asks for exactly two sentences; refuse anything else.
if ENTRY.count(".") != 2:
    raise SystemExit("entry must be exactly two sentences")

OUTPUT_PATH = "/output/entry.txt"

os.makedirs("/output", exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(ENTRY)

# Read back and confirm the file holds exactly the entry story: what the
# grader reads must be what was intended, byte for byte.
with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
    written = f.read()
if written != ENTRY:
    raise SystemExit("entry.txt does not match the entry story after writing")
