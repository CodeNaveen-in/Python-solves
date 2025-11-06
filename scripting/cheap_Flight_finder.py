import requests
from twilio.rest import Client
from datetime import datetime, timedelta

# ---------------------------- CONFIG ------------------------------- #
TEQUILA_API_KEY = "your_tequila_api_key"
TWILIO_SID = "your_twilio_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE = "+1234567890"
TO_PHONE = "+91xxxxxxxxxx"

ORIGIN = "DEL"
DESTINATION = "DXB"
MAX_PRICE = 15000  # INR
DATE_FROM = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
DATE_TO = (datetime.now() + timedelta(days=30)).strftime("%d/%m/%Y")

# ---------------------------- SEARCH FLIGHTS ------------------------------- #
def search_flights():
    url = "https://api.tequila.kiwi.com/v2/search"
    headers = {"apikey": TEQUILA_API_KEY}
    params = {
        "fly_from": ORIGIN,
        "fly_to": DESTINATION,
        "date_from": DATE_FROM,
        "date_to": DATE_TO,
        "curr": "INR",
        "price_to": MAX_PRICE,
        "limit": 1,
        "sort": "price"
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()["data"]
    return data[0] if data else None

# ---------------------------- SEND SMS ------------------------------- #
def send_sms(message):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        body=message,
        from_=TWILIO_PHONE,
        to=TO_PHONE
    )

# ---------------------------- MAIN ------------------------------- #
if __name__ == "__main__":
    flight = search_flights()
    if flight:
        price = flight["price"]
        airline = flight["airlines"][0]
        departure = flight["route"][0]["local_departure"]
        msg = f"✈️ Cheap flight found!\n₹{price} | {airline}\nDeparts: {departure}"
        send_sms(msg)
        print("✅ SMS sent!")
    else:
        print("❌ No cheap flights found.")