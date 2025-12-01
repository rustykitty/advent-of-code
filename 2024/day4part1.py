import sys

wordSearch = sys.stdin.read().rstrip().split('\n')

matches = 0

match_str = 'XMAS'

# horizontal matches
def match_horizontal(s):
    global matches
    for i in wordSearch:
        for j in range(len(wordSearch[0]) - 3):
            if i[j:j+4] == s:
                matches += 1
match_horizontal(match_str)
match_horizontal(match_str[::-1])
# vertical matches
def match_vertical(s):
    global matches
    for i in range(len(wordSearch)):
        for j in range(len(wordSearch[0]) - 3):
            if ''.join(x[i] for x in wordSearch[j:j+4]) == s:
                matches += 1
match_vertical(match_str)
match_vertical(match_str[::-1])
# diagonal matches
def match_diagonal(s):
    global matches
    for i in range(len(wordSearch) - 3): # we have to do 3 for some reason instead of 
        for j in range(len(wordSearch[0]) - 3): # 4, idk why but that's just how it is
            diagonal_str = ''.join(wordSearch[i + x][j + x] for x in range(4))
            if diagonal_str == s:
                matches += 1
def match_backward_diagonal(s):
    global matches
    for i in range(len(wordSearch) - 3):
        for j in range(3, len(wordSearch[0])):
            diagonal_str = ''.join(wordSearch[i + x][j - x] for x in range(4))
            if diagonal_str == s:
                matches += 1
match_diagonal(match_str)
match_diagonal(match_str[::-1])
match_backward_diagonal(match_str)
match_backward_diagonal(match_str[::-1])

print(matches)
