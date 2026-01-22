#  Window Functions (Intermediate)
#
# - For each customer:
#       - sort by order_date
#       - compute prev_order_date
#       - compute days_since_prev
#       - compute rolling 3-order average net_amount
# - Identify customers whose average order value is increasing (simple heuristic).
#

import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("data/orders.csv")

    df["order_date"] = pd.to_datetime(df["order_date"], format="%Y-%m-%d")

    df = df.sort_values(by="order_date")

    df["prev_order_date"] = df.groupby("customer_id")["order_date"].shift(1)
    df["days_since_prev"] = df["order_date"] - df["prev_order_date"]
    df["average_net_amount"] = (
        df.groupby("customer_id")["net_amount"]
        .rolling(window=3, min_periods=1)
        .mean()
        .reset_index(level=0, drop=True)
    )

    df = pd.merge(
        df,
        df.groupby("customer_id")["average_net_amount"]
        .aggregate(first_average="first", last_average="last")
        .reset_index(level=0),
        on="customer_id",
    )

    df["order_value_increasing"] = df["first_average"] < df["last_average"]

    display_columns = [
        "customer_id",
        "prev_order_date",
        "days_since_prev",
        "average_net_amount",
        "order_value_increasing",
    ]

    print(df[display_columns].dropna())
