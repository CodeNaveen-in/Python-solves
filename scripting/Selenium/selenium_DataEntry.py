import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# ---------------------------- SETUP ------------------------------- #
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

FORM_URL = "https://example.com/form"  # Replace with actual form URL
driver.get(FORM_URL)
time.sleep(3)

# ---------------------------- READ CSV ------------------------------- #
with open("data.csv", newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Fill form fields (update selectors as needed)
        driver.find_element(By.NAME, "name").clear()
        driver.find_element(By.NAME, "name").send_keys(row["Name"])

        driver.find_element(By.NAME, "email").clear()
        driver.find_element(By.NAME, "email").send_keys(row["Email"])

        driver.find_element(By.NAME, "phone").clear()
        driver.find_element(By.NAME, "phone").send_keys(row["Phone"])

        driver.find_element(By.NAME, "message").clear()
        driver.find_element(By.NAME, "message").send_keys(row["Message"])

        # Submit form
        driver.find_element(By.ID, "submit-button").click()
        print(f"✅ Submitted: {row['Name']}")
        time.sleep(5)  # Wait before next entry

# ---------------------------- CLEANUP ------------------------------- #
driver.quit()