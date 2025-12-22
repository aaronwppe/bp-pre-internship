# Prog. 26
# Write a function to check if the given tuple list has all k elements.

from typing import Any


def exists_in_tuple(input_tuple: tuple[Any], elements: list[Any]) -> bool:
    check_set = set(input_tuple)

    for element in elements:
        if element not in check_set:
            return False

    return True


if __name__ == "__main__":
    print(exists_in_tuple((1, 2, 3, 4, 4, 5, 6), [1, 2, 3, 4, 5]))
