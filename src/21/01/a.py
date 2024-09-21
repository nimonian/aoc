from pathlib import Path


def solution():
    file = Path(__file__).parent / "input.txt"
    lines = file.read_text().splitlines()
    nums = [int(line) for line in lines]

    return sum(nums[i + 1] > nums[i] for i in range(len(nums) - 1))
