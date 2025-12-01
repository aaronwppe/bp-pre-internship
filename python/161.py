# Prog. 161
# Write a function to remove all elements from a given list present in another list.

from typing import Any


def remove_values(array: list[Any], target_values: list[Any]) -> None:
    if len(array) == 0 or len(target_values) == 0:
        return

    targets_set = set(target_values)
    i = 0

    while i < len(array):
        if array[i] in targets_set:
            array.pop(i)
        else:
            i += 1


if __name__ == "__main__":
    my_list = [1, 2, "hello", None, 2.0, None]
    remove_values(my_list, [1, None])
    print(my_list)
