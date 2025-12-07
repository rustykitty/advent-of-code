# The cursed solution below...
# Don't even ask me how this works, I have no idea

import re
from functools import reduce

data = open("6.in").read().rstrip("\n").split("\n")

reop = re.compile(r"[+*]")

operations = []

*numbers_data, operations_data = data

del data

start = 0

columns = []

while (match := reop.search(operations_data, start)):
    columns.append(match.start())
    operations.append(operations_data[match.start()])
    start = match.end()

del start
del match
del reop

columns.append(len(operations_data) + 1)

numbers = []

for i in range(len(columns) - 1):
    start, end = (columns[i], columns[i + 1])
    column = [
        row[start:end - 1]
        for row in numbers_data
    ]
    numbers.append(column)

del columns
del operations_data
del numbers_data

# and then we flip
numbers = tuple(
    tuple(
        int(''.join(row[i][j] for i in range(len(row))))
        for j in range(len(row[0]))
    )
    for row in numbers
)

res = 0

for i in range(len(numbers)):
    row = numbers[i]
    if operations[i] == "+":
        res += sum(row)
    elif operations[i] == "*":
        res += reduce(lambda x, y: x * y, row)
    else:
        raise AssertionError

print(res)