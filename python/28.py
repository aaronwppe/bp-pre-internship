# Prog. 028
# Write a python function to find binomial co-efficient.


def get_binomial_coefficient(n: int, r: int) -> int | None:
    if n < 0 or r < 0 or n < r:
        return None
    
    coefficient = 1

    for i in range(n, r, -1):
        coefficient *= i
    
    for i in range(n - r, 1, -1):  
        coefficient //= i

    retun coefficient




# C(n, r) = n! / r! * (n - r)!
# where, n >= r

