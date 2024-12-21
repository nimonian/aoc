from pathlib import Path

path = Path(__file__).parent / "input.txt"
G = [list(line) for line in path.read_text().strip().splitlines()]
R, C = range(len(G)), range(len(G[0]))

visited = {}


def inside(x, y):
    return x in R and y in C


def fill(r0, c0):
    Q = set([(r0, c0)])
    A, P = 0, 0

    while len(Q):
        r, c = Q.pop()
        visited[(r, c)] = True
        steps = [(r + dr, c + dc) for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]]
        neighbour = set((x, y) for x, y in steps if inside(x, y) and G[x][y] == G[r][c])

        A += 1
        P += 4 - len(neighbour)

        Q.update((x, y) for x, y in neighbour if not visited.get((x, y)))

    return A, P


def solution():
    result = 0

    for r in R:
        for c in C:
            if (r, c) in visited:
                continue

            A, P = fill(r, c)
            result += A * P

    return result
