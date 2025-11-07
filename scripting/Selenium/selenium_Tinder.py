from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ---------------------------- SETUP ------------------------------- #
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

driver.get("https://tinder.com")

# ---------------------------- LOGIN MANUALLY ------------------------------- #
print("⏳ Please log in manually (Google/Facebook/Phone) within 60 seconds...")
time.sleep(60)  # Give user time to log in manually

# ---------------------------- SWIPE LOOP ------------------------------- #
def swipe_right():
    try:
        like_button = driver.find_element(By.XPATH, '//button[@aria-label="Like"]')
        like_button.click()
        print("👉 Swiped right")
    except:
        print("⚠️ Like button not found")

def swipe_left():
    try:
        dislike_button = driver.find_element(By.XPATH, '//button[@aria-label="Nope"]')
        dislike_button.click()
        print("👈 Swiped left")
    except:
        print("⚠️ Dislike button not found")

# ---------------------------- AUTO SWIPE ------------------------------- #
for _ in range(20):  # Swipe 20 times
    swipe_right()
    time.sleep(2)

# ---------------------------- CLEANUP ------------------------------- #
time.sleep(5)
driver.quit()