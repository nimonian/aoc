from pathlib import Path
from functools import reduce
from src.utils import cartesian
import re

path = Path(__file__).parent / "input.txt"
txt = path.read_text().strip().splitlines()
lines = [re.findall(r"(\d+)", line) for line in txt]


def f(x, y):
    match y[0]:
        case "+":
            return x + y[1]
        case "*":
            return x * y[1]


def solution():
    operators = ("*", "+")
    result = 0

    for target, *nums in [map(int, line) for line in lines]:
        ops = cartesian((operators,) * (len(nums) - 1))

        for op in ops:

            if target == reduce(f, zip(op, nums[1:]), nums[0]):
                result += int(target)
                break

    return result
