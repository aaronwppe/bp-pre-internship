# Prog. 379
# Write a function to find the surface area of a cuboid.

def surface_area(length: int | float, breadth: int | float, height: int | float) -> int | float:
    return 2 * ((length * breadth) + (breadth * height) + (length * height))

if __name__ == "__main__":
    l, b, h = 5, 20, 6
    
    print(surface_area(l, b, h))