# Prog. 262
# Write a function to split a given list into two parts where the length of the first part of the list is given.

from typing import Any


def split_list(input_list: list[Any], split_len: int) -> tuple[list[Any], list[Any]]:
    # interpreting a -ve split_len as the number of elements to exclude from the first list
    if split_len < 0:
        split_len = max(split_len + len(input_list), 0)

    return (input_list[:split_len], input_list[split_len:])


if __name__ == "__main__":
    list_1 = [1, 2, 3, 4, 5, 6]

    print(split_list(list_1, 2))
    print(split_list(list_1, -1))
