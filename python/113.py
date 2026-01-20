# Prog. 113
# Write a function to check if a string represents an integer or not.

import re

def is_integer(string: str) -> bool:
    pattern = "^ *0*[0-9]+ *$"
    return re.search(pattern, string) != None

if __name__ == '__main__':
    print(is_integer("09"))