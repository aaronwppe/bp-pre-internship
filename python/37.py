# Prog. 037
# Write a function to sort a given mixed list of integers and strings.


def sort_mixed_list(input_list: list[int | str], reverse: bool = False) -> None:
    input_list.sort(key=lambda element: str(element), reverse=reverse)
    return input_list


if __name__ == "__main__":
    print(sort_mixed_list(["ba", "aa", 1, 2]))
