import re
import sys
expr = re.compile(r"mul\((\d+),(\d+)\)")

data = sys.stdin.read()

res = 0

enabled = True

for match in expr.finditer(data):
    if enabled:
        res += int(match.group(1)) * int(match.group(2))

print(res)
