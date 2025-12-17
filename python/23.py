# Prog. 23
# Write a python function to find the maximum sum of elements of list in a list of lists.


def get_max_sum(lists: list[list[int]]) -> int:
    max_sum = 0

    for li in lists:
        list_sum = sum(li)
        if list_sum > max_sum:
            max_sum = list_sum

    return max_sum


if __name__ == "__main__":
    lists = [
        [1, 2, 3],
        [2, 2, 2],
        [0, 0, 1],
        [4, 4, 4],
    ]

    print(get_max_sum(lists))
