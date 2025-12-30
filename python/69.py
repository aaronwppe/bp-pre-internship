# Prog. 069
# Write a function to check whether a list contains the given sublist or not.


from typing import Any


def sublist_exists(input_list: list[Any], sub_list: list[Any]) -> bool:
    if len(sub_list) > len(input_list):
        return False

    i = 0
    j = 0

    while i < len(input_list) and j < len(sub_list):
        if input_list[i] == sub_list[j]:
            i += 1
            j += 1

        else:
            i -= j + 1
            j = 0

    return j == len(sub_list)


if __name__ == "__main__":
    input_list = [7, 8, 1, 2, 1, 2, 3, 4, 5, 6, 7]
    print(sublist_exists(input_list, [1, 2, 3]))
