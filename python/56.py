# Prog. 056
# Write a python function to check if a given number is one less than twice its reverse.


def check_num(num):
    n = abs(num)
    rev = 0

    while n > 0:
        rev *= 10
        rev += n % 10
        n //= 10

    if num < 0:
        rev *= -1

    return ((2 * rev) - 1) == num


if __name__ == "__main__":
    print(check_num(73))
