from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import csv

# Setup Chrome options for headless operation
options = Options()
options.add_argument("--headless")  # Optional: Run browser in background
options.add_argument("--disable-gpu")

# Start the WebDriver (Make sure chromedriver is in PATH or provide its path)
driver = webdriver.Chrome(options=options)

# Navigate to Rozee.pk
driver.get("https://www.rozee.pk/job/jsearch/q/all")

# Wait for the page to fully load
time.sleep(5)

# Extract job listings
jobs = driver.find_elements(By.CSS_SELECTOR, "div.job")

job_data = []

for job in jobs:
    try:
        title_elem = job.find_element(By.CSS_SELECTOR, "h3.s-18")
        title = title_elem.get_attribute("title").strip()

        company_elem = job.find_element(By.CSS_SELECTOR, "a.display-inline")
        company = company_elem.text.strip()

        location_elem = job.find_element(By.CSS_SELECTOR, "a.display-inline")
        location = location_elem.text.strip()

        date_elem = job.find_element(By.CSS_SELECTOR, "span")
        date_posted = date_elem.text.strip()

        job_data.append([title, company, location, date_posted])
    except Exception as e:
        print("Error extracting job:", e)

# Save to CSV
with open("rozee_jobs.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Location", "Date Posted"])
    writer.writerows(job_data)

print("Data saved to rozee_jobs.csv")

# Close the browser
driver.quit()