# Prog. 062
# Write a python function to find smallest number in a list.

from typing import Any
import math


def get_smallest_num(input_list: list[Any]) -> Any:
    min_element = math.inf

    for element in input_list:
        if not (isinstance(element, int) or isinstance(element, float)):
            continue

        if min_element > element:
            min_element = element

    if min_element == math.inf:
        min_element = None

    return min_element


if __name__ == "__main__":
    print(get_smallest_num(["a", "a", 1, 9, 0.3]))
