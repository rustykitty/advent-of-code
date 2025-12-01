data = open("1.in").read().splitlines()

data = [
    -int(op[1:]) if op[0] == 'L' else int(op[1:])
    for op in data
]

d = 50

n = 0

for op in data:
    diff = -1 if op < 0 else 1

    for _ in range(abs(op)):
        d += diff

        if not (0 <= d <= 99):
            d %= 100

        if d == 0:
            n += 1

print(n)