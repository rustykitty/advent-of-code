import itertools

class Point2D:
    """A two-dimensional point"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

def calculate_area(p1: Point2D, p2: Point2D) -> int:
    return (abs(p1.x - p2.x) + 1) * (abs(p1.y - p2.y) + 1)

points = tuple(
    Point2D(*map(int, line.split(",")))
    for line in open("9.in").read().rstrip().split("\n")
)

res = max(calculate_area(p1, p2) for (p1, p2) in itertools.product(points, repeat=2))

print(res)
