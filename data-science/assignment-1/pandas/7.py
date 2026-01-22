# Joins / Merges (Customers + Orders)
#
# - Create a customers DataFrame: customer_id, signup_date, segment.
# - Merge with orders.
# - Compute revenue by segment and retention proxy:
#       - “active in last 60 daysˮ per segment
#

import pandas as pd

if __name__ == "__main__":
    customers_df = pd.read_csv("data/customers.csv")
    orders_df = pd.read_csv("data/orders.csv")

    orders_df["order_date"] = pd.to_datetime(orders_df["order_date"], format="%Y-%m-%d")

    merged_df = pd.merge(left=orders_df, right=customers_df, on="customer_id")
    date_after = merged_df["order_date"].max() - pd.Timedelta(days=60)

    filtered_df = merged_df[merged_df["order_date"] > date_after]

    result_df = filtered_df.groupby("segment").aggregate(
        revenue=pd.NamedAgg("net_amount", "sum")
    )

    print(result_df)
