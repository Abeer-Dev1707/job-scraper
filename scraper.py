import requests
from bs4 import BeautifulSoup
import json
import time

all_jobs = []

# عدد الصفحات اللي نريد نزورها (مثلاً 50 صفحة = تقريباً آلاف الوظائف)
for page in range(1, 51):
    url = f"https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&cboWorkExp1=0&pDate=I&sequence={page}&startPage=1"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

    if not jobs:  # لو الصفحة فاضية نوقف
        print(f"🔴 ما في وظائف بالصفحة {page}، وقفنا.")
        break

    for job in jobs:
        job_title = job.find("h2").text.strip() if job.find("h2") else "N/A"
        company = job.find("h3", class_="joblist-comp-name")
        company = company.text.strip() if company else "N/A"
        skills = job.find("span", class_="srp-skills")
        skills = skills.text.strip() if skills else "N/A"
        more_info = job.header.h2.a['href'] if job.header and job.header.h2 and job.header.h2.a else "N/A"

        all_jobs.append({
            "title": job_title,
            "company": company,
            "skills": skills,
            "link": more_info
        })

    print(f"✅ الصفحة {page} تمت، إجمالي الوظائف حتى الآن: {len(all_jobs)}")

    time.sleep(2)  # نريح شوي علشان ما يوقفنا الموقع

# حفظ في JSON
with open("jobs.json", "w", encoding="utf-8") as f:
    json.dump(all_jobs, f, ensure_ascii=False, indent=4)

print(f"🎉 تم جمع {len(all_jobs)} وظيفة وحفظها في jobs.json")
