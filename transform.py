import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

raw_file = BASE_DIR / "data" / "raw" / "api_health_data.csv"
processed_file = BASE_DIR / "data" / "processed" / "clean_api_health_data.csv"

processed_file.parent.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(raw_file)

# Clean column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)

# Remove duplicate rows
df = df.drop_duplicates()

# Replace blanks/missing values
df = df.fillna("Unknown")

# Save cleaned file
df.to_csv(processed_file, index=False)

print("API health data transformed successfully.")
print("Rows and columns:", df.shape)
print(df.head())
print("\nColumns:")
print(df.columns.tolist())