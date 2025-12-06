"""
This script should work in theory but it is way too slow.
"""


fresh, available = open("5.in").read().rstrip().split("\n\n")

fresh = (line.split("-") for line in fresh.split("\n"))
fresh = tuple(
    range(x, y + 1) for x, y in ((int(k) for k in line) for line in fresh)
)

del available # Don't need it

res = 0

low = min(r.start for r in fresh)
hi = max(r.stop - 1 for r in fresh)

for n in range(low, hi + 1):
    if any(n in r for r in fresh):
        res += 1

print(res)