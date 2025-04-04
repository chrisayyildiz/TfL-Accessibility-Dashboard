import requests
import pandas as pd
from datetime import datetime
import os

url = "https://api.tfl.gov.uk/Line/Mode/tube/Disruption"
data = requests.get(url).json()

rows = []
now = datetime.now()

for d in data:
    rows.append({
        "datetime": now,
        "line": d["lineName"],
        "category": d["category"],
        "severity": d["categoryDescription"]
    })

df = pd.DataFrame(rows)

os.makedirs("data", exist_ok=True)
file_path = "data/disruptions_log.csv"

# Append or create file
if os.path.exists(file_path):
    df.to_csv(file_path, mode="a", header=False, index=False)
else:
    df.to_csv(file_path, index=False)
