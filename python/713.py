# Prog. 713
# Write a function to check if the given tuple contains all valid values or not.


from typing import Any

def validate(input_tuple: tuple[Any, ...], valid_elements: tuple[Any, ...]) -> bool:
    return len(set(input_tuple).difference(valid_elements)) == 0

if __name__ == "__main__":
    input_tuple = (1, 2, None, "this is a string")
    valid_elements = (1, "this is a string")

    print(validate(input_tuple, valid_elements))