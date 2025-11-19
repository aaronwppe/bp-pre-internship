# Prog. 966
# Write a function to remove an empty tuple from a list of tuples.

from typing import Any

def remove_empty_tuples(tuples: list[tuple[Any, ...]]) -> None:
    i = 0

    while i < len(tuples):
        if len(tuples[i]) == 0:
            tuples.pop(i)
        else:
            i += 1
        
    return


if __name__ == '__main__':
    list_of_tuples = [
        tuple(),
        tuple(),
        (1, 2, 3),
        tuple(),
    ]

    remove_empty_tuples(list_of_tuples)

    print(list_of_tuples)