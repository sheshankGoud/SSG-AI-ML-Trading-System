import sqlite3

DB = "data/market_data.db"

conn = sqlite3.connect(DB)

indexes = conn.execute(
    "PRAGMA index_list(ml_predictions)"
).fetchall()

print("\n=== ML PREDICTION INDEXES ===")

for index in indexes:
    print(index)

conn.close()