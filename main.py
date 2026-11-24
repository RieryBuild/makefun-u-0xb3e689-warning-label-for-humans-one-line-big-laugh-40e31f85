"""Warning Label for Humans: One Line, Big Laugh — make.fun bounty entry.

Writes one single-line safety warning label for every human being to
/output/entry.txt. Deterministic: the same fixed text on every run.
Python 3.13 stdlib only, no network.
"""

import os

# Final label, chosen after critiquing 8 in-session candidates against the
# judge criteria in order (see gate-run.md): strongest on recognition +
# end-turn + label form. One concrete, universal human moment — saying yes
# to plans, then hoping they get cancelled — with the turn landing in the
# last few words, in real printed-label wording.
# Exact size: 123 characters / 123 bytes (ASCII only), inside the 160 limit.
LABEL = "CAUTION: Contents under pressure. Will say 'yes' to every plan, then spend the whole week quietly hoping it gets cancelled."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
