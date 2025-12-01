from sys import stdin

i1, i2 = stdin.read().rstrip().split('\n\n')

rules = [tuple(int(i) for i in x.split('|')) for x in i1.split('\n')]

pages = [list(int(i) for i in x.split(',')) for x in i2.split('\n')]

def evaluate_rules(pages):
    global rules
    for i, j in rules:
        if i in pages and j in pages:
            if pages.index(i) > pages.index(j):
                return False
    return True

incorrect_pages = filter(lambda x: not evaluate_rules(x), pages)

result = 0

for i in incorrect_pages:
    while not evaluate_rules(i):
        for j, k in rules:
            if j in i and k in i:
                if i.index(j) > i.index(k):
                    i[i.index(j)], i[i.index(k)] = i[i.index(k)], i[i.index(j)]
    result += i[len(i) // 2]

print(result)
