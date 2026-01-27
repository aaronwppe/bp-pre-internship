# Prog. 115
# Write a function to check whether all dictionaries in a list are empty or not.

from typing import Any

def all_dict_empty(input_list: list[Any]) -> bool:
    for element in input_list:
        if isinstance(element, dict) and len(element) != 0:
            return False
        
    return True


if __name__ == '__main__':
    input_list = [
        (1, 2, 3),
        dict(),
        dict(),
    ]

    print(all_dict_empty(input_list))
