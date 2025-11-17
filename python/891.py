# Prog. 891
# Write a python function to check whether the given two numbers have same number of digits or not.


def check_digit_equality(n1: int, n2: int) -> bool:
    n1 = abs(n1)
    n2 = abs(n2)
    multiple = 10

    while n1 >= multiple and n2 >= multiple:
        multiple *= 10

    return n1 < multiple and n2 < multiple

# more "pythonic"
def check_digit_equality_using_str(n1: int, n2: int) -> bool:
    return len(str(n1)) == len(str(n2))


if __name__ == '__main__':
    print(check_digit_equality(1, -9))
    print(check_digit_equality(1000, 999))
    print(check_digit_equality(10, 90))
