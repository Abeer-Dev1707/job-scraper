import requests
from bs4 import BeautifulSoup
import json
import os

URL = "https://realpython.github.io/fake-jobs/"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

jobs = []

for job_element in soup.find_all("div", class_="card-content"):
    title = job_element.find("h2", class_="title").text.strip()
    company = job_element.find("h3", class_="subtitle").text.strip()
    location = job_element.find("p", class_="location").text.strip()
    jobs.append({"title": title, "company": company, "location": location})

# --- 📌 تعديل هنا: نضيف للملف بدلاً من استبداله ---
file_path = "jobs.json"

# إذا الملف موجود، نقرأ محتواه ونضيف عليه
if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            existing_jobs = json.load(f)
        except json.JSONDecodeError:
            existing_jobs = []
else:
    existing_jobs = []

# ندمج الوظائف الجديدة مع القديمة
all_jobs = existing_jobs + jobs

# نحفظ الملف مع كل الوظائف
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(all_jobs, f, indent=2, ensure_ascii=False)

print(f"✅ تمت إضافة {len(jobs)} وظيفة جديدة، المجموع الآن {len(all_jobs)} وظيفة.")
