from pathlib import Path
import re

path = Path(__file__).parent / "input.txt"
txt = path.read_text().strip()


def solution():
    nums = [int(n) for n in re.findall(r"(\d+)", txt)]
    return sum(x * nums[1::2].count(x) for x in nums[::2])
