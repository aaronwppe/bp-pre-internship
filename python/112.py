# Prog. 112
# Write a python function to find the perimeter of a cylinder.

def perimeter_of_cylinder(diameter: int | float, height: int | float) -> int | float:
    return (2 * diameter) + (2 * height)


if __name__ == '__main__':
    print(perimeter_of_cylinder(5, 10))