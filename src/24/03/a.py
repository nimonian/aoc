from pathlib import Path
import re
from functools import reduce

path = Path(__file__).parent / "input.txt"
txt = path.read_text().strip()


def solution():
    matches = re.findall(r"mul\((\d+),(\d+)\)", txt)
    return sum(int(x) * int(y) for x, y in matches)
