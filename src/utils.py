from functools import reduce


def compose(*funcs):

    def _compose(f, g):
        return lambda x: f(g(x))

    return reduce(_compose, funcs, lambda x: x)
