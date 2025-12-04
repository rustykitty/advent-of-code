import itertools

grid = tuple(
    tuple(
        c == "@" for c in row
    ) for row in open("4.in").read().strip().split('\n')
)

def getNeighborCount(grid, x, y):
    n = len(grid)
    m = len(grid[0])

    res = 0

    for (i, j) in itertools.product((x - 1, x, x + 1), (y - 1, y, y + 1)):
        if not (0 <= i < n and 0 <= j < m):
            continue
        if (i, j) == (x, y):
            continue

        res += grid[i][j]

    return res

n = len(grid)
m = len(grid[0])

res = 0

for i in range(n):
    for j in range(m):
        if grid[i][j]:
            if getNeighborCount(grid, i, j) < 4:
                res += 1

print(res)