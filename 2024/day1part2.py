import sys

list1 = []
list2 = {}

def dl(d: dict, k: int):
    if k in d:
        return d[k]
    else:
        print('0')
        return 0

while (line := sys.stdin.readline()) != '':
    line = [int(i) for i in line[:-1].split()]
    list1.append(line[0])
    list2[line[1]] = dl(list2, line[1]) + 1

res = 0

for i in list1:
    print(i, res)
    res += dl(list2, i) * i

print(res)
