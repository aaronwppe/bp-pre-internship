#  Prog. 124
# Write a function to get the angle of a complex number.

import math


def get_angle(num: complex) -> float:
    return math.atan2(num.imag, num.real)


if __name__ == "__main__":
    print(f"{get_angle(3 + 4j):.4f}")
