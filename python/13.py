# Prog. 013
# Write a function to count the most common words in a dictionary.

import heapq


def most_common_words(occ_dict: dict[str, int], n: int = 1) -> list[str]:
    if n == 0:
        return []

    comparision_value_callback = lambda word: occ_dict[word]

    if n < 0:
        return heapq.nsmallest(abs(n), occ_dict, comparision_value_callback)

    return heapq.nlargest(n, occ_dict, comparision_value_callback)


if __name__ == "__main__":
    occ_dict = {
        "word": 5,
        "value": 2,
        "pencil": 1,
        "big": 70,
    }

    print(most_common_words(occ_dict, 2))
