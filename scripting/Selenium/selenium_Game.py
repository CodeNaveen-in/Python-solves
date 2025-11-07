from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ---------------------------- SETUP ------------------------------- #
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# Replace with your game URL
GAME_URL = "https://play2048.co/"
driver.get(GAME_URL)

time.sleep(2)  # Wait for game to load

# ---------------------------- GAME CONTROL ------------------------------- #
# Focus game container
game_container = driver.find_element(By.TAG_NAME, "body")

# Simulate key presses
moves = [Keys.ARROW_UP, Keys.ARROW_RIGHT, Keys.ARROW_DOWN, Keys.ARROW_LEFT]

for _ in range(50):  # Play 50 moves
    for move in moves:
        game_container.send_keys(move)
        time.sleep(0.2)

# ---------------------------- CLEANUP ------------------------------- #
time.sleep(5)
driver.quit()