import sys

s = sys.stdin.read().rstrip().split('\n')

matches = 0

for i in range(1, len(s) - 1):
    for j in range(1, len(s[0]) - 1):
        if s[i][j] == 'A':
            forward_match = (s[i-1][j-1] == 'M' and s[i+1][j+1] == 'S') or \
                            (s[i-1][j-1] == 'S' and s[i+1][j+1] == 'M')
            backward_match = (s[i+1][j-1] == 'M' and s[i-1][j+1] == 'S') or \
                             (s[i+1][j-1] == 'S' and s[i-1][j+1] == 'M')
            if forward_match and backward_match:
                matches += 1

print(matches)
