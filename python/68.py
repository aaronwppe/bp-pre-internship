# Prog. 068
# Write a python function to check whether the given array is monotonic or not.

#  monotonic means either the array is in increasing order or in decreasing order


def is_monotonic(array: list[int | float]) -> bool:
    if len(array) < 2:
        return False

    i = 1
    is_increasing = None

    for i in range(i, len(array)):
        prev = array[i - 1]
        curr = array[i]

        if prev != curr:
            is_increasing = True if prev < curr else False
            break

    if is_increasing is None:
        return False

    for i in range(i, len(array)):
        prev = array[i - 1]
        curr = array[i]

        if (is_increasing == True and prev > curr) or (is_increasing == False and prev < curr):
            return False

    return True


if __name__ == "__main__":
    array = [0, 0, 0, 1, 2, 3, 3, 3, 4]
    print(is_monotonic(array))
