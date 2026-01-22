# GroupBy Aggregations
#
# - Group by city and compute:
#       - total orders
#       - unique customers
#       - total revenue (sum net_amount)
#       - average order value
# - Sort by revenue desc and show top 10 cities.
#

import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("data/orders.csv")

    grouped_df = (
        df.groupby("city")
        .aggregate(
            total_orders=pd.NamedAgg("order_id", "count"),
            unique_customers=pd.NamedAgg("customer_id", "nunique"),
            total_revenue=pd.NamedAgg("net_amount", "sum"),
            average_order_value=pd.NamedAgg("net_amount", "mean"),
        )
        .reset_index(level=0)
    )

    print(grouped_df)

    sorted_df = grouped_df.sort_values(by="total_revenue", ascending=False)

    print("Top 10 CIties:")
    print(sorted_df[["city", "total_revenue"]][:10])
