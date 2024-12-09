from pathlib import Path
from src.utils import filter

path = Path(__file__).parent / "input.txt"
outpath = Path(__file__).parent / "output.txt"
M = path.read_text().strip().splitlines()
rows, cols = range(len(M)), range(len(M[0]))


def ingrid(p):
    return p[0] in rows and p[1] in cols


def solution():
    N = set()  # nodes
    A = {}  # antennae

    for r in rows:
        for c in cols:
            if M[r][c] != ".":
                A[M[r][c]] = A.get(M[r][c], []) + [(r, c)]

    for char in A:
        for i, p in enumerate(A[char]):
            for q in A[char][:i]:
                u = (2 * q[0] - p[0], 2 * q[1] - p[1])  # r1 = 2q - p
                v = (2 * p[0] - q[0], 2 * p[1] - q[1])  # r2 = 2p - q

                N.update(filter(ingrid, [u, v]))

    return len(N)
