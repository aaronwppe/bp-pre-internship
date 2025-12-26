# Prog. 50
# Write a function to find the list with minimum length using lambda function.

if __name__ == "__main__":
    min_len_list = lambda input_lists: min(input_lists, key=len)

    lists = [
        [1, 2, 3],
        ["a", "b"],
        ["1"],
    ]

    print(min_len_list(lists))
