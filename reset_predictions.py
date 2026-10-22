import sqlite3

DB = "data/market_data.db"

conn = sqlite3.connect(DB)

count = conn.execute(
    "SELECT COUNT(*) FROM ml_predictions"
).fetchone()[0]

conn.execute(
    "DELETE FROM ml_predictions"
)

conn.commit()
conn.close()

print(f"Deleted old ML predictions: {count}")
print("Prediction journal reset.")