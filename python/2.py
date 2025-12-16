# Prog. 002
# Write a function to find the similar elements from the given two tuple lists.

from typing import Any


def get_similar(
    first_list: list[tuple[Any, ...]], second_list: list[tuple[Any, ...]]
) -> list[tuple[Any, ...]]:
    return [
        tuple_1
        for tuple_1 in first_list
        for tuple_2 in second_list
        if is_similar(tuple_1, tuple_2)
    ]


def is_similar(first_tuple: tuple[Any], second_tuple: tuple[Any]) -> bool:
    if len(first_tuple) != len(second_tuple):
        return False

    for i, j in zip(first_tuple, second_tuple):
        if i != j:
            return False

    return True


if __name__ == "__main__":
    print(get_similar(first_list=[(1, 2), ("")], second_list=["hello", (1, 2)]))
