from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import time

# Launch Chrome and open the Dino game
options = webdriver.ChromeOptions()
options.add_argument("disable-infobars")
options.add_argument("--mute-audio")
options.add_argument("--window-size=800,600")
driver = webdriver.Chrome(options=options)
driver.get("chrome://dino")

# Activate the game canvas
body = driver.find_element(By.TAG_NAME, "body")
body.send_keys(Keys.SPACE)

time.sleep(2)  # Let the game start

# Coordinates for obstacle detection (adjust based on screen resolution)
def is_obstacle():
    # Check pixel ahead of dino (x=400, y=450)
    pixel = pyautogui.pixel(400, 450)
    return pixel[0] < 100  # Dark pixel means obstacle

# Main loop
try:
    while True:
        if is_obstacle():
            pyautogui.press("up")  # Jump
        time.sleep(0.05)
except KeyboardInterrupt:
    print("🛑 Bot stopped.")
    driver.quit()