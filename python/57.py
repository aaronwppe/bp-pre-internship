# Prog. 057
# Write a python function to find the largest number that can be formed with the given digits.

# References:
# - https://www.geeksforgeeks.org/dsa/find-the-largest-number-that-can-be-formed-with-the-given-digits/


def get_largest_num(digits: list[int]) -> int | None:
    if not digits:
        return None

    digits.sort(reverse=True)

    num = 0

    for digit in digits:
        if digit < 0 or digit > 9:
            return None

        num *= 10
        num += digit

    return num


# Solution from 'geeks for geeks'
def get_largest_num_2(digits: list[int]) -> int | None:
    if not digits:
        return None

    freq = [0] * 10

    for digit in digits:
        if digit < 0 or digit > 9:
            return None

        freq[digit] += 1

    num = 0
    i = 9

    while i >= 0:
        while freq[i] > 0:
            num *= 10
            num += i
            freq[i] -= 1

        i -= 1

    return num


if __name__ == "__main__":
    print(get_largest_num([1, 2, 3, 3, 0]))
