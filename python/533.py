# Prog. 533
# Write a function to remove particular data type elements from the given tuple.


from typing import Any

def remove_type(input_tuple: tuple[Any, ...], data_type: type) -> tuple[Any, ...]:
    return tuple([
        element
        for element in input_tuple
        if type(element) is not data_type 
    ])

if __name__ == "__main__":
    my_tuple = (1, "str", 0.2, 1)
    
    print(remove_type(my_tuple, float))