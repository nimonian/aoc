from functools import reduce, cache
from typing import Iterable


def compose(*funcs):

    def _compose(f, g):
        return lambda x: f(g(x))

    return reduce(_compose, funcs, lambda x: x)


def prod(L: Iterable[float]) -> float:
    return reduce(lambda x, y: x * y, L, 1)


@cache
def cartesian(lists):

    if len(lists) == 1:
        return tuple((a,) for a in lists[0])

    A = lists[0]
    B = cartesian(lists[1:])

    return tuple((a,) + b for a in A for b in B)


def filter(f, A):
    return [a for a in A if f(a)]
