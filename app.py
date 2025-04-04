import streamlit as st
import pandas as pd
import plotly.express as px
from data_fetcher import get_line_status, get_accessibility_alerts

st.set_page_config(layout="wide")
st.title("♿ TfL Accessibility Dashboard")

# Load Live Data
line_status = get_line_status()
accessibility_alerts = get_accessibility_alerts()

# Load Historical Data
try:
    df = pd.read_csv("data/disruptions_log.csv", parse_dates=["datetime"])
    daily_trend = df.groupby(df["datetime"].dt.date).size().reset_index(name="disruptions")
except:
    daily_trend = pd.DataFrame(columns=["datetime", "disruptions"])

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔴 Live Line Status")
    for line in line_status:
        status = line["lineStatuses"][0]["statusSeverityDescription"]
        reason = line["lineStatuses"][0].get("reason", "")
        st.markdown(f"**{line['name']}** — {status}")
        if reason:
            st.caption(reason)

with col2:
    st.subheader("♿ Accessibility Alerts")
    if accessibility_alerts:
        for alert in accessibility_alerts:
            st.error(f"{alert['description']}")
    else:
        st.success("No accessibility-related disruptions.")

st.markdown("---")
st.subheader("📊 Historical Disruption Trend")

if not daily_trend.empty:
    fig = px.line(daily_trend, x="datetime", y="disruptions", title="Disruptions Over Time")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.write("No historical data yet — run `log_disruptions.py` to start tracking.")
