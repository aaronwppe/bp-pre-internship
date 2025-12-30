# Prog. 065
# Write a function of recursion list sum.


def recursive_sum(input_list: list[int]) -> int:
    if len(input_list) == 0:
        return 0

    return input_list[0] + recursive_sum(input_list[1:])


if __name__ == "__main__":
    print(recursive_sum([1, 2, 3, 4]))
