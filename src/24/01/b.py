from pathlib import Path
import re

path = Path(__file__).parent / "input.txt"
txt = path.read_text().strip()


def solution():
    nums = [int(n) for n in re.findall(r"(\d+)", txt)]
    X = [nums[2 * k] for k in range(len(nums) // 2)]
    Y = [nums[2 * k + 1] for k in range(len(nums) // 2)]

    return sum(x * Y.count(x) for x in X)
