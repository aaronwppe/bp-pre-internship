# Prog. 047
# Write a python function to find the last digit when factorial of a divides factorial of b.


import math


def get_last_digit_of_factorial_division(a: int, b: int) -> int | None:
    if a < 0 or b < 0:
        return None

    return (math.factorial(a) // math.factorial(b)) % 10


if __name__ == "__main__":
    print(get_last_digit_of_factorial_division(5, 2))
