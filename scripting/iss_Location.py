import requests
from plyer import notification
import time

# ---------------------------- YOUR LOCATION ------------------------------- #
MY_LAT = 28.6702   # Random latitude
MY_LONG = 78.4538  # Random longitude

# ---------------------------- CHECK ISS POSITION ------------------------------- #
def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])

    # Check if ISS is within ±5 degrees of your location
    if (MY_LAT - 5 <= iss_lat <= MY_LAT + 5) and (MY_LONG - 5 <= iss_long <= MY_LONG + 5):
        return True
    return False

# ---------------------------- NOTIFY ------------------------------- #
def notify_user():
    notification.notify(
        title="🚀 Look Up!",
        message="The ISS is passing overhead. Go outside and take a look!",
        timeout=10
    )

# ---------------------------- LOOP ------------------------------- #
while True:
    try:
        if is_iss_overhead():
            notify_user()
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(60)