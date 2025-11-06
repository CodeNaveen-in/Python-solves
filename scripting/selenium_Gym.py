from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ---------------------------- CONFIG ------------------------------- #
GYM_URL = "https://yourgymwebsite.com/login"
USERNAME = "your_email@example.com"
PASSWORD = "your_password"
DESIRED_SLOT = "6:00 AM - 7:00 AM"

# ---------------------------- SETUP ------------------------------- #
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get(GYM_URL)

# ---------------------------- LOGIN ------------------------------- #
time.sleep(2)
driver.find_element(By.ID, "email").send_keys(USERNAME)
driver.find_element(By.ID, "password").send_keys(PASSWORD)
driver.find_element(By.ID, "login-button").click()

# ---------------------------- NAVIGATE TO BOOKING ------------------------------- #
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Book Slot").click()

# ---------------------------- SELECT SLOT ------------------------------- #
time.sleep(2)
slots = driver.find_elements(By.CLASS_NAME, "slot-time")
for slot in slots:
    if DESIRED_SLOT in slot.text:
        slot.click()
        break

# ---------------------------- CONFIRM BOOKING ------------------------------- #
time.sleep(1)
driver.find_element(By.ID, "confirm-button").click()
print("✅ Gym slot booked successfully!")

# ---------------------------- CLEANUP ------------------------------- #
time.sleep(5)
driver.quit()