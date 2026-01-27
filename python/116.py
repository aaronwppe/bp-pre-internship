# Prog. 116
# Write a function to convert a given tuple of positive integers into an integer.

def get_integer(integers: tuple[int, ...]) -> int | None:
    num = 0
    mul = 10 ** (len(integers) - 1)

    for i in integers:
        if not isinstance(i, int) or i < 0:
            return None

        num += mul * i
        mul //= 10

    return num

if __name__ == '__main__':
    print(get_integer((1, 2, 3)))