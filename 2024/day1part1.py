import sys

list1 = []
list2 = []

while (line := sys.stdin.readline()) != '':
    line = [int(i) for i in line[:-1].split()]
    list1.append(line[0]), list2.append(line[1])

list1.sort()
list2.sort()

res = 0

for i, j in zip(list1, list2):
    res += abs(i - j)

print(res)
