# Prog. 044
# Write a function that matches a word at the beginning of a string.

import re


def matches_at_beginning(string: str, word: str) -> bool:
    pattern = r"^" + word
    return re.search(pattern, string) != None


if __name__ == "__main__":
    print(matches_at_beginning("Hello World", "Hello"))
