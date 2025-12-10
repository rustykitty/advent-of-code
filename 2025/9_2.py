import functools
import itertools

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

@functools.lru_cache
def calculate_area(p1: Point, p2: Point) -> int:
    return (abs(p1.x - p2.x) + 1) * (abs(p1.y - p2.y) + 1)

red_squares = tuple(
    Point(*map(int, line.split(",")))
    for line in open("9.in").read().rstrip().split("\n")
)

polygon = Polygon(red_squares)

res = 0

for (p1, p2) in itertools.product(red_squares, repeat=2):
    if p1 == p2:
        continue

    x1, x2 = sorted((p1.x, p2.x))
    y1, y2 = sorted((p1.y, p2.y))
    vertices = (
        (x1, y1), (x1, y2), (x2, y2), (x2, y1)
    )

    rectangle = Polygon(vertices)

    inside = polygon.contains(rectangle)

    # inside = all(
    #     polygon.contains(p) or polygon.touches(p) for p in (Point(v) for v in vertices)
    # )

    if inside:
        res = int(max(res, calculate_area(p1, p2)))

print(res)