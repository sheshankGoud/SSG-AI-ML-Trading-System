import sqlite3
import pandas as pd

DB = "data/market_data.db"

conn = sqlite3.connect(DB)

df = pd.read_sql(
    """
    SELECT
        id,
        timestamp,
        symbol,
        prediction,
        confidence,
        entry_price,
        evaluation_time,
        exit_price,
        future_return,
        actual_target,
        correct,
        evaluated
    FROM ml_predictions
    ORDER BY id
    """,
    conn
)

print("\n=== ML PREDICTION EVALUATION ===")

if df.empty:
    print("No predictions found.")

else:
    print(df.to_string(index=False))

    evaluated = df[df["evaluated"] == 1]

    print("\n=== SUMMARY ===")

    print("Total predictions :", len(df))
    print("Evaluated          :", len(evaluated))

    if not evaluated.empty:

        correct = int(evaluated["correct"].sum())
        success_rate = evaluated["correct"].mean()

        print("Correct            :", correct)
        print("Incorrect          :", len(evaluated) - correct)
        print("Success rate       :", f"{success_rate:.2%}")

        print("\n=== ACTUAL TARGET DISTRIBUTION ===")
        print(
            evaluated["actual_target"]
            .value_counts()
            .to_string()
        )

        print("\n=== PREDICTION DISTRIBUTION ===")
        print(
            evaluated["prediction"]
            .value_counts()
            .to_string()
        )

conn.close()