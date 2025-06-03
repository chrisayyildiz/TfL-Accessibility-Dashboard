# Transport for London Accessibility Dashboard

A tool designed to identify, track, and visualise disruption data related to accessibility across the Transport for London (TfL) network.

## The Problem

For many passengers with accessibility needs, being informed about a station's step-free status is a hassle. All too often people only find out lifts are out of service when they reach a station, delaying their journey and causing undue stress.

https://github.com/user-attachments/assets/c0edcb78-ae45-46cf-9794-15f6a3c167ac

---

While Transport for London (TfL) does publish accessibility and disruption information, it is often:
- Hard to navigate in real-time
- Not centralised for accessibility concerns
- Lacking historical insight into how often disruptions affect certain stations

---

This project addresses the problem by:
- Providing a filterable, visual dashboard of accessibility-related disruptions
- Automating the collection of live data from TfL
- Making real-time and historical insights available in one place
- Notifying users as soon as their station requires steps, and rapidly reroutes them

---

## Tech Stack
- Airflow: DAG scheduling and automation
- Streamlit: Interactive dashboard frontend
- Asyncio + REST APIs: Efficient data collection and backend services
- Pandas: Data processing and transformation
- PostgreSQL: Backend storage

## Station Level Data Collection
Extracted from the TfL Unified API, transformed to feature accessibility markers, and subsequently loaded.

<img width="1229" alt="Screenshot 2025-06-02 at 22 36 29" src="https://github.com/user-attachments/assets/e0baf285-1c77-4d81-9fb3-9db48145c114" />

## Development Phases

### Phase One
- [x] **Phase One:** Deploy project to a Streamlit dashboard

### Phase Two
- [ ] **Phase Two:** Migrate project to a unified app for enhanced usability and notifications
![AccessDashboard](https://github.com/user-attachments/assets/04b41497-f78d-4776-8af5-d1efda6af9a6)

