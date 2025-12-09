import math

def calculate_distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt(
        abs(x1 - x2) ** 2 +
        abs(y1 - y2) ** 2 +
        abs(z1 - z2) ** 2
    )

nodes = (
    tuple(map(int, line.split(","))) for line in 
    open("8.in").read().rstrip().split("\n")
)

n = 1000

# Find n shortest distances
# Adapted from https://stackoverflow.com/questions/73035944/best-way-to-retrieve-k-largest-elements-from-large-unsorted-arrays
import heapq
import itertools
import functools

paths = heapq.nsmallest(
    n * 2, 
    ((a, b) for (a, b) in itertools.product(nodes, repeat=2) if a != b),
    key=(lambda a: calculate_distance(*a[0], *a[1])))

paths = set(
    tuple(sorted(path)) for path in paths
)

nodes = set(path[0] for path in paths) | set(path[1] for path in paths)

networks = set(
    frozenset(
        [node]
    )
    for node in nodes
)

for p1, p2 in paths:
    p1_network = next(
        (
            network for network in networks
            if p1 in network
        ),
        None
    )
    p2_network = next(
        (
            network for network in networks
            if p2 in network
        ),
        None
    )
    assert p1_network is not None
    assert p2_network is not None

    networks.remove(p1_network)
    if p1_network != p2_network:
        networks.remove(p2_network)
    networks.add(p1_network | p2_network)

three_largest = heapq.nlargest(
    3,
    (len(network) for network in networks)
)

res = functools.reduce(lambda x, y: x * y, three_largest)

print(res)
