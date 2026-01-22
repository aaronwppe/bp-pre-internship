# Outlier Detection + Capping (Intermediate)
#
# - For each category
#       - compute IQR of net_amount
#       - flag outliers (outside [Q1-1.5IQR, Q3+1.5IQR])
#       - cap outliers to bounds (winsorize)
# - Report outlier counts by category before/after
#

import pandas as pd


def get_outlier_flag(
    series: pd.Series, lower_bound: pd.Series, upper_bound: pd.Series
) -> pd.Series:
    return (series < lower_bound) | (series > upper_bound)


if __name__ == "__main__":
    df = pd.read_csv("data/orders.csv")

    grouped_net_amount = df.groupby("category")["net_amount"]

    q1 = grouped_net_amount.transform(lambda x: x.quantile(0.25))
    q3 = grouped_net_amount.transform(lambda x: x.quantile(0.75))

    iqr_series = q3 - q1
    lower_bound_series = q1 - (1.5 * iqr_series)
    upper_bound_series = q3 + (1.5 * iqr_series)

    df["outlier"] = get_outlier_flag(
        df["net_amount"], lower_bound_series, upper_bound_series
    )

    old_outlier_count = df[df["outlier"] == True].shape[0]

    df["net_amount"] = df["net_amount"].clip(lower_bound_series, upper_bound_series)

    df["outlier"] = get_outlier_flag(
        df["net_amount"], lower_bound_series, upper_bound_series
    )

    new_outlier_count = df[df["outlier"] == True].shape[0]

    print(
        "Outlier Counts:" f"Before: {old_outlier_count}",
        f"After: {new_outlier_count}",
        sep="\n",
    )
