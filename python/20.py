# Prog. 20
# Write a function to check if the given number is woodball or not.

# References:
# - https://www.geeksforgeeks.org/dsa/woodall-number/


def is_woodall(num: int) -> bool:
    if num % 2 == 0:
        return False

    num += 1
    power = 0

    while num % 2 == 0:
        num //= 2
        power += 1

        if power == num:
            return True

    return False


if __name__ == "__main__":
    print(is_woodall(63))


# nums = 1, 2, 3, 4, 5, 6, ...
# woodall = 1, 7, 23, 63, 159, 383, ...
# W(n) = n * (2 ** n) - 1
