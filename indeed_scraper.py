from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import csv

# Setup Chrome options
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--log-level=3")

# Start the WebDriver
driver = webdriver.Chrome(options=options)

# Base URL
base_url = "https://pk.indeed.com/"

job_data = []

# Loop through multiple pages
for page in range(0, 3):  # 3 pages
    url = f"{base_url}&start={page * 10}"
    driver.get(url)
    time.sleep(5)  # Wait for the page to load

    job_cards = driver.find_elements(By.CSS_SELECTOR, "div")

    for job in job_cards:
        try:
            title = job.find_element(By.CSS_SELECTOR, "h2").text.strip()
            company = job.find_element(By.CSS_SELECTOR, "a").text.strip()
            location = job.find_element(By.CSS_SELECTOR, "div").text.strip()

            job_data.append([title, company, location])
        except Exception as e:
            print("Error reading job:", e)
            continue

    time.sleep(2)

# Save to CSV
with open("jobs_indeed.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Location"])
    writer.writerows(job_data)

print(" Indeed scraping complete! Data saved to jobs_indeed.csv")

# Close browser
driver.quit()