# Prog. 096
# Write a python function to find the number of divisors of a given integer.

import math

def get_divisor_count(num: int) -> int | float:
    if num == 0:
        return math.inf
    
    num = abs(num)

    if num == 1:
        return 1

    count = 2
    i = 2
    while i <= num // i:
        if num % i == 0:
            count += 1
        
        i += 1

    return count


if __name__ == '__main__':
    print(get_divisor_count(25))

    