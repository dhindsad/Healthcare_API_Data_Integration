import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

processed_file = BASE_DIR / "data" / "processed" / "clean_api_health_data.csv"

df = pd.read_csv(processed_file)

print("Running API health data validation checks...")

missing_values = df.isnull().sum()
duplicates = df.duplicated().sum()

print("\nRows and columns:", df.shape)
print("\nMissing values:")
print(missing_values)

print("\nDuplicate rows:", duplicates)

if len(df) > 0 and duplicates == 0:
    print("\nValidation passed. Data is ready for reporting.")
else:
    print("\nValidation warning. Please review data quality issues.")