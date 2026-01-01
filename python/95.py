# Prog. 095
# Write a python function to find the minimum length of sublist.

from typing import Any

def min_list_len(lists: list[list[Any]]) -> int | None:
    if not lists:
        return None
    
    min_list = min(lists, key=lambda l: len(l))
    return len(min_list)


if __name__ == '__main__':
    lists = [
        [1, 2, 3],
        [5, 6],
        [99]
    ]

    print(min_list_len(lists))
    