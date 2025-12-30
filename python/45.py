# Prog. 045
# Write a function to find the gcd of the given array elements.


def get_array_gcd(array: list[int]) -> int | None:
    if len(array) == 0:
        return None

    ret_gcd = array[0]

    for element in array:
        ret_gcd = gcd(ret_gcd, element)

    return ret_gcd


def gcd(n1: int, n2: int) -> int:
    min_element = min(n1, n2)

    for i in range(min_element, 1, -1):
        if n1 % i == 0 and n2 % i == 0:
            return i

    return 1


if __name__ == "__main__":
    array = [2, 4, 6, 8]
    print(get_array_gcd(array))
