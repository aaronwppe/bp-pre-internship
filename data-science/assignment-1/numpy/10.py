# Time Series Rolling Window Stats
#
# - Create a 1D array representing 365 days of random “daily salesˮ.
# - Compute rolling 7-day mean and rolling 30-day mean using NumPy (no pandas).
# - Detect days where sales are > (rolling_30_mean + 2*rolling_30_std).
#

import numpy as np

if __name__ == "__main__":
    rng = np.random.default_rng()

    daily_sales = rng.integers(low=0, high=100, size=365)

    rolling_mean_lambda = lambda a, w: np.convolve(a, np.ones(w) / w, mode="valid")

    mean_7_day = rolling_mean_lambda(daily_sales, 7)
    mean_30_day = rolling_mean_lambda(daily_sales, 30)

    std_30_day = np.lib.stride_tricks.sliding_window_view(daily_sales, 30).std(axis=1)

    anamoly_condition = daily_sales[29:] > (mean_30_day + (2 * std_30_day))
    anomaly_days = np.where(anamoly_condition)[0] + 29

    print(f"Anamoly Sales: {daily_sales[anomaly_days]}")
