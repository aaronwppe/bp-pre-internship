# Prog. 066
# Write a python function to count positive numbers in a list.


from typing import Any


def count_positive_nums(input_list: list[Any]) -> int:
    count = 0

    for element in input_list:
        if not (isinstance(element, int) or isinstance(element, float)):
            continue

        if element > 0:
            count += 1

    return count


if __name__ == "__main__":
    print(count_positive_nums([1, 2, 3, "any", -1, -2]))
