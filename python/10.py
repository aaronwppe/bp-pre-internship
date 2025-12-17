# Prog. 010
# Write a function to get the n smallest items from a dataset.


from typing import Any


def get_smallest(data_set: set[int], n: int) -> list[Any]:
    if n <= 0:
        return []

    len_diff = n - len(data_set)

    if len_diff >= 0:
        return list(data_set) + [None for _ in range(len_diff)]

    data_iter = iter(data_set)
    min_elements = [next(data_iter) for _ in range(n)]
    min_elements.sort()

    while True:
        element = next(data_iter, None)
        if element is None:
            break

        _swap_with_greater_element(min_elements, element)

    return min_elements


def _swap_with_greater_element(input_list: list[int], element: int) -> None:
    for i in range(len(input_list)):
        if element < input_list[i]:
            input_list.pop()
            input_list.insert(i + 1)


if __name__ == "__main__":
    data_set = {3, 4, 1, 2, 8}
    print(get_smallest(data_set, 2))
