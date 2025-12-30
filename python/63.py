# Prog. 063
# Write a function to find the maximum difference between available pairs in the given tuple list.

import math


def get_max_diff(tuple_list: list[tuple[int, int]]) -> int | None:
    max_diff = -math.inf

    for i, j in tuple_list:
        d = j - i

        if max_diff < d:
            max_diff = d

    if max_diff == -math.inf:
        max_diff = None

    return max_diff


if __name__ == "__main__":
    input_list = [
        (1, 2),
        (13, 20),
        (2, 2),
    ]

    print(get_max_diff(input_list))
