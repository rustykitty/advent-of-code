"""
THIS SOLUTION DOES NOT WORK
"""

from collections import defaultdict
import functools
import itertools
from enum import StrEnum, auto

class Point2D:
    """A two-dimensional point"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return type(self) is type(other) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))
    
    def __iter__(self):
        return iter((self.x, self.y))

class GridSquare(StrEnum):
    EMPTY = "."
    RED = "#"
    GREEN = "X"

@functools.lru_cache
def calculate_area(p1: Point2D, p2: Point2D) -> int:
    return (abs(p1.x - p2.x) + 1) * (abs(p1.y - p2.y) + 1)

red_squares = tuple(
    Point2D(*map(int, line.split(",")))
    for line in open("9.in").read().rstrip().split("\n")
)

n = max(p.x for p in red_squares)
m = max(p.y for p in red_squares)

grid = defaultdict(lambda: GridSquare.EMPTY)

# grid = [
#     [GridSquare.EMPTY] * (m + 1) for _ in range(n + 1)
# ]

for p in red_squares:
    grid[(p.x, p.y)] = GridSquare.RED

green_squares = []

for (p1, p2) in itertools.zip_longest(red_squares, itertools.chain(red_squares[1:], [red_squares[0]])):
    if p1.x == p2.x and p1.y != p2.y:
        # (p1.x, p2.x) (i.e. p1.x < i < p2.x)
        if p1.y > p2.y:
            p1, p2 = p2, p1
        greens = (Point2D(p1.x, y) for y in range(p1.y + 1, p2.y))
    elif p1.y == p2.y and p1.x != p2.x:
        if p1.x > p2.x:
            p1, p2 = p2, p1
        greens = (Point2D(x, p1.y) for x in range(p1.x + 1, p2.x))
    else:
        raise AssertionError(f"{str(p1)} {str(p2)}")
    green_squares.extend(greens)

for p in green_squares:
    grid[(p.x, p.y)] = GridSquare.GREEN

del green_squares

def print_grid():
    print(f"n={n}, m={m}")

    for row in grid:
        print("".join(e.value for e in row))

# def flood(x, y):
#     if not (0 <= x < n and 0 <= y < m):
#         return

#     if grid[(x, y)] != GridSquare.EMPTY:
#         return

#     grid[(x, y)] = GridSquare.GREEN

#     flood(x - 1, y)
#     flood(x + 1, y)
#     flood(x, y - 1)
#     flood(x, y + 1)

# def flood(x, y):
#     s = []
#     s.append((x, y))
#     while s:
#         x, y = s.pop()
#         if (0 <= x < n and 0 <= y < m) and grid[(x, y)] == GridSquare.EMPTY:
#             grid[(x, y)] = GridSquare.GREEN
#             s.append((x - 1, y))
#             s.append((x + 1, y))
#             s.append((x, y - 1))
#             s.append((x, y + 1))
#     return
# flood(50000,48400)


def flood():
    # by_rows = defaultdict(defaultdict)
    # for ((x, y), v) in grid.items():
    #     by_rows[x][y] = v
    for i in range(n):
        inside = False
        for j in range(m):
            if grid[(i, j)] in (
                GridSquare.GREEN,
                GridSquare.RED
            ):
                inside = not inside
            if inside:
                grid[(i, j)] = GridSquare.GREEN

flood()

def all_good(p1: Point2D, p2: Point2D):
    x1, x2 = sorted((p1.x, p2.x))
    y1, y2 = sorted((p1.y, p2.y))
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if grid[(i, j)] not in (
                GridSquare.RED,
                GridSquare.GREEN
            ):
                return False
    return True

res = max(
    print(p1, p2, calculate_area(p1, p2)) or calculate_area(p1, p2)
    for (p1, p2) in itertools.product(red_squares, repeat=2)
    if all_good(p1, p2)
)
print(res)