# Prog. 036
# Write a python function to find the nth digit in the proper fraction of two given numbers.


def get_nth_digit(numerator: int, denominator: int, n: int) -> int | None:
    numerator = abs(numerator)
    denominator = abs(denominator)

    if numerator >= denominator or n <= 0:
        return None

    digit = 0
    count = 0

    while numerator > 0 and count < n:
        numerator *= 10
        digit = numerator // denominator
        numerator %= denominator
        count += 1

    if count < n:
        return 0

    return digit


if __name__ == "__main__":
    print(get_nth_digit(1, 2, 1))
