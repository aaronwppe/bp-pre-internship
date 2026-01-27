# Prog. 119
# Write a python function to find the element that appears only once in a sorted array.

import unittest


class TestAppearsOnce(unittest.TestCase):
    def test_positive_case(self):
        params = (
            ([1, 2, 3, 4, 5], 3),
            ([1, 2, 3, 4, 5], 1),
            ([1, 2, 3, 4, 5], 5),
        )

        for array, element in params:
            self.assertTrue(appears_once(array, element))

    def test_negative_cases(self):
        params = (
            ([1, 2, 3, 4, 5], 0),
            ([1, 2, 3, 3, 4, 5], 3),
            ([1, 2, 3, 4, 5, 5], 5),
            ([], 2),
        )

        for array, element in params:
            self.assertFalse(appears_once(array, element))


def _get_index(array: list[int], element: int) -> int | None:
    low = 0
    high = len(array)

    while low < high:
        mid = (low + high) // 2

        if array[mid] < element:
            low = mid + 1
        elif array[mid] > element:
            high = mid
        else:
            return mid

    return None


def appears_once(array: list[int], element: int) -> bool:
    index = _get_index(array, element)
    if index is None:
        return False

    lower_index = index - 1
    if lower_index >= 0 and array[lower_index] == element:
        return False

    higher_index = index + 1
    if higher_index < len(array) and array[higher_index] == element:
        return False

    return True


if __name__ == "__main__":
    unittest.main()
