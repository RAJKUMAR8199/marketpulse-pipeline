import pandas as pd
import json
from sqlalchemy import create_engine

# Load raw JSON data
with open("data/raw_jobs.json") as file:
    jobs = json.load(file)

# Convert to DataFrame
df = pd.DataFrame(jobs)

print("Original rows:", len(df))

# Handle missing values
df["company"] = df["company"].fillna("Unknown")

df["position"] = df["position"].fillna("Unknown")

df["location"] = df["location"].fillna("Remote")

# Remove duplicates
df.drop_duplicates(inplace=True)

print("Rows after cleaning:", len(df))

# Save cleaned CSV
df.to_csv("data/cleaned_jobs.csv", index=False)

print("Cleaned CSV saved successfully")

# Create SQLite database connection
engine = create_engine("sqlite:///database/jobs.db")

# Store data into database
df.to_sql("jobs", engine, if_exists="replace", index=False)

print("Data stored into SQLite database successfully")