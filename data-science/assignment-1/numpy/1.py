# Array Basics + Types
#
# - Create a 1D array of integers from 1 to 20.
# - Print: shape, dtype, min, max, sum, mean.
# - Convert it to float and show dtype change.
#

import numpy as np

if __name__ == "__main__":
    array = np.arange(1, 21)

    print(
        f"Array: {array}",
        f"Shape: {array.shape}",
        f"Datatype: {array.dtype}",
        f"Min: {array.min()}",
        f"Max: {array.max()}",
        f"Sum: {array.sum()}",
        f"Mean: {array.mean()}",
        sep="\n",
    )

    float_array = array.astype(np.float64)
    print(f"Float Array Datatype: {float_array.dtype}")
