# Prog. 622
# Write a function to find the median of two sorted arrays of same size.

# References:
# - 597.py (kth element of 2 sorted arrays)

from math import inf
from typing import Any


# utility function
def _get_element(array: list[int], index: int, default: Any) -> Any:
    return array[index] if index >= 0 and index < len(array) else default


def median_of_sorted_arrays(array_1: list[int], array_2: list[int]) -> float | None:
    if len(array_1) == 0 or len(array_1) != len(array_2):
        return None

    k = len(array_1) - 1
    low = 0
    high = len(array_1)

    while low < high:
        mid_1 = (low + high) // 2
        mid_2 = k - mid_1 - 1

        l1 = _get_element(array_1, mid_1, -inf)
        r1 = _get_element(array_1, mid_1 + 1, inf)

        l2 = _get_element(array_2, mid_2, -inf)
        r2 = _get_element(array_2, mid_2 + 1, inf)

        if l1 > r2:
            high = mid_1

        elif l2 > r1:
            low = mid_1 + 1

        else:
            return (max(l1, l2) + min(r1, r2)) / 2

    return (array_1[0] + array_2[k]) / 2


if __name__ == "__main__":
    print(median_of_sorted_arrays(array_1=[5, 8, 9, 10], array_2=[1, 2, 6, 7]))


# ==============================
# 1, 2, 5, |6, 7,| 8, 9, 10

# k = 4 (higher mid)

# i = 1
# low = 0, high = 4
# mid_1 = 2, mid_2 = 1

# 5, 8, 9, | 10
# 1, 2, | 6, 7

# i = 2
# low = 0, high = 2
# mid_1 = 1, mid_2 = 2
#
# 5, 8, | 9, 10
# 1, 2, 6, | 7

# i = 3
# low = 0, high = 1
# mid_1 = 0, mid_2 = 3
#
# 5, | 8, 9, 10
# 1, 2, 6, 7 |

# =========================

# 5, 8, 9, 10
# 1, 2, 6, 7
# 1, 2, 5, | 6, 7,| 8, 9, 10

# k = 3 (lower mid)

# i = 1
# low = 0, high = 4
# mid_1 = 2, mid_2 = 0
#
# 5, 8, 9, | 10
# 1, | 2, 6, 7

# i = 2
# low = 0, high = 2
# mid_1 = 1, mid_2 = 1
#
# 5, 8, | 9, 10
# 1, 2, | 6, 7

# i = 3
# low = 0, high = 1
# mid_1 = 0, mid_2 = 2
#
# 5, | 8, 9, 10
# 1, 2, 6, | 7
