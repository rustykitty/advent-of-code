import re
from functools import reduce

spaces = re.compile(r" +")

*numbers, operations = (
    re.split(spaces, line.strip())
    for line in
    open("6.in").read().strip().split("\n")
)

del spaces

numbers = tuple(
    tuple(map(int, line))
    for line in numbers
)

rows = len(numbers)
cols = len(operations)

numbers = tuple(
    tuple(
        numbers[row][col] for row in range(rows)
    )
    for col in range(cols)
)

assert all(op in "+*" for op in operations)

res = 0

for i in range(cols):
    if operations[i] == "+":
        res += sum(numbers[i])
    elif operations[i] == "*":
        res += reduce(lambda x, y: x * y, numbers[i])
    else:
        raise AssertionError

print(res)