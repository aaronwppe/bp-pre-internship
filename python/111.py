# Prog. 111
# Write a function to find common elements in given nested lists.

from typing import Any
from collections import Counter

def get_common_elements(nested_list: list[list[Any]]) -> list[Any]:
    if not nested_list:
        return []
    
    counters = [Counter(li) for li in nested_list]

    common_elements = []

    for element, freq in counters[0].items():
        flag = True

        for counter in counters[1:]:
            if counter.get(element, 0) != freq:
                flag = False
        
        if flag == True:
            common_elements.extend([element] * freq)

    return common_elements


if __name__ == '__main__':
    nested_list = [
        [1, 1, 2, 3],
        [1, 1, 2],
        [1, 1, 3]
    ]

    print(get_common_elements(nested_list))