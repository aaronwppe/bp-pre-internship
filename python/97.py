# Prog. 097
# Write a function to find frequency count of list of lists.

from typing import Any

def get_frequency(lists: list[list[Any]]) -> list[int]:
    if not lists:
        return []
    
    freq_list = [0] * len(lists)
    counted_indexes = set()
    i = 0

    while i < len(lists):
        if i in counted_indexes:
            i += 1
            continue

        j = i + 1
        count = 1
        similar_lists = {i}

        while j < len(lists):
            if lists[i] == lists[j]:
                similar_lists.add(j)
                count += 1

            j += 1

        for k in similar_lists:
            freq_list[k] = count

        counted_indexes.update(similar_lists)
        i += 1

    return freq_list


if __name__ == '__main__':
    lists = [
        [1, 2, 3],
        [1, 2, 3],
        [2, 3]
    ]

    print(get_frequency(lists))