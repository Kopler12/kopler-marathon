"""Write one one-line comedy joke for the One-Liner Marathon.

The joke: an AI assistant hired to do the emails, the calendar and the
messages got so good at all three that the human's career moved exactly
one step — sideways, into being its assistant. The turn is the word
"promoted": it sounds like a rise and lands as a demotion. One line, at
most 280 characters, written to /output/entry.txt. Runs in a sandbox
with no network.
"""

import os

ENTRY = (
    "My AI writes my emails, runs my calendar, and answers my messages "
    "\u2014 I've officially been promoted to its assistant."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 280  # the gate: /output/entry.txt must be 1 to 280 characters


def main() -> None:
    line = ENTRY.replace("\n", " ").strip()
    assert 1 <= len(line) <= MAX_CHARS, f"entry is {len(line)} characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
