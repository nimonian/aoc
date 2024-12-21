from pathlib import Path

path = Path(__file__).parent / "input.txt"
G = [list(line) for line in path.read_text().strip().splitlines()]
R, C = range(len(G)), range(len(G[0]))

visited = {}


def inside(x, y):
    return x in R and y in C


def fill(r0, c0):
    Q = set([(r0, c0)])
    group = set([(r0, c0)])

    while len(Q):
        r, c = Q.pop()
        visited[(r, c)] = True
        group.add((r, c))
        steps = [(r + dr, c + dc) for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]]
        nbrs = set((x, y) for x, y in steps if inside(x, y) and G[x][y] == G[r][c])
        Q.update((x, y) for x, y in nbrs if not visited.get((x, y)))

    return group


def solution():
    for r in R:
        for c in C:
            if (r, c) in visited:
                continue

            print(fill(r, c))
