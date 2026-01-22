# Matrix Ops (Dot, Transpose, Identity)
#
# - Generate two matrices A (3, 4) and B (4, 2).
# - Compute A @ B.
# - Verify properties:
#       - (A.T).T equals A
#       - create identity matrix I and show A @ I (shape permitting).
#

import numpy as np

if __name__ == "__main__":
    rng = np.random.default_rng()

    low = 0
    high = 10

    matrix_a = rng.integers(low, high, size=(3, 4))
    matrix_b = rng.integers(low, high, size=(4, 2))

    transpose_of_transpose = (matrix_a.T).T

    identity_matrix = np.identity(max(matrix_a.shape), dtype=np.int64)

    print(
        f"Matrix Multiplication: \n{matrix_a @ matrix_b}",
        f"(A.T).T == A ? {np.allclose(transpose_of_transpose, matrix_a)}",
        f"A . I = \n{matrix_a @ identity_matrix}",
        sep="\n",
    )
