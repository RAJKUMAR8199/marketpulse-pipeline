import requests
import json

url = "https://remoteok.com/api"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

print("Total records:", len(data))

jobs = []

for item in data[1:]:

    job = {
        "company": item.get("company", "Unknown"),
        "position": item.get("position", "Unknown"),
        "location": item.get("location", "Remote")
    }

    jobs.append(job)

with open("data/raw_jobs.json", "w") as file:
    json.dump(jobs, file, indent=4)

print("Data saved successfully")
print("Total jobs stored:", len(jobs))