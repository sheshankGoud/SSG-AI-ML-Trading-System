import sqlite3

conn = sqlite3.connect("data/market_data.db")

result = conn.execute(
    "SELECT MAX(timestamp) FROM candles WHERE symbol = ?",
    ("NSE:WIPRO-EQ",)
).fetchone()

print("Latest WIPRO candle:", result[0])

conn.close()