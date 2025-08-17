import requests
from bs4 import BeautifulSoup
import json

def scrape_jobs(pages=5):
    all_jobs = []
    base_url = "https://realpython.github.io/fake-jobs/"

    for page in range(1, pages+1):
        url = f"{base_url}?page={page}"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"فشل تحميل الصفحة {page}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all("div", class_="card-content")

        for job in jobs:
            title = job.find("h2", class_="title").text.strip()
            company = job.find("h3", class_="company").text.strip()
            location = job.find("p", class_="location").text.strip()
            all_jobs.append({
                "title": title,
                "company": company,
                "location": location
            })

    return all_jobs


if __name__ == "__main__":
    jobs = scrape_jobs(pages=5)  # عدد الصفحات المطلوب سحبه
    print(f"تم استخراج {len(jobs)} وظيفة ✅")

    with open("jobs.json", "w", encoding="utf-8") as f:
        json.dump(jobs, f, ensure_ascii=False, indent=2)
