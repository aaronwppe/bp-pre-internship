# Cohort Analysis (Intermediate)
#
# - Define cohort month = customerʼs first order month.
# - For each cohort, compute:
#       - number of active customers by month offset (M0, M1, M2, ... )
#       - retention rate matrix (cohort table)
# - Output as a DataFrame shaped like a retention heatmap table (values as %).
#

import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("data/orders.csv")

    df["order_date"] = pd.to_datetime(df["order_date"])
    df["order_month"] = df["order_date"].dt.to_period("M")

    df["cohort_month"] = df.groupby("customer_id")["order_month"].transform("min")

    df["month_offset"] = df.apply(
        lambda d: (d["order_month"].year - d["cohort_month"].year) * 12
        + (d["order_month"].month - d["cohort_month"].month),
        axis=1,
    )

    counts = (
        df.groupby(["cohort_month", "month_offset"])["customer_id"]
        .nunique()
        .reset_index()
    )

    table = counts.pivot(
        index="cohort_month", columns="month_offset", values="customer_id"
    )

    retention_rate = table.divide(table[0], axis=0) * 100

    print(retention_rate)
