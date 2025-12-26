# Prog. 038
# Write a function to find the division of first even and odd number of a given list.


def divide_first_even_odd(input_list: list[int]) -> float | None:
    numerator = None
    denominator = None

    for element in input_list:
        if element % 2 == 0 and numerator is None:
            numerator = element

        elif denominator is None:
            denominator = element

        if numerator is not None and denominator is not None:
            return numerator // denominator

    return None


if __name__ == "__main__":
    print(divide_first_even_odd([1, 1, 1, 2]))
