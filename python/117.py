# Prog. 117
# Write a function to convert all possible convertible elements in the list to float.

from typing import Any


def transform_nums_to_float(input_list: list[Any]) -> list[Any]:
    ret_list = []

    for element in input_list:
        try:
            transformed_value = float(element)

        except ValueError:
            transformed_value = element

        ret_list.append(transformed_value)

    return ret_list


if __name__ == "__main__":
    input_list = ["1.2", "pop", 1.2, 1]

    print(transform_nums_to_float(input_list))
