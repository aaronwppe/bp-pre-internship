# Prog. 001
# Write a function to find the minimum cost path to reach (m, n) from (0, 0)
# for the given cost matrix cost[][] and a position (m, n) in cost[][].

# References:
# - https://www.programiz.com/dsa/bellman-ford-algorithm

import math
from itertools import product

type Point = tuple[int, int]

ALL_MOVES = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
)


def get_min_cost_path(
    cost: list[list[int]],
    dest: Point,
    start_vertex: Point = (0, 0),
):
    rows = len(cost)
    cols = len(cost[0])
    vertices = rows * cols

    prev: dict[Point, Point] = dict()

    dist = [math.inf for _ in range(vertices)]

    start = (0, 0)
    start_vertex = get_vertex(start_vertex, cols)
    dist[start_vertex] = 0

    for _ in range(vertices - 1):
        if relax_vertices(cost, dist, prev) == False:
            break

    if negative_cycle_exists(cost, dist) or dest not in prev:
        return []

    path = []
    current_point = dest

    while current_point != start:
        path.append(current_point)
        current_point = prev[current_point]

    path.append(start)
    path.reverse()

    return path


def get_vertex(point: Point, cols: int) -> int:
    return (point[0] * cols) + point[1]


def relax_vertices(
    cost: list[list[int]],
    dist: list[int | float],
    prev: dict[Point, Point],
) -> bool:
    rows = len(cost)
    cols = len(cost[0])

    did_relax = False

    for r, c in product(range(rows), range(cols)):
        from_point = (r, c)
        from_vertex = get_vertex(from_point, cols)

        for move in ALL_MOVES:
            new_r = r + move[0]
            new_c = c + move[1]
            to_point = (new_r, new_c)
            to_vertex = get_vertex(to_point, cols)

            if dist[from_vertex] == math.inf:
                continue

            if not (0 <= new_r < rows and 0 <= new_c < cols):
                continue

            new_dist = dist[from_vertex] + cost[new_r][new_c]

            if new_dist >= dist[to_vertex]:
                continue

            dist[to_vertex] = new_dist
            prev[to_point] = from_point
            did_relax = True

    return did_relax


def negative_cycle_exists(cost: list[list[int]], dist: list[int | float]) -> bool:
    rows = len(cost)
    cols = len(cost[0])

    for r, c in product(range(rows), range(cols)):
        from_vertex = get_vertex((r, c), cols)

        for move in ALL_MOVES:
            new_r = r + move[0]
            new_c = c + move[1]
            to_vertex = get_vertex((new_r, new_c), cols)

            if not (0 <= new_r < rows and 0 <= new_c < cols):
                continue

            if dist[from_vertex] + cost[new_r][new_c] < dist[to_vertex]:
                return True

    return False


if __name__ == "__main__":
    cost_matrix = [
        [1, 100, 1],
        [25, 1, 1],
    ]

    print(get_min_cost_path(cost_matrix, (0, 2)))
