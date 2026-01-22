# Handling Missing Values
#
# - Randomly introduce missing values in city, payment_mode, and discount_pct.
# - Apply different strategies:
#       - fill categorical with “Unknownˮ
#       - fill numeric with median by category
# - Prove it worked: show missing counts before/after.
#

import pandas as pd
import numpy as np


def insert_nan(dataframe: pd.DataFrame, percent: float, column_name: str) -> None:
    indexes = df.sample(frac=percent).index
    dataframe.loc[indexes, column_name] = np.nan


if __name__ == "__main__":
    df = pd.read_csv("data/orders.csv")

    columns = ["city", "payment_mode", "discount_pct"]

    for column in columns:
        insert_nan(df, 0.2, column)

    print(df.isna().sum())

    categorical_columns = ["city", "payment_mode"]
    df[categorical_columns] = df[categorical_columns].fillna("Unknown")

    df["discount_pct"] = df.groupby("category")["discount_pct"].transform(
        lambda x: x.fillna(x.median())
    )

    print(df.isna().sum())
