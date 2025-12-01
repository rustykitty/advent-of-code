import sys

safe_reports = 0

def is_going(arr, up):
    condition = (lambda x, y: x < y) if up else (lambda x, y: x > y)
    for i in range(len(arr) - 1):
        if condition(arr[i], arr[i + 1]):
            pass
        else:
            return False
    return True

def in_bounds(arr):
    for i in range(len(arr) - 1):
        if 1 <= abs(arr[i] - arr[i + 1]) <= 3:
            pass
        else:
            return False
    return True


is_safe = lambda x: is_going(x, (x[1] - x[0]) > 0) and in_bounds(x)

while (line := sys.stdin.readline()):
    if (line == '\n'): break
    report = [int(level) for level in line[:-1].split(' ')]
    if is_safe(report):
        safe_reports += 1
    else: # remove this line to line 36 to get part 1
        for i in range(len(report)):
            if is_safe(report[:i] + report[i + 1:]):
                safe_reports += 1
                break

print(safe_reports)
