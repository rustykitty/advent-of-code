banks = tuple(
    tuple(
        int(x) for x in bank
    )
    for bank in open("3.in").read().strip().split("\n")
)

res = 0

for bank in banks:
    first = max(enumerate(bank[:-1]), key=lambda x: x[1])
    second = max(enumerate(bank[first[0]+1:]), key=lambda x: x[1])

    res += int(f"{first[1]}{second[1]}")

print(res)