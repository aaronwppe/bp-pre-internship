# Prog. 105,
# Write a python function to count true booleans in the given list.

from typing import Any

def count_true_booleans(array: list[Any]) -> int:
    count = 0

    for element in array:
        if isinstance(element, bool) and element:
            count += 1

    return count


if __name__ == '__main__':
    print(count_true_booleans([1, 2, True, True, False]))