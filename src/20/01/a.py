from pathlib import Path
from toolz import compose
from toolz.curried import map

txt = Path(__file__).parent / "input.txt"
target = 2020


def solution():
    parse = compose(sorted, map(int))
    L = parse(txt.read_text().splitlines())

    i, j = 0, len(L) - 1

    while i < j:
        n = L[i] + L[j]

        if n == target:
            return L[i] * L[j]
        if n < target:
            i += 1
        else:
            j -= 1
