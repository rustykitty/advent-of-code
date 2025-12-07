data = open("7.in").read().rstrip().split("\n")
s = data[0].index("S")
n = len(data)
m = len(data[0])
beams = [s]
pos = 1

res = 0

while pos < n:
    beams_new = set()
    for beam in beams:
        if data[pos][beam] == "^":
            res += 1
            beams_new.add(beam - 1)
            beams_new.add(beam + 1)
        else:
            beams_new.add(beam)
    beams = [
        beam for beam in beams_new
        if 0 <= beam <= m
    ]

    pos += 1

print(res)