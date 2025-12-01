# Prog. 951
# Write a function to find the maximum of similar indices in two lists of tuples.


List_of_Tuples = list[tuple[int | float, ...]]


def max_tuples(list_1: List_of_Tuples, list_2: List_of_Tuples) -> List_of_Tuples:
    if len(list_1) > len(list_2):
        max_list = list_1
        max_list_is_first = True
        min_len = len(list_2)

    else:
        max_list = list_2
        max_list_is_first = False
        min_len = len(list_1)

    ret_list = [(max(list_1[i]), max(list_2[i])) for i in range(min_len)]

    len_diff = abs(len(list_1) - len(list_2))

    if len_diff == 0:
        return ret_list

    get_tuple = lambda value: (
        (value, None) if max_list_is_first == True else (None, value)
    )

    return ret_list + [get_tuple(max(tup)) for tup in max_list[-len_diff:]]


if __name__ == "__main__":
    list_1 = [
        (1, 2),
        (9, 8),
        (12, 12),
    ]
    list_2 = [
        (4, 3),
        (0, 1),
    ]

    print(max_tuples(list_1, list_2))
