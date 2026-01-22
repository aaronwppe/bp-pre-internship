# Pivot Table Dashboard View
#
# - Create a pivot:
#       - index: month (from order_date )
#       - columns: category
#       - values: net_amount sum
# - Add a “Grand Totalˮ column and compute month-over-month growth %.
#

import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("data/orders.csv")

    df["order_date"] = pd.to_datetime(df["order_date"], format="%Y-%m-%d")
    df["order_month"] = df["order_date"].dt.month_name()

    pivot_df = df.pivot_table(
        index="order_month",
        columns="category",
        values="net_amount",
        aggfunc="sum",
        fill_value=0,
        sort=False,
    )

    pivot_df["grand_total"] = pivot_df.sum(axis=1)

    pivot_df["growth_pct"] = pivot_df["grand_total"].pct_change() * 100
    pivot_df["growth_pct"] = pivot_df["growth_pct"].fillna(0)

    print(pivot_df)
