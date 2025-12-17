# Prog. 014
# Write a python function to find the volume of a triangular prism.

from math import sqrt


def get_volume_of_triangular_prism(
    first_side: int | float,
    second_side: int | float,
    third_side: int | float,
    height: int | float,
) -> float:
    return (
        (1 / 4)
        * height
        * sqrt(
            -(first_side**4)
            + 2 * (first_side * second_side) ** 2
            + 2 * (first_side * third_side) ** 2
            - second_side**4
            + 2 * (second_side * third_side) ** 2
            - third_side**4
        )
    )


if __name__ == "__main__":
    print(get_volume_of_triangular_prism(4, 2, 3, 9))
