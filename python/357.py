# Prog. 357
# Write a function to find the maximum element of all the given tuple records.


from typing import Any

def max_element(tuples: list[tuple[Any, ...]]) -> Any | None:
    max = None
    
    for tup in tuples:
        if tup:
            max = tup[0]
            break
    
    if max is None:
        return None

    for tup in tuples:
        for element in tup:
            if element > max:
                max = element
        
    return max

if __name__ == "__main__":
    records = [
        (),
        (1, 3),
        (4,)
    ]

    print(max_element(records))