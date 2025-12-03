# Prog. 504
# Write a python function to find the cube sum of first n natural numbers.


def cube_sum(num: int) -> int | None:
    if num < 0:
        return None

    sum = 0

    while num > 0:
        sum += num**3
        num -= 1

    return sum


if __name__ == "__main__":
    print(cube_sum(5))
