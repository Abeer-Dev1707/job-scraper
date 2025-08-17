import requests
import json
from datetime import datetime

def scrape_jobs():
    # رابط API وهمي (بدليه بالرابط الصحيح لاحقاً)
    url = "https://remoteok.com/api"

    response = requests.get(url)
    jobs = response.json()

    # نحفظ البيانات في ملف jobs.json داخل مجلد data
    data = []
    for job in jobs[1:10]:  # ناخذ أول 10 وظائف كمثال
        data.append({
            "title": job.get("position"),
            "company": job.get("company"),
            "location": job.get("location"),
            "date": job.get("date"),
        })

    # إنشاء مجلد data إذا ما كان موجود
    import os
    if not os.path.exists("data"):
        os.makedirs("data")

    with open("data/jobs.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"تم حفظ {len(data)} وظيفة في data/jobs.json")

if __name__ == "__main__":
    scrape_jobs()
