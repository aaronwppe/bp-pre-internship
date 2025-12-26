# Prog. 040
# Write a function to find frequency of the elements in a given list of lists using collections module.


from typing import Any
from collections import Counter


def get_frequency_dict(input_list: list[list[Any]]) -> dict[Any, int]:
    counter = Counter()

    for li in input_list:
        counter.update(li)

    return dict(counter)


if __name__ == "__main__":
    lists = [
        [1, 2, 3, "hi"],
        ["hi", 1],
    ]

    print(get_frequency_dict(lists))
