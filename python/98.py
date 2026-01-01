#  Prog. 098
# Write a function to multiply all the numbers in a list and divide with the length of the list.

from typing import Any

def multiply_and_divide_list(input_list: list[Any]) -> float | None:
    if len(input_list) == 0:
        return None
    
    res = 1
    num_exists = False

    for e in input_list:
        if not(isinstance(e, int) or isinstance(e, float)):
            continue
        
        num_exists = True
        res *= e

    if num_exists == False:
        return None

    return res / len(input_list)


if __name__ == '__main__':
    print(multiply_and_divide_list([1, 2, 3]))
