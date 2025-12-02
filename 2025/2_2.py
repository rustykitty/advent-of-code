import itertools

ranges = [tuple(int(x) for x in l.split('-')) for l in open('2.in').readline().split(',')]

it = itertools.chain(*(range(a, b + 1) for a, b in ranges))

n = 0

for i in it:
        s = str(i)
        for j in range(1, len(s)):
            if len(s) % j == 0 and all(s[:j] == s[k:k+j] for k in range(0, len(s), j)):
                n += i
                break

print(n)
