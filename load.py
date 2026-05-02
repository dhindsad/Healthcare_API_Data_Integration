import pandas as pd
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

processed_file = BASE_DIR / "data" / "processed" / "clean_api_health_data.csv"
database_file = BASE_DIR / "outputs" / "api_health_database.db"
summary_file = BASE_DIR / "outputs" / "api_health_summary_report.csv"

database_file.parent.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(processed_file)

conn = sqlite3.connect(database_file)

df.to_sql("api_health_data", conn, if_exists="replace", index=False)

summary = pd.DataFrame({
    "total_records": [len(df)],
    "total_columns": [len(df.columns)],
    "duplicate_rows": [df.duplicated().sum()]
})

summary.to_csv(summary_file, index=False)

conn.close()

print("API health data loaded successfully.")
print("Database created:", database_file)
print("Summary report created:", summary_file)
print(summary)