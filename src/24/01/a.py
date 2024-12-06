from pathlib import Path
import re

path = Path(__file__).parent / "input.txt"
txt = path.read_text().strip()


def solution():
    nums = [int(n) for n in re.findall(r"(\d+)", txt)]
    return sum(abs(x - y) for x, y in zip(sorted(nums[::2]), sorted(nums[1::2])))
