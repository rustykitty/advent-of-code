data = open("1.in").read().strip().splitlines()

data = [
    -int(op[1:]) if op[0] == 'L' else int(op[1:])
    for op in data
]

d = 50

n = 0

for op in data:
    
    d += op

    if not (0 <= d <= 99):
        d %= 100

    if d == 0:
        n += 1

print(n)