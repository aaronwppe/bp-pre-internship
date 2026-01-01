# Prog. 093
# Write a function to calculate the value of 'a' to the power 'b'.

def power(base: int | float, exponent: int | float) -> int | float:
    return base ** exponent

if __name__ == '__main__':
    print(power(-2, 3))