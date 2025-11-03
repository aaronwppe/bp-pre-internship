# Prog. 049
# Write a function to extract every first or specified element from a given two-dimensional list.

from typing import Any

def extract(lists: list[list[Any]], element: Any = None) -> list[Any]:
    if element is None:
        return [
            curr_list[0] if curr_list else None
            for curr_list in lists
        ]
    
    return [
        element if element in curr_list else None
        for curr_list in lists
    ]


if __name__ == "__main__":
    two_d_list = [
        [],
        [0, 1],
        [1],
        ['POP', 3, -1]
    ]

    extracted_list = extract(two_d_list)
    print(extracted_list)