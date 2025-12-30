# Prog. 060
# Write a function to find the maximum length of the subsequence with difference between adjacent elements for the given array.


def max_len_of_sub_sequence(array: list[int], diff: int) -> int:
    if len(array) <= 1:
        return 0

    i = 1
    max_len = 0
    curr_len = 0

    while i < len(array):
        d = array[i] - array[i - 1]

        if d == diff:
            curr_len += 1
        else:
            curr_len = 0

        if max_len < curr_len:
            max_len = curr_len

        i += 1

    return max_len + 1


if __name__ == "__main__":
    print(max_len_of_sub_sequence([13, 14, 15, 16, 17, 1, 2, 4, 5, 6], 1))
    print(max_len_of_sub_sequence([1, 2], 1))
