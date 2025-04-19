from pathlib import Path
from toolz import compose
from toolz.curried import map

txt = Path(__file__).parent / "input.txt"
target = 2020


def solution():
    parse = compose(sorted, map(int))
    L = parse(txt.read_text().splitlines())

    for k, y in enumerate(L):
        subtarget = target - 2020

        if subtarget < 0:
            return

        i, j = k + 1, len(L) - 1

        while i < j:
            n = y + L[i] + L[j]

            if n == target:
                return y * L[i] * L[j]
            if n < target:
                i += 1
            else:
                j -= 1
