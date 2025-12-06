fresh, available = open("5.in").read().rstrip().split("\n\n")

fresh = (line.split("-") for line in fresh.split("\n"))
fresh = tuple(
    range(x, y + 1) for x, y in ((int(k) for k in line) for line in fresh)
)

available = tuple(
    int(x)
    for x in available.split("\n")
)

res = 0

for n in available:
    res += any(n in f for f in fresh)

print(res)