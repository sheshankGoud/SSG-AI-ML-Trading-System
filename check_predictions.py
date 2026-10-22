import sqlite3

DB = "data/market_data.db"

conn = sqlite3.connect(DB)

result = conn.execute(
    "PRAGMA table_info(ml_predictions)"
).fetchall()

print("\n=== ML PREDICTION TABLE ===")

for column in result:
    print(column)

conn.close()