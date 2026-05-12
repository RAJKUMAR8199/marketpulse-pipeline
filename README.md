# MarketPulse – B2B Job Intelligence Pipeline

## Problem Statement

Businesses need real-time hiring intelligence to track:
- competitor hiring trends
- in-demand skills
- top hiring locations
- active hiring companies

This project builds an automated ETL pipeline that collects live job market data, cleans it, stores it in a database, and exposes insights through REST APIs.

---

## Features

- Automated job data collection using RemoteOK API
- Data cleaning and preprocessing pipeline
- SQLite database storage
- REST APIs using FastAPI
- Automated pipeline scheduling
- Hiring insights and analytics endpoints

---

## Tech Stack

- Python
- FastAPI
- Pandas
- SQLite
- SQLAlchemy
- APScheduler
- Requests

---

## Project Structure

marketpulse-pipeline/

├── scraper/

├── cleaning/

├── pipeline/

├── api/

├── data/

├── database/

├── requirements.txt

├── README.md

└── .env.example

---

## Setup Instructions

### Clone Repository

```bash
git clone <your_repo_url>
cd marketpulse-pipeline
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Scraper

```bash
python scraper/scraper.py
```

---

## Run Cleaning Pipeline

```bash
python cleaning/clean.py
```

---

## Run API

```bash
uvicorn api.main:app --reload
```

---

## API Documentation

Open:

http://127.0.0.1:8000/docs

---

## Available Endpoints

### Get Jobs

```bash
GET /jobs
```

### Hiring Insights

```bash
GET /insights
```

### Top Companies

```bash
GET /top-companies
```

### Top Roles

```bash
GET /top-roles
```

---

## Environment Variables

```env
DATABASE_URL=sqlite:///database/jobs.db
SCRAPER_SCHEDULE=6h
API_KEY=optional
```

---

## Future Improvements

- Docker deployment
- PostgreSQL integration
- Skill trend analytics
- Cloud deployment
- Real-time dashboards