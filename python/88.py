# Prog. 088
# Write a function to get the frequency of the elements in a list.

from collections import Counter


def get_frequencies(elements: list) -> dict:
    return dict(Counter(elements))

if __name__ == '__main__':
    elements = [1, 2, 3, 4, 5, 1, 1, 2, 2]
    print(get_frequencies(elements))