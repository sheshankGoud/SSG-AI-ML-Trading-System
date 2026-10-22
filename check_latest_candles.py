import sqlite3
import pandas as pd

conn = sqlite3.connect("data/market_data.db")

df = pd.read_sql(
    """
    SELECT timestamp, close
    FROM candles
    WHERE symbol = ?
    ORDER BY timestamp DESC
    LIMIT 15
    """,
    conn,
    params=("NSE:WIPRO-EQ",)
)

print(df.to_string(index=False))

conn.close()