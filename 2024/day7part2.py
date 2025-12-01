import sys
import itertools

data = [x.split(': ') for x in sys.stdin.read().rstrip().split('\n')]

res = 0

funcs = [
    lambda x, y: x + y, 
    lambda x, y: x * y,
    lambda x, y: int(str(x) + str(y)) # concat operator
]

for i in data:
    a, b = i
    a = int(a)
    b = tuple(int(x) for x in b.split(' '))
    for x in itertools.product(funcs, repeat=len(b) - 1):
        r = b[0]
        for j in range(len(b) - 1):
            r = x[j](r, b[j + 1])
        if a == r:
            res += r
            break

print(res)