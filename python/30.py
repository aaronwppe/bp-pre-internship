# Prog. 30
# Write a python function to count all the substrings starting and ending with same characters.


def count_sub_strings(string: str) -> int:
    char_freq = dict()

    for s in string:
        if s not in char_freq:
            char_freq[s] = 1
        else:
            char_freq[s] += 1

    count = 0
    for n in char_freq.values():
        count += (n * (n + 1)) // 2

    return count


if __name__ == "__main__":
    print(count_sub_strings("pap-pop"))


# occ -- sub_count --
# 0 -- 0
# 1 -- 0 + 1 = 1
# 2 -- 1 + 2 = 3
# 3 -- 3 + 3 = 6
# 4 -- 6 + 4 = 10

# Let n = occ,
# sub_count = 1 + ... (n - k(i)) + ... + (n - 2) + (n - 1) + n
# Triangular Number = [ n(n + 1) ] / 2
