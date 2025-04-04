import requests

def get_line_status():
    url = "https://api.tfl.gov.uk/Line/Mode/tube/Status"
    return requests.get(url).json()

def get_accessibility_alerts():
    url = "https://api.tfl.gov.uk/Line/Mode/tube/Disruption"
    data = requests.get(url).json()
    # Filter alerts related to accessibility
    accessibility_keywords = ["step-free", "accessibility", "lift", "escalator"]
    return [
        alert for alert in data
        if any(kw in alert.get("description", "").lower() for kw in accessibility_keywords)
    ]

def get_disruptions():
    url = "https://api.tfl.gov.uk/Line/Mode/tube/Disruption"
    return requests.get(url).json()
