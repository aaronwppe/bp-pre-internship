# Prog. 051
# Write a function to print check if the triangle is equilateral or not.


def is_equilateral(s1: int | float, s2: int | float, s3: int | float) -> bool:
    return s1 == s2 == s3


if __name__ == "__main__":
    print(is_equilateral(1, 1, 1))
