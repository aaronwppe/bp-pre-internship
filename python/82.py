# Prog. 082
# Write a function to find the volume of a sphere.

import math

def volume_of_sphere(radius: int | float) -> float | None:
    if radius <= 0:
        return None
    
    return (4 / 3) * math.pi * radius ** 3 

if __name__ == '__main__':
    radius = 5
    print(volume_of_sphere(5))