# Prog. 032
# Write a python function to find the largest prime factor of a given number.

# References:
# - https://www.geeksforgeeks.org/dsa/find-largest-prime-factor-number/


# 2 methods:
# 1. Following prime factorization by division method
# 2. Compute all primes till 'n' and find prime factors in reverse (not implemented)


# Keep simplifying (dividing) the number till sqrt(n)
# if num cannot be simplified then it is prime itself
def get_largest_prime_factor_1(num: int) -> int | None:
    largest_prime = None

    if num <= 1:
        return largest_prime

    while num % 2 == 0:
        largest_prime = 2
        num //= 2

    while num % 3 == 0:
        largest_prime = 3
        num //= 3

    i = 5
    while i <= num // i:
        while num % i == 0:
            largest_prime = i
            num //= i

        i += 2

    if num >= 5:
        return num

    return largest_prime


# same as 1 but instead of simplifying by each odd number
# step using 6k and 6k + 1 rule
def get_largest_prime_factor_2(num: int) -> int | None:
    largest_prime = None

    if num <= 1:
        return None

    for i in [2, 3]:
        while num % i == 0:
            largest_prime = i
            num //= i

    i = 5
    while i <= num // i:
        while num % i == 0:
            largest_prime = i
            num //= i

        j = i + 2

        while num % j == 0:
            largest_prime = j
            num //= j

        i += 6

    if num >= 5:
        return num

    return largest_prime


if __name__ == "__main__":
    print(get_largest_prime_factor_2(84))
