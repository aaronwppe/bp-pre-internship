# Prog. 034
# Write a python function to find the missing number in a sorted array.


# assumes nums contains distinct ints
def get_missing_num(nums: list[int]) -> int | None:
    if len(nums) <= 1 or (nums[0] + len(nums) - 1) == nums[-1]:
        return None

    low = 0
    high = len(nums) - 1

    while (high - low) != 1:
        mid = (low + high) // 2
        mid_diff = nums[mid] - mid

        if (nums[low] - low) != mid_diff:
            high = mid

        elif (nums[high] - high) != mid_diff:
            low = mid

    return nums[low] + 1


if __name__ == "__main__":
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 9]
    print(get_missing_num(sorted_array))
