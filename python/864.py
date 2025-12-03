# Prog. 864
# Write a function to find palindromes in a given list of strings using lambda function.

from typing import Callable


def filter_strings(
    input_list: list[str], filter_callable: Callable[[str], bool]
) -> list[str]:
    return [s for s in input_list if filter_callable(s) == True]


def is_palindrome(input_string: str) -> bool:
    i = 0
    j = len(input_string) - 1
    ret_bool = True

    while i < j:
        if input_string[i] != input_string[j]:
            ret_bool = False
            break

        i += 1
        j -= 1

    return ret_bool


if __name__ == "__main__":
    arr = ["", "a", "aba", "abc", "abba"]

    is_palindrome_1 = lambda s: s == s[::-1]
    is_palindrome_2 = lambda s: is_palindrome(s)

    print(filter_strings(arr, is_palindrome_2))
