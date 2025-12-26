# Prog. 033
# Write a python function to convert a decimal number to binary number.

import math


def decimal_to_binary(
    input_decimal: int | float, max_fractional_bit_len: int = 10
) -> str:
    sign = "-" if input_decimal < 0 else ""
    input_decimal = abs(input_decimal)

    decimal_tuple = math.modf(input_decimal)
    fractional = decimal_tuple[0]
    integer = int(decimal_tuple[1])

    binary_str = ""

    while integer > 0:
        binary_str += str(integer % 2)
        integer //= 2

    binary_str = sign + "0b" + binary_str[::-1]

    if isinstance(input_decimal, int):
        return binary_str

    fractional_binary_str = ""

    while fractional > 0 and len(fractional_binary_str) < max_fractional_bit_len:
        fractional, bit = math.modf(fractional * 2)
        fractional_binary_str += str(int(bit))

    return binary_str + "." + fractional_binary_str


if __name__ == "__main__":
    print(decimal_to_binary(-5.1))
