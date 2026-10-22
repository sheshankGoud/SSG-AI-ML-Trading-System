import sqlite3
import pandas as pd

conn = sqlite3.connect("data/market_data.db")

query = """
SELECT
    symbol,
    COUNT(*) AS candles,
    MIN(timestamp) AS first_candle,
    MAX(timestamp) AS last_candle
FROM candles
GROUP BY symbol
ORDER BY symbol
"""

df = pd.read_sql(query, conn)

print("\n=== HISTORICAL DATA ===")
print(df.to_string(index=False))

print("\n=== TOTAL CANDLES ===")
print(df["candles"].sum())

conn.close()