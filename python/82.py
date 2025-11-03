# Prog. 082	
# Write a function to find the volume of a sphere.

from math import pi

def volume_of_sphere(radius: int | float) -> int | float:
    volume = (4 / 3) * pi * (radius ** 3)
    radius_type = type(radius)
    return radius_type(volume)

if __name__ == "__main__":
    radius_of_sphere = 5.

    volume = volume_of_sphere(radius_of_sphere)
    print(volume)