import sqlite3
import pandas as pd

DB = "data/market_data.db"

conn = sqlite3.connect(DB)

df = pd.read_sql(
    """
    SELECT
        time,
        symbol,
        ltp,
        ltq,
        bid_price,
        ask_price
    FROM ticks
    WHERE symbol = ?
    ORDER BY id DESC
    LIMIT 30
    """,
    conn,
    params=("NSE:WIPRO-EQ",)
)

print("\n=== LATEST WIPRO LIVE TICKS ===")

print(
    df.to_string(index=False)
)

print("\n=== UNIQUE LTP VALUES ===")

print(
    df["ltp"].value_counts()
)

conn.close()