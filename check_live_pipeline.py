import sqlite3
import pandas as pd

DB = "data/market_data.db"

conn = sqlite3.connect(DB)

print("\n=== LATEST WIPRO CANDLES ===")

candles = pd.read_sql(
    """
    SELECT
        symbol,
        timestamp,
        open,
        high,
        low,
        close,
        volume
    FROM candles
    WHERE symbol = ?
    ORDER BY timestamp DESC
    LIMIT 5
    """,
    conn,
    params=("NSE:WIPRO-EQ",)
)

print(candles.to_string(index=False))


print("\n=== LATEST ML PREDICTIONS ===")

predictions = pd.read_sql(
    """
    SELECT
        timestamp,
        symbol,
        prediction,
        confidence,
        entry_price,
        evaluated
    FROM ml_predictions
    ORDER BY id DESC
    LIMIT 10
    """,
    conn
)

print(predictions.to_string(index=False))


conn.close()