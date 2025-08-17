import requests
from bs4 import BeautifulSoup
import json

URL = "https://realpython.github.io/fake-jobs/"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

jobs = []
for job in soup.find_all("div", class_="card-content"):
    title = job.find("h2", class_="title").get_text(strip=True)
    company = job.find("h3", class_="company").get_text(strip=True)
    location = job.find("p", class_="location").get_text(strip=True)
    jobs.append({
        "title": title,
        "company": company,
        "location": location
    })

with open("jobs.json", "w", encoding="utf-8") as f:
    json.dump(jobs, f, indent=2, ensure_ascii=False)

print(f"✅ Extracted {len(jobs)} jobs and saved to jobs.json")
