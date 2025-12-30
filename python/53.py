# Prog. 053
# Write a python function to check whether the first and last characters of a given string are equal or not.


def is_first_and_last_equal(string: str) -> bool:
    if len(string) <= 1:
        return True

    return string[0] == string[-1]


if __name__ == "__main__":
    print(is_first_and_last_equal("oh hello"))
