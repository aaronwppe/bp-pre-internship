# Prog. 42
# Write a python function to find the sum of repeated elements in a given array.


def sum_of_duplicates(array: list[int]) -> int:
    traversed = dict()

    for element in array:
        if element not in traversed:
            traversed[element] = 0
        else:
            traversed[element] = element

    return sum(traversed.values())


if __name__ == "__main__":
    print(sum_of_duplicates([1, 2, 3, 4, 1, 1, 2]))
