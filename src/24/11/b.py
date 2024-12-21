def transform(L):
    result = []

    for x in L:
        y = str(x)
        if x == 0:
            result.append(1)

        elif len(y) % 2 == 0:
            result.append(int(y[: len(y) // 2]))
            result.append(int(y[len(y) // 2 :]))

        else:
            result.append(x * 2024)

    return result


L = [0]
U = set()

for _ in range(30):
    L = transform(L)
    if U.issuperset(L):
        print(_, U, len(U))
        break

    U.update(set(L))
