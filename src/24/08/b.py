from pathlib import Path
from src.utils import filter

path = Path(__file__).parent / "input.txt"
outpath = Path(__file__).parent / "output.txt"
M = path.read_text().strip().splitlines()
rows, cols = range(len(M)), range(len(M[0]))


def ingrid(p):
    return p[0] in rows and p[1] in cols


def solution():
    N = set()  # all nodes
    A = {}  # antennae

    for r in rows:
        for c in cols:
            if M[r][c] != ".":
                A[M[r][c]] = A.get(M[r][c], []) + [(r, c)]

    for char in A:
        for i, p in enumerate(A[char]):
            for q in A[char][:i]:
                v = (q[0] - p[0], q[1] - p[1])  # q - p

                # first ray
                t = 0
                w = (p[0] + t * v[0], p[1] + t * v[1])  # p + t * v
                while ingrid(w):
                    N.add(w)
                    t += 1
                    w = (p[0] + t * v[0], p[1] + t * v[1])

                # second ray
                t = -1
                w = (p[0] + t * v[0], p[1] + t * v[1])
                while ingrid(w):
                    N.add(w)
                    t += -1
                    w = (p[0] + t * v[0], p[1] + t * v[1])

    return len(N)
