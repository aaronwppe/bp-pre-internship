# Prog. 062
# Write a python function to find smallest number in a list.


def min_element(array: list[int | float]) -> int | float | None:
    if len(array) == 0:
        return None

    min = array[0]
    if len(array) == 1:
        return min

    for element in array[1:]:
        if element < min:
            min = element

    return min


if __name__ == __name__:
    print(min_element([1, 2, 3, -0.5]))
