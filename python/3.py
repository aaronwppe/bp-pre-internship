# Prog. 003
# Write a python function to identify non-prime numbers.


def is_not_prime(num: int) -> bool:
    if num <= 1:
        return True

    i = 2

    while i * i <= num:
        if num % i == 0:
            return True
        i += 1

    return False


if __name__ == "__main__":
    print(is_not_prime(4))
