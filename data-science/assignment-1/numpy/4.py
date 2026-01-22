# Broadcasting Practice
#
# - Create a (4, 5) matrix of random floats.
# - Create a (5, ) vector and add it to every row using broadcasting.
# - Normalize each row to sum to 1 (handle division carefully).
#

import numpy as np

if __name__ == "__main__":
    rng = np.random.default_rng()

    matrix = rng.random(size=(4, 5))
    vector = rng.random(size=5)

    broadcast_sum_matrix = matrix + vector

    row_sums = broadcast_sum_matrix.sum(axis=1, keepdims=True)

    zero_positions = row_sums == 0

    broadcast_sum_matrix[zero_positions.flatten()] = 1 / broadcast_sum_matrix.shape[1]
    row_sums[zero_positions] = 1

    normalized_matrix = broadcast_sum_matrix / row_sums

    print(
        f"Matrix: {matrix}",
        f"Vector: {vector}",
        f"Broadcast Sum: {broadcast_sum_matrix}",
        f"Normalized Matrix: {normalized_matrix}",
        sep="\n",
    )
