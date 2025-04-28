from pathlib import Path
import re

txt = Path(__file__).parent / "input.txt"


def is_valid(line: str) -> bool:
    match = re.match("(\d+)-(\d+) (\w): (\w+)", line)
    x, y, char, pwd = match.groups()
    return int(x) <= pwd.count(char) <= int(y)


def solution():
    lines = txt.read_text().splitlines()
    return sum(is_valid(line) for line in lines)
