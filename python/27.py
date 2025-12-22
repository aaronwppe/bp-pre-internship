# Prog. 27
# Write a python function to remove all digits from a list of strings.

import re


def remove_all_digits(string_list: list[str]) -> None:
    pattern = r"[0-9]"

    for i in range(len(string_list)):
        string_list[i] = re.sub(pattern, "", string_list[i])


if __name__ == "__main__":
    string_list = ["Hello123", "aaron1"]
    remove_all_digits(string_list)
    print(string_list)
