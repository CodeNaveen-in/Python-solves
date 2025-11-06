from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ---------------------------- CONFIG ------------------------------- #
USERNAME = "your_username"
PASSWORD = "your_password"
INFLUENCERS = ["influencer1", "influencer2", "influencer3"]  # Instagram usernames

# ---------------------------- SETUP ------------------------------- #
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get("https://www.instagram.com/accounts/login/")

# ---------------------------- LOGIN ------------------------------- #
time.sleep(5)
driver.find_element(By.NAME, "username").send_keys(USERNAME)
driver.find_element(By.NAME, "password").send_keys(PASSWORD)
driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)

time.sleep(10)  # Wait for login and popups

# ---------------------------- FOLLOW LOOP ------------------------------- #
for user in INFLUENCERS:
    driver.get(f"https://www.instagram.com/{user}/")
    time.sleep(5)
    try:
        follow_button = driver.find_element(By.XPATH, "//button[text()='Follow']")
        follow_button.click()
        print(f"✅ Followed {user}")
    except:
        print(f"⚠️ Already following or button not found: {user}")
    time.sleep(3)

# ---------------------------- CLEANUP ------------------------------- #
time.sleep(5)
driver.quit()