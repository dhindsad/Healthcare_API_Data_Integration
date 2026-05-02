import pandas as pd
import requests
from io import StringIO

url = "https://data.cdc.gov/resource/9bhg-hcku.csv"  

response = requests.get(url)

df = pd.read_csv(StringIO(response.text))

print(df.head())

df.to_csv("data/raw/api_health_data.csv", index=False)