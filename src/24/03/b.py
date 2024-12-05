from pathlib import Path
import re
from functools import reduce

path = Path(__file__).parent / "input.txt"
txt = "do()" + path.read_text().strip()


def do_mul_sum(s):
    matches = re.findall(r"mul\((\d+),(\d+)\)", s)
    return sum(int(x) * int(y) for x, y in matches)


def solution():
    pattern = r"do\(\)(.*?)don\'t\(\)"
    lines = re.findall(pattern, txt, re.DOTALL)
    nums = map(do_mul_sum, lines)
    return sum(nums)
