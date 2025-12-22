# Prog. 19
# Write a function to find whether a given array of integers contains any duplicate element.


def contains_duplicates(array: list[int]) -> bool:
    array_set = set()

    for element in array:
        if element in array_set:
            return True

        array_set.add(element)

    return False


if __name__ == "__main__":
    array = [1, 2, 3, 3]
    print(contains_duplicates(array))
