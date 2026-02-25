# 🔐 NVD – CVE API
# A RESTful API built using Python Flask and MySQL to retrieve and filter CVE (Common Vulnerabilities and Exposures) data from the NVD dataset.
---


## 📌 Overview

This project provides an API endpoint to:

Retrieve all CVEs

Filter CVEs by year

Filter by minimum CVSS v3 score

Sort results dynamically (ascending / descending)

Return structured JSON output

Built with:

🐍 Python

🌶 Flask

🛢 MySQL

🔗 SQLAlchemy ORM 

---

## Install Dependencies
pip install -r requirements.txt


<img width="909" height="333" alt="Screenshot 2026-02-25 103709" src="https://github.com/user-attachments/assets/9cfb6012-1595-42ef-8468-3002e0d888b9" />

---


## Queries

<img width="810" height="443" alt="Screenshot 2026-02-25 104506" src="https://github.com/user-attachments/assets/4089b1ee-dff3-4f77-aef0-9086be80837f" />


---

## DB Sync
```bash
http://127.0.0.1:5000/sync
```
<img width="1919" height="1016" alt="Screenshot 2026-02-25 140242" src="https://github.com/user-attachments/assets/2bd3763d-3655-40ce-bc11-9381d81a7d31" />




--- 
## Check cves 
```bash
http://127.0.0.1:5000/api/cves
```

<img width="1209" height="791" alt="image" src="https://github.com/user-attachments/assets/2b2164f3-bdc2-4c52-a919-5e39ff99d1a3" />

---

## Apply Sorting as DESC
```bash
http://127.0.0.1:5000/api/cves?sort=score_v3&order=desc
```

<img width="1230" height="768" alt="image" src="https://github.com/user-attachments/assets/ba215e50-74e3-4eb4-98e2-a942697884ee" />

---


## Check by minimum score 
```bash
http://127.0.0.1:5000/api/cves?min_score=9
```
<img width="1214" height="752" alt="image" src="https://github.com/user-attachments/assets/dfcd4c2b-593f-4f6e-a936-bbd3f83db61f" />

---

## Filter By Year 
```bash
http://127.0.0.1:5000/api/cves?year=1999-0082
```
<img width="600" height="307" alt="image" src="https://github.com/user-attachments/assets/2f0f20cf-7572-44fc-a9de-a60bceb77bfc" />

---

<img width="1919" height="894" alt="Screenshot 2026-02-25 113129" src="https://github.com/user-attachments/assets/6767e531-df91-4a3e-8134-f63a6ff67730" />

---

## 𝒦𝒶𝓋𝒾𝓃𝓀𝓊𝓂𝒶𝓇 𝒩






