# Prog. 075
# Write a function to find tuples which have all elements divisible by k from the given list of tuples.

from typing import Any


def get_tuples(tuples: list[tuple[Any, ...]], divisible_by: int) -> list[tuple[Any, ...]]:
    is_divisible = False
    ret_list = []

    for t in tuples:
        is_divisible = True

        for e in t:
            if e % divisible_by != 0:
                is_divisible = False
                break
            
        if is_divisible:
            ret_list.append(t)

    return ret_list


if __name__ == '__main__':
    input_list = [
        (1, 2, 3),
        (2, 4, 6),
        (6, 8),
    ]

    print(get_tuples(input_list, 2))