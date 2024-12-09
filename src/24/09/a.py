from pathlib import Path
from functools import reduce

path = Path(__file__).parent / "input.txt"
nums = [int(x) for x in path.read_text().strip()]


def solution():
    files = nums[::2]
    space = nums[1::2]
    expanded = reduce(lambda x, y: x + [y[0]] * y[1], enumerate(files), [])

    i, compacted = 0, []

    while len(expanded):
        for _ in range(files[i]):
            try:
                compacted.append(expanded.pop(0))
            except:
                break

            if not len(expanded):
                break

        for _ in range(space[i]):
            try:
                compacted.append(expanded.pop(-1))
            except:
                break

        i += 1

    return sum(i * x for i, x in enumerate(compacted))
