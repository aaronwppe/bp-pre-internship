# Prog. 176
# Write a function to find the perimeter of a triangle.


def perimeter(sides_of_triangle: tuple[int|float, int|float, int|float]) -> int | float:
    return sum(sides_of_triangle)

if __name__ == "__main__":
    sides = (1.2, 2.3, 1)

    print(perimeter(sides))