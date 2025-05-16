from pathlib import Path
from math import inf

txt = Path(__file__).parent / "input.txt"


def solution():
    lines = txt.read_text().splitlines()
    to_int = lambda s: sum(2**i * (c in ["B", "R"]) for i, c in enumerate(s[::-1]))

    a, b, s = inf, -inf, 0
    for line in lines:
        n = to_int(line[:7]) * 8 + to_int(line[-3:])
        a, b, s = min(a, n), max(b, n), s + n

    return (b + a) * (b - a + 1) // 2 - s
