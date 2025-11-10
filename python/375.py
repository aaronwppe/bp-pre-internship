# Prog. 375
# Write a function to round the given number to the nearest multiple of a specific number.


def round_num(num: int | float, multiple_of: int | float) -> int | float:
    if multiple_of == 0:
        return 0
    
    multiplier = num // multiple_of

    lower_multiple = multiple_of * multiplier
    upper_multiple = lower_multiple + multiple_of
    
    if (num - lower_multiple) < (upper_multiple - num):
        return lower_multiple
    else:
        return upper_multiple 
    
if __name__ == "__main__":
    print(round_num(500, 3))
    print(round_num(11, 3))