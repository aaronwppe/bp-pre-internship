#  Missing Values Simulation
#
# - Create a 1D float array of size 40.
# - Randomly turn 20% positions into np.nan.
# - Compute mean ignoring NaNs.
# - Replace NaNs with the median of non-NaN values
#

import numpy as np

if __name__ == '__main__':
    rng = np.random.default_rng()

    size = 40
    array = rng.random(size)

    random_positions = np.random.choice(size, int(size * 0.2), replace=False)
    array[random_positions] = np.nan

    print(f"Array = {array}")
    print(f"Mean = {np.nanmean(array)}")
    print(f"Transformed Array = {
            np.nan_to_num(
                array, 
                copy=False, 
                nan=np.nanmedian(array),
            )}"
    )
    # alternative way 
    # array[random_positions] = np.nanmedian(array)
