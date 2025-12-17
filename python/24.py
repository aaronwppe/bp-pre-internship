# Prog. 24
# Write a function to convert the given binary number to its decimal equivalent.


def binary_to_decimal(binary: str) -> int | float | None:
    ret_decimal = 0

    split_binary_list = binary.split(".", maxsplit=1)

    if len(split_binary_list) == 2:
        fractional_binary = split_binary_list[1]

        for i, binary_digit in enumerate(fractional_binary, start=1):
            ret_decimal += int(binary_digit) * (2 ** (-i))

    non_fractional_binary = split_binary_list[0]

    for i, binary_digit in enumerate(non_fractional_binary[::-1]):
        ret_decimal += int(binary_digit) * (2**i)

    return ret_decimal


if __name__ == "__main__":
    print(binary_to_decimal("0000010.1"))
