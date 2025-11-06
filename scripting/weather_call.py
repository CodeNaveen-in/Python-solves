import requests
from twilio.rest import Client

# ---------------------------- CONFIG ------------------------------- #
API_KEY = "your_openweather_api_key"
CITY = "Delhi"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

TWILIO_ACCOUNT_SID = "your_twilio_account_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE_NUMBER = "+1234567890"  # Your Twilio number
TO_PHONE_NUMBER = "+91xxxxxxxxxx"   # Your verified phone number

# ---------------------------- CHECK WEATHER ------------------------------- #
def check_rain():
    try:
        response = requests.get(URL)
        response.raise_for_status()
        data = response.json()

        weather_conditions = [w["main"].lower() for w in data["weather"]]
        if "rain" in weather_conditions:
            send_sms("🌧️ It's raining in Delhi. Don't forget your umbrella!")
        else:
            print("☀️ No rain right now.")
    except Exception as e:
        print(f"❌ Error fetching weather: {e}")

# ---------------------------- SEND SMS ------------------------------- #
def send_sms(message):
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=TO_PHONE_NUMBER
        )
        print("✅ SMS sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send SMS: {e}")

# ---------------------------- RUN ------------------------------- #
if __name__ == "__main__":
    check_rain()