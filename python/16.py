# Prog. 16
# Write a function to find sequences of lowercase letters joined with an underscore.

import re


def get_lowercase_sequences(string: str) -> list[str]:
    pattern = r"[a-z]+(?:_+[a-z]+)+"
    return re.findall(pattern, string)


if __name__ == "__main__":
    print(get_lowercase_sequences("hello_world Hello_worLd"))
