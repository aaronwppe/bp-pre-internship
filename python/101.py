# Prog. 101
# Write a function to find the kth element in the given array.

from typing import Any

def get_kth_element(array: list[Any], k: int) -> Any | None:
    if len(array) <= k or k < -len(array):
        return None
    
    return array[k]

if __name__ == '__main__':
    print(get_kth_element([1, 2, 3], 0))
