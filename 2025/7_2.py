data = open("7.in").read().rstrip().split("\n")
s = data[0].index("S")
n = len(data)
m = len(data[0])

from functools import lru_cache

@lru_cache()
def traverse(beam, pos):
    if not (0 <= beam < m):
        return 0
    if pos >= n:
        return 1

    if data[pos][beam] == "^":
        return traverse(beam - 1, pos + 1) + traverse(beam + 1, pos + 1)
    else:
        return traverse(beam, pos + 1)

print(traverse(s, 1))
