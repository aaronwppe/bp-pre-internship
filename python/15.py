# Prog. 015
# Write a function to split a string at lowercase letters.


def split_at_lowercase(string: str) -> tuple[str, str]:
    i = 0

    while i < len(string):
        if string[i].islower():
            break

        i += 1

    return (string[:i], string[i:])


if __name__ == "__main__":
    print(split_at_lowercase("HIHIH"))
