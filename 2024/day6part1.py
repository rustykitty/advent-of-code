import sys
labmap = [list(i) for i in sys.stdin.read().rstrip().split('\n')]
pos = (-1, -1)

def repeat(i):
    while True:
        for ele in i:
            yield ele

def get(pos):
    x, y = pos
    return labmap[x][y]

for i in range(len(labmap)):
    for j in range(len(labmap[0])):
        if labmap[i][j] == '^':
            pos = (i, j)
            labmap[i][j] = '.'

gen = repeat([
        (-1, 0), # up
        (0, 1), # right
        (1, 0), # down
        (0, -1) # left
])

add = (lambda a, b: tuple(i + j for (i, j) in zip(a, b)))

direction = next(gen)

visited = set()

while True:
    fwd_p = add(pos, direction)
    print(fwd_p)
    if fwd_p[0] >= len(labmap[0]) or fwd_p[1] >= len(labmap) \
        or fwd_p[0] < 0 or fwd_p[1] < 0:
        direction = next(gen)
        break
    if get(fwd_p) == '#':
        direction = next(gen)
        continue
    else:
        visited.add(pos)
        pos = add(direction, pos)

print(len(visited) + 1)