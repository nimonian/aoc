from pathlib import Path
import re


get_nums = lambda line: [int(d) for d in re.findall(r"(\d+)", line)]


def is_safe(nums):
    d0 = nums[1] - nums[0]
    for i in range(len(nums) - 1):
        d = nums[i + 1] - nums[i]

        if (d * d0) < 0:
            return False

        if not 0 < abs(d) < 4:
            return False

    return True


def is_kinda_safe(nums):
    subs = (nums[:i] + nums[i + 1 :] for i in range(len(nums)))
    return any(is_safe(sub) for sub in subs)


def solution():
    path = Path(__file__).parent / "input.txt"
    lines = path.read_text().strip().splitlines()
    lines = (get_nums(line) for line in lines)
    return sum(is_safe(line) or is_kinda_safe(line) for line in lines)
