# Prog. 121
# Write a function to find the triplet with sum of the given array

import unittest


class TestTripletSum(unittest.TestCase):
    def test_case_false(self):
        self.assertFalse(triplet_sum([1], 10))
        self.assertFalse(triplet_sum([], 0))
        self.assertFalse(triplet_sum([1, 2], 5))
        self.assertFalse(triplet_sum([1, 2, 3], 3))

    def test_case_success(self):
        self.assertTrue(triplet_sum([1, 2, 3], 6))
        self.assertTrue(triplet_sum([25, 2, 16, 2, -1, -1, 5], 0))


def triplet_sum(array: list[int], target_sum: int) -> bool:
    if len(array) < 3:
        return False

    array = sorted(array)

    for i in range(len(array) - 2):
        low = i + 1
        high = len(array) - 1

        remaining_target = target_sum - array[i]

        while low < high:
            current_sum = array[low] + array[high]
            if current_sum == remaining_target:
                return True

            if current_sum > remaining_target:
                high -= 1
            else:
                low += 1

    return False


if __name__ == "__main__":
    unittest.main()
