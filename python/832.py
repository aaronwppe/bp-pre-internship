# Prog. 832
# Write a function to extract the maximum numeric value from a string by using regex.

# References:
# - https://docs.python.org/3/library/re.html#re.findall

import re


def get_max_int(string: str) -> int | None:
    pattern = re.compile("-?[0-9]+")

    num_strings = pattern.findall(string)

    if not num_strings:
        return None
    
    max_num = int(num_strings[0])

    if len(num_strings) == 1:
        return max_num
    
    for num_str in num_strings[1:]:
        num = int(num_str)
        if num > max_num:
            max_num = num

    return max_num


if __name__ == "__main__":
   string = "-this 234 is-549a -123 string." 
   print(get_max_int(string))