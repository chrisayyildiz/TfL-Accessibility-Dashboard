# Transport for London Accessibility Dashboard

A tool designed to identify, track, and visualise disruption data related to accessibility across the Transport for London (TfL) network.

## The Problem

For many passengers with accessibility needs, being informed about a station's step-free status is a hassle. All too often people only find out lifts are out of service when they reach a station, delaying their journey and causing undue stress.

Watch the video below:

<a href="https://www.youtube.com/watch?v=EZS0XN-p6jE" target="_blank">
  <img src="https://github.com/user-attachments/assets/c5f18e45-37d0-4362-a542-63ac3a5afd8a" alt="Watch the AccessTransport video" width="800">
</a>

---

While Transport for London (TfL) does publish accessibility and disruption information, it is often:
- Hard to navigate in real-time
- Not centralised for accessibility-specific concerns
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

## Development Phases
- [x] **Phase One:** Deploy project to a Streamlit dashboard
- [ ] **Phase Two:** Migrate project to a unified app for enhanced usability and notifications
