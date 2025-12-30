# Prog. 43
# Write a function to find sequences of lowercase letters joined with an underscore using regex.

import re


def get_sequences(string: str) -> list[str]:
    pattern = r"[a-z]+(?:_+[a-z]+)+"
    return re.findall(pattern, string)


if __name__ == "__main__":
    string = "hello_world I am_coding_this"
    print(get_sequences(string))
