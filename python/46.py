# Prog. 046
# Write a python function to determine whether all the numbers are different from each other are not.


def are_distinct(array: list[int]) -> bool:
    return len(set(array)) == len(array)


if __name__ == "__main__":
    print(are_distinct([1, 2, 3, 3]))
