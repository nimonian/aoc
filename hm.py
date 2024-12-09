L = [{"a": 1}, {"a": 2}, {"a": 3}]

for x in L[::-1]:
    x["a"] = 4

print(L)
