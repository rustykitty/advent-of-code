import sys

stones = [int(i) for i in sys.stdin.readline().rstrip().split(' ')]

for n in range(25):
    old_stones = stones.copy()
    stones = []
    for i in old_stones:
        if i == 0:
            stones.append(1)
        elif (len(str(i)) & 1) == 0:
            e = len(str(i)) // 2
            stones.append(int(str(i)[0:e]))
            stones.append(int(str(i)[e:]))
        else:
            stones.append(i * 2024)
print(len(stones))
