ranges = [tuple(int(x) for x in l.split('-')) for l in open('2.in').readline().split(',')]

n = 0

for rang in ranges:
    for i in range(rang[0], rang[1] + 1):
        s = str(i)
        if len(s) % 2 == 0 and s[:len(s)//2] == s[len(s)//2:]:
            n += i

print(n)
