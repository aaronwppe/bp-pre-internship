# Prog. 29
# Write a python function to find the element occurring odd number of times.

from typing import Any


def get_odd_occurring_elements(input_list: list[Any]) -> list[Any]:
    occurrences = dict()

    for element in input_list:
        if element not in occurrences:
            occurrences[element] = 1
        else:
            occurrences[element] += occurrences[element]

    return [element for element, occ in occurrences.items() if occ % 2 != 0]


if __name__ == "__main__":
    print(get_odd_occurring_elements([1, 2, "st", 2, "st"]))
