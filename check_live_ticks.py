import sqlite3
import pandas as pd

DB = "data/market_data.db"

conn = sqlite3.connect(DB)

query = """
SELECT
    symbol,
    COUNT(*) AS tick_count,
    MIN(time) AS first_tick,
    MAX(time) AS latest_tick
FROM ticks
GROUP BY symbol
ORDER BY tick_count DESC
"""

df = pd.read_sql(query, conn)

print("\n=== LIVE TICK DATABASE CHECK ===")

if df.empty:
    print("No ticks found in database.")
else:
    print(df.to_string(index=False))
    print("\n=== TOTAL LIVE TICKS ===")
    print(df["tick_count"].sum())

print("\n=== LATEST 10 TICKS ===")

latest = pd.read_sql("""
    SELECT *
    FROM ticks
    ORDER BY id DESC
    LIMIT 10
""", conn)

print(latest.to_string(index=False))

conn.close()