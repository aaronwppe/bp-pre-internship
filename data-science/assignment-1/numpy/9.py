# Linear Regression From Scratch
#
# - Generate synthetic data:
#       - X: 200 samples, 1 feature (random)
#       - y = 3*X + 5 + noise
# - Fit using closed-form normal equation (no sklearn).
# - Print estimated slope and intercept
#

import numpy as np

if __name__ == "__main__":
    rng = np.random.default_rng()

    sample_count = 200

    feature_1 = rng.random((sample_count, 1))
    y = (3 * feature_1) + 5 + rng.random((sample_count, 1))

    feature_0 = np.ones((sample_count, 1))

    X = np.append(feature_0, feature_1, axis=1)

    theta = np.linalg.inv(X.T @ X) @ X.T @ y

    print(f"Intercept = {theta[0][0]:.4f}")
    print(f"Slope = {theta[1][0]:.4f}")
