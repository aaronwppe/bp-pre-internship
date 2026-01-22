# Add Derived Columns
#
# - Using quantity, unit_price, discount_pct: 
#       - compute gross_amount = quantity * unit_price 
#       - compute net_amount = gross_amount * (1 - discount_pct/100)
# - Add a is_high_value flag (net_amount > threshold).
#

import pandas as pd

if __name__ == '__main__':
    file_name = "data/orders.csv"
    df = pd.read_csv(file_name)

    df["gross_amount"] = df["quantity"] * df["unit_price"]
    df["net_amount"] = df["gross_amount"] * (1 - df["discount_pct"] / 100)
    df["is_high_value"] = df["net_amount"] > 50_000

    df.to_csv(file_name)
    print(df)