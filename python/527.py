# Prog. 527
# Write a function to find all pairs in an integer array whose sum is equal to a given number.

# References:
# - https://www.geeksforgeeks.org/dsa/check-if-pair-with-given-sum-exists-in-array/


def get_pairs(array: list[int], equal_to: int) -> list[tuple[int, int]]:
    array_len = len(array)

    return [
        (array[i], array[j])
        for i in range(array_len)
        for j in range(i + 1, array_len)
        if (array[i] + array[j]) == equal_to
    ]

# Solution from 'Geeks for Geeks'
def get_pairs_using_sets(array: list[int], equal_to: int) -> list[tuple[int, int]]:
    if len(array) < 2:
        return []
    
    traversed = {array[0]}
    pairs = list()

    for element in array[1:]:
        complement = equal_to - element

        if complement in traversed:
            pairs.append((complement, element))

        traversed.add(element)
    
    return pairs


if __name__ == "__main__":
    array = [24, 10, 12, 12, 4, 14]
    target = 24

    print(get_pairs_using_sets(array, target))
