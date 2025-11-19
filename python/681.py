# Prog. 681
# Write a python function to find the smallest prime divisor of a number.

# References:
# - https://www.geeksforgeeks.org/dsa/smallest-prime-divisor-of-a-number/ 

import time

def smallest_prime_divisor(num: int) -> int | None:
    if num <= 1:
        return None
    
    if num % 2 == 0:
        return 2
    
    for i in range(3, num, 2):
        is_prime = True

        for j in range(3, i, 2):
            if i % j == 0:
                is_prime = False
                break

        if is_prime == True and num % i == 0:
            return i

    return num


# a better solution from 'geeks for geeks'
def smallest_prime_divisor_2(num: int) -> int | None:
    if num <= 1:
        return None
    
    if num % 2 == 0:
        return 2
    
    i = 3 

    while (i * i) <= num:
        if num % i == 0:
            return i
        
        i += 2
        
    return num

# 'smallest_prime_divisor_2()' is still better but 
# this is another approach using something from 'Sieve of Eratosthenes'
def smallest_prime_divisor_3(num: int) -> int | None:
    if num <= 1:
        return None
    
    if num % 2 == 0:
        return 2
    
    primes = list()
    i = 3

    while (i * i) <= num:
        if _is_prime(i, primes) == True:
            if num % i == 0:
                return i
            
            primes.append(i)

        i += 2

    return num

# utility function
# this function assumes that 'primes' has all the prime numbers which appear before 'num'
def _is_prime(num: int, primes: list[int]) -> bool:
    if len(primes) == 0:
        return True

    i = 0

    while (primes[i] ** 2) <= num:
        if num % primes[i] == 0:
            return False
        
        i += 1

    return True


if __name__ == '__main__':
    print(smallest_prime_divisor_2(9))   