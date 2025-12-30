# Prog. 070
# Write a function to find whether all the given tuples have equal length or not.

from typing import Any


def are_of_equal_length(tuples: list[tuple[Any, ...]]) -> bool:
    if not tuples:
        return True

    tup_len = len(tuples[0])

    for tup in tuples[1:]:
        if len(tup) != tup_len:
            return False

    return True


if __name__ == "__main__":
    tuples = [
        (1, 2, 3),
        ("a", "b", 1),
    ]

    print(are_of_equal_length(tuples))
