# Prog. 22
# Write a function to find the first duplicate element in a given array of integers.


def find_first_duplicate(array: list[int]) -> int | None:
    distinct_array = set()

    for num in array:
        if num in distinct_array:
            return num

        distinct_array.add(num)

    return None


if __name__ == "__main__":
    print(find_first_duplicate([1, 2, 2, 3, 9]))
