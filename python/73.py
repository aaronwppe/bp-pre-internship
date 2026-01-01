# Prog. 073
# Write a function to split the given string with multiple delimiters by using regex.

import re

def split_using_regex(string: str, delimiters: list[str]) -> str:
    pattern = "|".join(delimiters)

    return re.split(pattern, string)


if __name__ == '__main__':
    string = "abcbcpcbp"
    print(split_using_regex(string, ["b", "p"]))
