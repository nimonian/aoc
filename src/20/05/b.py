from pathlib import Path
from math import inf

txt = Path(__file__).parent / "input.txt"


def solution():
    lines = txt.read_text().splitlines()
    to_int = lambda s: sum(2**i * (c in ["B", "R"]) for i, c in enumerate(s[::-1]))
    id = lambda s: to_int(s[:7]) * 8 + to_int(s[-3:])

    a, b, s = inf, -inf, 0
    for line in lines:
        n = id(line)
        a, b, s = min(a, n), max(b, n), s + n

    return (b + a) * (b - a + 1) // 2 - s
