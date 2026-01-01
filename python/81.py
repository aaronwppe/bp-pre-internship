# Prog. 081
# Write a function to zip the two given tuples.

from typing import Any

def zip_tuples(tuple_1: tuple[Any, ...], tuple_2: tuple[Any, ...]) -> list[tuple[Any, Any]]:
    return list(zip(tuple_1, tuple_2))


if __name__ == '__main__':
    tuple_1 = (1, 2, 3, 4)
    tuple_2 = (5, 6, 7)

    print(zip_tuples(tuple_1, tuple_2))