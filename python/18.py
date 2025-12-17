# Prog. 18
# Write a function to remove characters from the first string which are present in the second string.


def remove_characters(string: str, char: str) -> str:
    ret_string = ""

    char_set = set(char)

    for s in string:
        if s not in char_set:
            ret_string += s

    return ret_string


if __name__ == "__main__":
    print(remove_characters("Hello World", "Hl "))
