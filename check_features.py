import sqlite3
import pandas as pd

from ml.features import create_features

symbol = "NSE:WIPRO-EQ"

df = create_features(symbol)

print("\n=== DATA QUALITY CHECK ===")

print("Total rows:", len(df))

print("\nRows with missing volume:")
print(
    df[
        df["volume"].isna() |
        (df["volume"] <= 0)
    ][
        ["timestamp", "close", "volume"]
    ].tail(20).to_string(index=False)
)

print("\nRows with zero volume:")
print((df["volume"] == 0).sum())

print("\nRows with negative volume:")
print((df["volume"] < 0).sum())

print("\nFeature missing values:")
print(
    df.isna().sum()
)