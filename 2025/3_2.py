banks = tuple(
    tuple(
        int(x) for x in bank
    )
    for bank in open("3.in").read().split("\n")
)

res = 0

def maxNum(digits, k):
    n = len(digits)
    start = 0
    res = 0
    for i in range(k):
        res *= 10
        this = max(enumerate(digits[start:n-(k-i)+1]), key=lambda x: x[1])
        start = this[0] + start + 1
        res += this[1]
    return res

for bank in banks:
    res += maxNum(bank, 12)

print(res)
