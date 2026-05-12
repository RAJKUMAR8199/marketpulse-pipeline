from fastapi import FastAPI
from sqlalchemy import create_engine
import pandas as pd

# Create FastAPI app
app = FastAPI(
    title="MarketPulse API",
    description="B2B Job Intelligence Pipeline API",
    version="1.0.0"
)

# Connect to SQLite database
engine = create_engine("sqlite:///database/jobs.db")


# Home Route
@app.get("/")
def home():
    return {
        "message": "MarketPulse API Running Successfully"
    }


# Get Jobs Endpoint
@app.get("/jobs")
def get_jobs(limit: int = 20):

    query = f"SELECT * FROM jobs LIMIT {limit}"

    df = pd.read_sql(query, engine)

    return df.to_dict(orient="records")


# Top Hiring Locations Endpoint
@app.get("/insights")
def insights():

    query = "SELECT * FROM jobs"

    df = pd.read_sql(query, engine)

    top_locations = df["location"].value_counts().head(5)

    return {
        "top_hiring_locations": top_locations.to_dict()
    }


# Top Companies Endpoint
@app.get("/top-companies")
def top_companies():

    query = "SELECT company FROM jobs"

    df = pd.read_sql(query, engine)

    top_companies = df["company"].value_counts().head(10)

    return {
        "top_companies": top_companies.to_dict()
    }


# Top Job Roles Endpoint
@app.get("/top-roles")
def top_roles():

    query = "SELECT position FROM jobs"

    df = pd.read_sql(query, engine)

    top_roles = df["position"].value_counts().head(10)

    return {
        "top_roles": top_roles.to_dict()
    }