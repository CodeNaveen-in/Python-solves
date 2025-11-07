from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ---------------------------- CONFIG ------------------------------- #
EXPECTED_SPEED = 100  # Mbps
TWITTER_URL = "https://twitter.com/login"
USERNAME = "your_twitter_username"
PASSWORD = "your_twitter_password"

# ---------------------------- SETUP ------------------------------- #
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# ---------------------------- RUN SPEEDTEST ------------------------------- #
driver.get("https://www.speedtest.net")
time.sleep(5)
driver.find_element(By.CLASS_NAME, "start-text").click()
time.sleep(45)  # Wait for test to complete

speed_element = driver.find_element(By.CLASS_NAME, "download-speed")
download_speed = float(speed_element.text)
print(f"📶 Download speed: {download_speed} Mbps")

# ---------------------------- COMPLAINT LOGIC ------------------------------- #
if download_speed < EXPECTED_SPEED:
    complaint = f"Hey ISP, I'm paying for {EXPECTED_SPEED} Mbps but getting only {download_speed} Mbps. Please fix this! #InternetSpeed #Complaint"

    # ---------------------------- LOGIN TO TWITTER ------------------------------- #
    driver.get(TWITTER_URL)
    time.sleep(5)
    driver.find_element(By.NAME, "text").send_keys(USERNAME)
    driver.find_element(By.NAME, "text").send_keys(Keys.ENTER)
    time.sleep(3)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
    time.sleep(5)

    # ---------------------------- POST TWEET ------------------------------- #
    tweet_box = driver.find_element(By.CSS_SELECTOR, "div[aria-label='Tweet text']")
    tweet_box.send_keys(complaint)
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[@data-testid='tweetButtonInline']").click()
    print("✅ Complaint tweeted!")

else:
    print("✅ Speed is acceptable. No complaint needed.")

# ---------------------------- CLEANUP ------------------------------- #
time.sleep(5)
driver.quit()