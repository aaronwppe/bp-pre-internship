# Prog. 054
# Write a function to sort the given array by using counting sort.

# References:
# - https://www.youtube.com/watch?v=OKd534EWcdk


from collections import Counter
import math


def counting_sort(array: list[int]) -> None:
    if len(array) <= 1:
        return None

    min_element, max_element = get_min_max_elements(array)
    if min_element == max_element or min_element is None or max_element is None:
        return None

    idx_offset = min_element

    counter = Counter(array)

    start_idx_list = [
        counter.get(element, 0) for element in range(min_element, max_element + 1)
    ]

    cummulative_sum = 0
    for i in range(len(start_idx_list)):
        cummulative_sum += start_idx_list[i]
        start_idx_list[i] = cummulative_sum

    prev_start_idx = start_idx_list[-1]

    for i in range(len(start_idx_list) - 2, -1, -1):
        start_idx = start_idx_list[i]

        if start_idx == prev_start_idx:
            continue

        element = idx_offset + i + 1
        array[start_idx:prev_start_idx] = [element] * (prev_start_idx - start_idx)
        prev_start_idx = start_idx

    array[0:prev_start_idx] = [min_element] * prev_start_idx

    return None


def get_min_max_elements(array: list[int]) -> tuple[int | None, int | None]:
    min_element = math.inf
    max_element = -math.inf

    for element in array:
        if element < min_element:
            min_element = element

        if element > max_element:
            max_element = element

    if min_element == math.inf:
        min_element = None

    if max_element == -math.inf:
        max_element = None

    return (min_element, max_element)


if __name__ == "__main__":
    elements = [1, 0, 3, 1, 3, 1, -1, -1]
    counting_sort(elements)
    print(elements)


# 0 - 3
# 0 1 2 3
# 0 1 2 3
# diff = 0 (num - idx)

# 1 - 4
# 1 2 3 4
# 0 1 2 3
# diff = 1

# -2 - 1
# -2 -1 0 1
# 0 1 2 3
# diff = -2

# num = diff + idx
