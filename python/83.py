# Prog. 083
# Write a python function to find the character made by adding all the characters of the given string.


def sum_of_characters(string: str) -> str | None:
    if len(string) == 0:
        return None
    
    char_sum = 0

    for s in string:
        char_sum += ord(s)

    # max val from 'chr()' docs
    if char_sum >= 0x110000:
        return None

    return chr(char_sum)

if __name__ == '__main__':
    string = "Hello"
    print(sum_of_characters(string))
