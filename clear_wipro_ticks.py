import sqlite3

DB = "data/market_data.db"

conn = sqlite3.connect(DB)

cursor = conn.execute(
    "DELETE FROM ticks WHERE symbol = ?",
    ("NSE:WIPRO-EQ",)
)

conn.commit()

print("Deleted WIPRO live ticks:", cursor.rowcount)

conn.close()