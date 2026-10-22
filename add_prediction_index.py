import sqlite3

DB = "data/market_data.db"

conn = sqlite3.connect(DB)

conn.execute("""
    CREATE UNIQUE INDEX IF NOT EXISTS
    idx_unique_ml_prediction
    ON ml_predictions (
        timestamp,
        symbol,
        model_version
    )
""")

conn.commit()

print("Unique prediction index created.")

conn.close()