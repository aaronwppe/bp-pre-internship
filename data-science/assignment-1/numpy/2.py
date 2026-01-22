# Slicing + Boolean Masking
#
# - Create an array of 50 random integers between 1 and 100.
# - Extract:
#       - all even numbers
#       - numbers divisible by 3 and > 50
# - Replace values < 20 with 20 (without loops)
#

import numpy as np


if __name__ == "__main__":
    rng = np.random.default_rng()
    array = rng.integers(low=1, high=100, size=50)

    print(
        f"Array: {array}",
        f"Even elements: {array[array % 2 == 0]}",
        f"Divisible by 3 and Greater than 50: {array[(array % 3 == 0) & (array > 50)]}",
        sep="\n",
    )

    array[array < 20] = 20
    print(f"Transformed Array: {array}")
