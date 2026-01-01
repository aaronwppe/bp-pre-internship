# Prog. 085
# Write a function to find the surface area of a sphere.

import math

def get_surface_area_of_sphere(radius: int | float) -> float | None:
    if radius <= 0:
        return None
    
    return 4 * math.pi * radius ** 2


if __name__ == '__main__':
    print(get_surface_area_of_sphere(5))