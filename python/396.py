# Prog. 396
# Write a function to check whether the given string starts and ends with the same character or not using regex.

# References:
# - https://www.pythontutorial.net/python-regex/python-regex-backreferences/

import re


def check_start_and_end_equality(string: str) -> bool:
    return re.search(r"^(.).*\1$", string) is not None


if __name__ == "__main__":
    print(check_start_and_end_equality("*type*"))
