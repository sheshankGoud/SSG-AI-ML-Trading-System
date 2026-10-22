import sqlite3
import pandas as pd
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    balanced_accuracy_score,
    f1_score,
    precision_score,
    recall_score,
)

DB = "data/market_data.db"

conn = sqlite3.connect(DB)

df = pd.read_sql_query("""
    SELECT
        prediction,
        actual_target,
        confidence,
        future_return
    FROM ml_predictions
    WHERE evaluated = 1
      AND actual_target IS NOT NULL
    ORDER BY id
""", conn)

conn.close()

print("\n=== MODEL V1 ANALYSIS ===")
print(f"Evaluated samples : {len(df)}")

labels = ["BUY", "HOLD", "SELL"]

print("\n=== CONFUSION MATRIX ===")
cm = confusion_matrix(
    df["actual_target"],
    df["prediction"],
    labels=labels
)

cm_df = pd.DataFrame(
    cm,
    index=[f"Actual {x}" for x in labels],
    columns=[f"Pred {x}" for x in labels]
)

print(cm_df)

print("\n=== CLASSIFICATION REPORT ===")
print(
    classification_report(
        df["actual_target"],
        df["prediction"],
        labels=labels,
        zero_division=0
    )
)

print("\n=== BALANCED ACCURACY ===")
print(
    f"{balanced_accuracy_score(df['actual_target'], df['prediction']):.4f}"
)

print("\n=== MACRO F1 ===")
print(
    f"{f1_score(df['actual_target'], df['prediction'], labels=labels, average='macro', zero_division=0):.4f}"
)

print("\n=== PREDICTION COUNTS ===")
print(df["prediction"].value_counts())

print("\n=== ACTUAL COUNTS ===")
print(df["actual_target"].value_counts())

print("\n=== CONFIDENCE BY PREDICTION ===")
print(
    df.groupby("prediction")["confidence"]
      .agg(["count", "mean", "min", "max"])
)

print("\n=== BUY PREDICTIONS ===")

buy = df[df["prediction"] == "BUY"]

if len(buy):
    print(f"BUY predictions : {len(buy)}")
    print(
        f"Actual BUY      : {(buy['actual_target'] == 'BUY').sum()}"
    )
    print(
        f"BUY precision    : {(buy['actual_target'] == 'BUY').mean():.4f}"
    )
else:
    print("No BUY predictions.")

print("\n=== SELL PREDICTIONS ===")

sell = df[df["prediction"] == "SELL"]

if len(sell):
    print(f"SELL predictions : {len(sell)}")
    print(
        f"Actual SELL      : {(sell['actual_target'] == 'SELL').sum()}"
    )
    print(
        f"SELL precision    : {(sell['actual_target'] == 'SELL').mean():.4f}"
    )
else:
    print("No SELL predictions.")

print("\n=== ALWAYS-HOLD BASELINE ===")

always_hold_accuracy = (
    df["actual_target"] == "HOLD"
).mean()

print(
    f"Always HOLD accuracy : {always_hold_accuracy:.4f}"
)

print("\n=== RETURN STATISTICS ===")
print(
    df.groupby("actual_target")["future_return"]
      .agg(["count", "mean", "min", "max"])
)

print("\nAnalysis complete.")