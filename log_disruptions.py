import requests
import pandas as pd
from datetime import datetime
import os

# TfL API endpoint
url = "https://api.tfl.gov.uk/Line/Mode/tube/Disruption"
data = requests.get(url).json()

# Keywords to flag accessibility issues
accessibility_keywords = ["step-free", "accessibility", "lift", "escalator"]

rows = []
now = datetime.now()

for d in data:
    description = d.get("description", "").lower()
    is_accessibility_issue = any(kw in description for kw in accessibility_keywords)

    rows.append({
        "datetime": now,
        "line": d["lineName"],
        "category": d["category"],
        "severity": d["categoryDescription"],
        "is_step_free_related": is_accessibility_issue
    })

df = pd.DataFrame(rows)

# Ensure directory exists
os.makedirs("data", exist_ok=True)
file_path = "data/disruptions_log.csv"

# Append or create file
if os.path.exists(file_path):
    df.to_csv(file_path, mode="a", header=False, index=False)
else:
    df.to_csv(file_path, index=False)
