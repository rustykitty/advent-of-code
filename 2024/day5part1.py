from sys import stdin

from typing import *

i1, i2 = stdin.read().rstrip().split('\n\n')

rules = [tuple(int(i) for i in x.split('|')) for x in i1.split('\n')]

pages = (tuple(int(i) for i in x.split(',')) for x in i2.split('\n'))

def evaluate_rules(pages):
    global rules
    for i, j in rules:
        if i in pages and j in pages:
            if pages.index(i) > pages.index(j):
                return False
    return True

correct_pages = filter(evaluate_rules, pages)

result = 0

for i in correct_pages:
    result += i[len(i) // 2]

print(result)
