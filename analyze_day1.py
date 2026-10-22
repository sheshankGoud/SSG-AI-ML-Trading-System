import sqlite3
import pandas as pd

DB = "data/market_data.db"
DATE = "2026-08-25"

conn = sqlite3.connect(DB)

query = """
SELECT
    prediction,
    actual_target,
    confidence,
    future_return,
    correct
FROM ml_predictions
WHERE DATE(timestamp) = ?
AND evaluated = 1
"""

df = pd.read_sql(
    query,
    conn,
    params=(DATE,)
)

conn.close()

print()
print("=" * 60)
print(f"DAY 1 ML EVALUATION - {DATE}")
print("=" * 60)

if df.empty:
    print("No evaluated predictions found.")
    raise SystemExit

# ------------------------------------------------
# BASIC SUMMARY
# ------------------------------------------------

print()
print("=== BASIC SUMMARY ===")

print(f"Evaluated predictions : {len(df)}")
print(f"Correct predictions   : {int(df['correct'].sum())}")
print(
    f"Overall success rate  : "
    f"{df['correct'].mean():.2%}"
)

# ------------------------------------------------
# PREDICTION DISTRIBUTION
# ------------------------------------------------

print()
print("=== PREDICTION DISTRIBUTION ===")

print(
    df["prediction"]
    .value_counts()
    .to_string()
)

# ------------------------------------------------
# ACTUAL DISTRIBUTION
# ------------------------------------------------

print()
print("=== ACTUAL TARGET DISTRIBUTION ===")

print(
    df["actual_target"]
    .value_counts()
    .to_string()
)

# ------------------------------------------------
# CONFUSION MATRIX
# ------------------------------------------------

print()
print("=== CONFUSION MATRIX ===")

matrix = pd.crosstab(
    df["prediction"],
    df["actual_target"]
)

print(matrix)

# ------------------------------------------------
# PERFORMANCE BY PREDICTION
# ------------------------------------------------

print()
print("=== SUCCESS BY PREDICTION ===")

performance = (
    df.groupby("prediction")["correct"]
    .agg(
        signals="count",
        correct="sum",
        success_rate="mean"
    )
)

performance["success_rate"] = (
    performance["success_rate"] * 100
)

print(performance.to_string())

# ------------------------------------------------
# RETURN ANALYSIS
# ------------------------------------------------

print()
print("=== RETURN ANALYSIS ===")

print(
    df["future_return"]
    .describe()
    .to_string()
)

print()
print(
    f"Average future return : "
    f"{df['future_return'].mean():.4%}"
)

# ------------------------------------------------
# BUY / SELL RETURN
# ------------------------------------------------

print()
print("=== RETURN BY PREDICTION ===")

return_by_prediction = (
    df.groupby("prediction")["future_return"]
    .agg(
        signals="count",
        average_return="mean"
    )
)

return_by_prediction["average_return"] = (
    return_by_prediction["average_return"] * 100
)

print(return_by_prediction.to_string())

# ------------------------------------------------
# CONFIDENCE BUCKETS
# ------------------------------------------------

print()
print("=== CONFIDENCE BUCKETS ===")

df["confidence_bucket"] = pd.cut(
    df["confidence"],
    bins=[0, 0.5, 0.6, 0.7, 0.8, 1.0],
    labels=[
        "<50%",
        "50-60%",
        "60-70%",
        "70-80%",
        "80%+"
    ],
    include_lowest=True
)

confidence = (
    df.groupby(
        "confidence_bucket",
        observed=False
    )["correct"]
    .agg(
        signals="count",
        correct="sum",
        success_rate="mean"
    )
)

confidence["success_rate"] = (
    confidence["success_rate"] * 100
)

print(
    confidence.to_string()
)

# ------------------------------------------------
# ACTIONABLE SIGNALS
# ------------------------------------------------

signals = df[
    df["prediction"].isin(["BUY", "SELL"])
]

print()
print("=== ACTIONABLE SIGNALS ===")

print(
    f"BUY/SELL signals : {len(signals)}"
)

if not signals.empty:

    print(
        f"Correct signals  : "
        f"{int(signals['correct'].sum())}"
    )

    print(
        f"Signal success    : "
        f"{signals['correct'].mean():.2%}"
    )

    print(
        f"Average return    : "
        f"{signals['future_return'].mean():.4%}"
    )

print()
print("=" * 60)
print("DAY 1 ANALYSIS COMPLETE")
print("=" * 60)