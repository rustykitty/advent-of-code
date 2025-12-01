import sys

schematics = [schematic.split('\n') for schematic in sys.stdin.read().strip().split('\n\n')]

keys = [schematic for schematic in schematics if all(i == '#' for i in schematic[0]) and all(i == '.' for i in schematic[-1])]
locks = [schematic for schematic in schematics if all(i == '.' for i in schematic[0]) and all(i == '#' for i in schematic[-1])]

def calculate_height(schematic):
    return tuple(n - 1 for n in (sum(schematic[j][i] == '#' for j in range(len(schematic))) for i in range(len(schematic[0]))))

res = 0

for key in keys:
    for lock in locks:
        if key == lock: # shouldnt happen but whatever
            continue
        if all(i + j <= len(key[0]) for i, j in zip(calculate_height(key), calculate_height(lock))):
            res += 1

print(res)