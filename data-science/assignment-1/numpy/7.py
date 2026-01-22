# Sorting + Top-K Without Full Sort
#
# - Create 100 random numbers (floats).
# - Find top 10 values and their indices using an efficient approach (argpartition).
# - Print top 10 sorted descending (values + indices aligned).
#

import numpy as np

if __name__ == "__main__":
    rng = np.random.default_rng()

    array = rng.random(100)

    top_indexes = array.argpartition(-10)[-10:]
    top_values = array[top_indexes]

    sorted_indexes = top_values.argsort()[::-1]

    print(
        f"Values: {top_values[sorted_indexes]}",
        f"Indices: {top_indexes[sorted_indexes]}",
        sep="\n",
    )
