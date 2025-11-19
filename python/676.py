# Prog. 676
# Write a function to remove everything except alphanumeric characters from the given string by using regex.

import re

def filter_str(string: str) -> str:
    pattern = re.compile("[A-Z]|[a-z]|[0-9]")
    return ''.join(pattern.findall(string))

if __name__ == '__main__':
    print(filter_str("&Hello 1234!"))