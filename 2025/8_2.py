import math
import itertools

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

paths = sorted(
    ((a, b) for (a, b) in itertools.product(nodes, repeat=2) if a != b),
    key=(lambda a: calculate_distance(*a[0], *a[1]))
)

nodes = set(path[0] for path in paths) | set(path[1] for path in paths)

networks = set(
    frozenset(
        [node]
    )
    for node in nodes
)

res = 0

for p1, p2 in paths:
    if len(networks) == 1:
        break

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

    if p1_network != p2_network:
        networks.remove(p1_network)
        networks.remove(p2_network)
        networks.add(p1_network | p2_network)
    res = p1[0] * p2[0]

print(res)
