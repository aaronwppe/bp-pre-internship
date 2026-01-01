# Prog. 091
# Write a function to check if a substring is present in a given list of string values

def substring_exists(string_list: list[str], substring: str) -> bool:
    for s in string_list:
        if substring in s:
            return True
        
    return False


if __name__ == '__main__':
    list_1 = [
        "cos",
        "bcs",
        "cs",
    ]

    print(substring_exists(list_1, "cs"))