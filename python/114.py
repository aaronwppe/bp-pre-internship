# Prog. 114
# Write a function to assign frequency to each tuple in the given tuple list.

from typing import Any
from collections import Counter

def get_freq(tuples: list[tuple[Any, ...]]) -> dict[tuple[Any, ...], int]:
    return dict(Counter(tuples))


if __name__ == '__main__':
    input_tuples = [
        (1, 2),
        (2, 4),
        (1, 2),
    ]
    print(get_freq(input_tuples))