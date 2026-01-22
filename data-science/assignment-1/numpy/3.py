# Reshape  Axis Operations
#
# - Create an array from 1 to 60 and reshape into (5, 12).
# - Compute:
#       - row-wise sums
#       - column-wise means
#       - global std
# - Find the index of the maximum value in the 2D array
#

import numpy as np

if __name__ == "__main__":
    array = np.arange(1, 61)

    shape = (5, 12)
    reshaped_array = array.reshape(shape)

    max_2d_index = reshaped_array.argmax()
    max_index_tuple = np.unravel_index(max_2d_index, shape)

    print(
        f"Reshaped Array: {reshaped_array}",
        f"Row Sum: {reshaped_array.sum(axis=1)}",
        f"Column Mean: {reshaped_array.mean(axis=0)}",
        f"Standard Deviation: {reshaped_array.std():.4f}",
        f"Max value Index: ({max_index_tuple[0]}, {max_index_tuple[1]})",
        sep="\n",
    )
