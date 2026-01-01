# Prog. 094
# Write a function to extract the index minimum value record from the given tuples.

from typing import Any
import math


# throws index error if tuple index out of range 
def get_min_value_record(records: list[tuple[Any]], compare_idx: int) -> int | None:
    if not records:
        return None
    
    min_record_idx = 0

    for i in range(1, len(records)):
        if records[i][compare_idx] < records[min_record_idx][compare_idx]:
            min_record_idx = i

    return min_record_idx


if __name__ == '__main__':
    records = [
        (1, 2),
        (3, 4),
        (5, 1),
    ]

    index = get_min_value_record(records, 1)
    if index is not None:
        print(records[index])
        