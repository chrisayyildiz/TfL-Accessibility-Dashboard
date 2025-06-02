import requests
import pandas as pd
from datetime import datetime
import os

# Fetch disruption data per station
url = "https://api.tfl.gov.uk/StopPoint/Mode/tube/Disruption"
data = requests.get(url).json()

# Keywords for accessibility
accessibility_keywords = ["step-free", "accessibility", "lift", "escalator"]

now = datetime.now()
rows = []

for d in data:
    for affected in d.get("affectedStops", []):
        station_name = affected.get("commonName", "")
        description = d.get("description", "").lower()
        is_access_issue = any(kw in description for kw in accessibility_keywords)

        rows.append({
            "datetime": now,
            "station": station_name,
            "category": d.get("category", ""),
            "severity": d.get("categoryDescription", ""),
            "description": d.get("description", ""),
            "is_step_free_related": is_access_issue
        })

df = pd.DataFrame(rows)

# Save to CSV
os.makedirs("data", exist_ok=True)
file_path = "data/station_disruptions_log.csv"

if os.path.exists(file_path):
    df.to_csv(file_path, mode="a", header=False, index=False)
else:
    df.to_csv(file_path, index=False)
