import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from datetime import datetime
from data_fetcher import get_line_status, get_accessibility_alerts, plan_accessible_journey, get_station_history
from notification import send_notification

st.set_page_config(layout="wide")
st.title("♿ AccessTransport: TfL Accessibility Dashboard")

# Load Live Disruption Data
line_status = get_line_status()
accessibility_alerts = get_accessibility_alerts()

# User Journey Planner
st.markdown("---")
st.subheader("🧭 Plan Your Accessible Journey")

from_station = st.text_input("From Station")
to_station = st.text_input("To Station")
access_pref = st.selectbox("Accessibility Preference", ["stepFreeToVehicle", "stepFreeToPlatform", "noPreference"])

if st.button("Plan Journey"):
    journey = plan_accessible_journey(from_station, to_station, access_pref)
    if journey:
        st.success("Accessible Journey Found")
        for leg in journey:
            st.markdown(f"- **{leg['instruction']}** ({leg['duration']} mins)")
            if leg.get("accessibilityIssue"):
                st.warning(f"⚠️ {leg['accessibilityIssue']}")
    else:
        st.error("No accessible route found or API error.")

# Alert User of Lift Outages
st.markdown("---")
st.subheader("🔔 Lift Outage Alerts")

user_interchange = st.text_input("Enter Interchange Station to Monitor")
notify = st.button("Check & Notify")

if notify and user_interchange:
    outage_alerts = [a for a in accessibility_alerts if user_interchange.lower() in a['description'].lower()]
    if outage_alerts:
        st.error(f"Lift outage found at {user_interchange}. Sending mobile notification...")
        send_notification(
            title="Lift Outage Alert",
            body=f"Step-free access unavailable at {user_interchange}. Consider rerouting."
        )
    else:
        st.success(f"No lift outage currently reported at {user_interchange}.")

# Live Line Status & Accessibility Alerts
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.subheader("🚇 Live Line Status")
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

# Historical Station Data
st.markdown("---")
st.subheader("📊 Station Accessibility History")
station_select = st.text_input("Station Name for History Analysis")

if station_select:
    history_df = get_station_history(station_select)
    if not history_df.empty:
        fig = px.bar(history_df, x="date", y="lift_outage_minutes", title=f"Lift Outage History for {station_select}")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No historical data found for this station.")
