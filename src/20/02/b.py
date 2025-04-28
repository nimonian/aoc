from pathlib import Path
import re

txt = Path(__file__).parent / "input.txt"


def is_valid(line: str) -> bool:
    match = re.match("(\d+)-(\d+) (\w): (\w+)", line)
    x, y, char, pwd = match.groups()
    count = (pwd[int(x) - 1] == char) + (pwd[int(y) - 1] == char)
    return count == 1


def solution() -> int:
    lines = txt.read_text().splitlines()
    return sum(is_valid(line) for line in lines)
