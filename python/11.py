# Prog. 011
# Write a python function to remove first and last occurrence of a given character from the string.


def remove_first_and_last_char(string: str, char: str) -> str:
    string = string.replace(char, "", count=1)

    right_char_idx = string.rfind(char)
    if right_char_idx == -1:
        return string

    if right_char_idx + 1 == len(string):
        return string[:-1]

    return string[0:right_char_idx] + string[right_char_idx + 1 :]


if __name__ == "__main__":
    print(remove_first_and_last_char("helhlho", "h"))
