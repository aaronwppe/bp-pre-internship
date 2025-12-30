# Prog. 039
# Write a function to check if the letters of a given string can be rearranged
# so that two characters that are adjacent to each other are different.


from collections import Counter


def is_rearrange_possible(string: str) -> bool:
    if len(string) <= 1:
        return True

    available_positions = ((len(string) - 1) // 2) + 1
    counter = Counter(string)
    available_positions -= max(counter.values())

    return available_positions >= 0


if __name__ == "__main__":
    string = "aaaabc"
    print(is_rearrange_possible(string))


# len - positions
# 1 = 1
# 2 = 1
# 3 = 2
# 4 = 2
# 5 = 3
# 6 = 3
# 7 = 4
# 8 = 4

# Relation = (len - 1)/2 + 1
