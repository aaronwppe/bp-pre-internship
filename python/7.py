# Prog. 007
# Write a function to find all words which are at least 4 characters long in a string by using regex.

import re


def get_words_by_len(string: str, str_len: int) -> tuple[str, ...]:
    if str_len <= 0:
        return tuple()

    pattern = r"\b[A-Za-z]{" + f"{str_len}" + r",}\b"

    matches = re.findall(pattern, string)
    return tuple(matches)


if __name__ == "__main__":
    print(get_words_by_len("Hello World", 4))
