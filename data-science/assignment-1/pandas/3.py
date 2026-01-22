# Filtering + Multi-condition Queries
#
# - Filter orders:
#       - category in a set (e.g., Electronics/Fashion)
#       - net_amount > X
#       - order_date within last N days (relative to max_date)
# - Output count + total net_amount
#

import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("data/orders.csv")
    df["order_date"] = pd.to_datetime(df["order_date"], format="%Y-%m-%d")

    categories = {"Fashion", "Home"}
    date_limit = df["order_date"].max() - pd.Timedelta(days=30)

    condition_1 = df["category"].isin(categories)
    condition_2 = df["net_amount"] > 4_000
    condition_3 = df["order_date"] >= date_limit

    print("Filtered Data:")
    print(df[condition_1 & condition_2 & condition_3])

    print(f"Total Orders: {df.shape[0]}")
    print(f"Total Net Amount: {df['net_amount'].sum()}")
