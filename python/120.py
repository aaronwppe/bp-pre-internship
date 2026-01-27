# Prog. 120
# Write a function to find the maximum product from the pairs of tuples within a given list.

import unittest


class TestMaximumProduct(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            maximum_product(
                [
                    (1, 2),
                    (5, 3),
                    (10, 4),
                ]
            ),
            40,
        )

    def test_case_2(self):
        self.assertEqual(maximum_product([]), None)


def maximum_product(array: list[tuple[int, int]]) -> int | None:
    if not array:
        return None

    num_1, num_2 = max(array, key=lambda t: t[0] * t[1])
    return num_1 * num_2


if __name__ == "__main__":
    unittest.main()
