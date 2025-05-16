from pathlib import Path

txt = Path(__file__).parent / "input.txt"


def solution():
    lines = txt.read_text().splitlines()
    to_int = lambda s: sum(2**i * (c in ["B", "R"]) for i, c in enumerate(s[::-1]))
    id = lambda s: to_int(s[:7]) * 8 + to_int(s[-3:])
    return max(map(id, lines))
