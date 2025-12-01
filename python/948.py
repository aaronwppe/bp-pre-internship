# Prog. 948
# Write a function to get an item of a tuple.

from typing import Any


def get_by_index(input_tuple: tuple[Any, ...], index: int) -> Any:
    if index < 0 or index >= len(input_tuple):
        return None

    return input_tuple[index]


if __name__ == "__main__":
    print(get_by_index((1, 2, 3), 3))
