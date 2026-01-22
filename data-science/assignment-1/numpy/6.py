# Fancy Indexing + Scatter Update
#
# - Create a length-30 zero array.
# - Randomly pick 8 unique positions and set them to 1.
# - Then set positions divisible by 5 to 9 (overwriting if needed)
#

import numpy as np

if __name__ == "__main__":
    size = 30
    array = np.zeros(shape=size, dtype="int")

    random_positions = np.random.choice(size, 8, replace=False)

    array[random_positions] = 1
    array[::5] = 9

    print(f"Final Array: {array}")
