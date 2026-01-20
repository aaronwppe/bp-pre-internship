# Prog. 108
# Write a function to merge multiple sorted inputs into a single sorted iterator using heap queue algorithm.

from typing import Any, Iterator
import heapq

def merge_sorted(*lists: list[list[Any]], reverse: bool = False) -> Iterator:
    return iter(heapq.merge(*lists, reverse=reverse))

if __name__ == '__main__':
    sorted_lists = [
        [4, 5, 6],
        [10, 11, 12],
        [1, 2, 3],
    ]

    print([i for i in merge_sorted(*sorted_lists)])