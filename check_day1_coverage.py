import sqlite3

DB = "data/market_data.db"
SYMBOL = "NSE:WIPRO-EQ"
DATE = "2026-08-25"

conn = sqlite3.connect(DB)

print()
print("=" * 60)
print("DAY 1 DATA COVERAGE")
print("=" * 60)

# -----------------------------
# TICKS
# -----------------------------

row = conn.execute(
    """
    SELECT
        MIN(time),
        MAX(time),
        COUNT(*)
    FROM ticks
    WHERE symbol = ?
    AND DATE(time) = ?
    """,
    (SYMBOL, DATE)
).fetchone()

print()
print("=== TICKS ===")
print("First :", row[0])
print("Last  :", row[1])
print("Count :", row[2])

# -----------------------------
# CANDLES
# -----------------------------

row = conn.execute(
    """
    SELECT
        MIN(timestamp),
        MAX(timestamp),
        COUNT(*)
    FROM candles
    WHERE symbol = ?
    AND DATE(timestamp) = ?
    """,
    (SYMBOL, DATE)
).fetchone()

print()
print("=== CANDLES ===")
print("First :", row[0])
print("Last  :", row[1])
print("Count :", row[2])

# -----------------------------
# PREDICTIONS
# -----------------------------

row = conn.execute(
    """
    SELECT
        MIN(timestamp),
        MAX(timestamp),
        COUNT(*)
    FROM ml_predictions
    WHERE symbol = ?
    AND DATE(timestamp) = ?
    """,
    (SYMBOL, DATE)
).fetchone()

print()
print("=== PREDICTIONS ===")
print("First :", row[0])
print("Last  :", row[1])
print("Count :", row[2])

# -----------------------------
# EVALUATED PREDICTIONS
# -----------------------------

row = conn.execute(
    """
    SELECT
        MIN(timestamp),
        MAX(timestamp),
        COUNT(*)
    FROM ml_predictions
    WHERE symbol = ?
    AND DATE(timestamp) = ?
    AND evaluated = 1
    """,
    (SYMBOL, DATE)
).fetchone()

print()
print("=== EVALUATED PREDICTIONS ===")
print("First :", row[0])
print("Last  :", row[1])
print("Count :", row[2])

conn.close()

print()
print("=" * 60)
print("COVERAGE CHECK COMPLETE")
print("=" * 60)