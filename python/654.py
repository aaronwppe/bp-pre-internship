# Prog. 654
# Write a function to find the perimeter of a rectangle.

def perimeter(length: int | float, breadth: int | float) -> int | float:
    return (length * 2) + (breadth * 2)

if __name__ == '__main__':
    print(perimeter(5.6, 4))