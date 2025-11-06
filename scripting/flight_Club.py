import requests
import json
from datetime import datetime, timedelta
from twilio.rest import Client

# ---------------------------- CONFIG ------------------------------- #
TEQUILA_API_KEY = "your_tequila_api_key"
TWILIO_SID = "your_twilio_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE = "+1234567890"

USER_FILE = "users.json"
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
HEADERS = {"apikey": TEQUILA_API_KEY}

# ---------------------------- USER MANAGEMENT ------------------------------- #
def load_users():
    try:
        with open(USER_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=2)

def add_user(name, phone, origin, destination, max_price):
    users = load_users()
    users.append({
        "name": name,
        "phone": phone,
        "origin": origin,
        "destination": destination,
        "max_price": max_price
    })
    save_users(users)
    print(f"✅ Added user: {name}")

# ---------------------------- FLIGHT SEARCH ------------------------------- #
def search_flight(origin, destination, max_price):
    date_from = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
    date_to = (datetime.now() + timedelta(days=30)).strftime("%d/%m/%Y")
    params = {
        "fly_from": origin,
        "fly_to": destination,
        "date_from": date_from,
        "date_to": date_to,
        "curr": "INR",
        "price_to": max_price,
        "limit": 1,
        "sort": "price"
    }
    response = requests.get(f"{TEQUILA_ENDPOINT}/v2/search", headers=HEADERS, params=params)
    response.raise_for_status()
    data = response.json()["data"]
    return data[0] if data else None

# ---------------------------- NOTIFY USER ------------------------------- #
def send_sms(to, message):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(body=message, from_=TWILIO_PHONE, to=to)

# ---------------------------- CLUB RUNNER ------------------------------- #
def run_club():
    users = load_users()
    for user in users:
        flight = search_flight(user["origin"], user["destination"], user["max_price"])
        if flight:
            msg = (
                f"✈️ Hi {user['name']}, cheap flight found!\n"
                f"₹{flight['price']} | {flight['airlines'][0]}\n"
                f"Departs: {flight['route'][0]['local_departure']}"
            )
            send_sms(user["phone"], msg)
            print(f"✅ Alert sent to {user['name']}")
        else:
            print(f"❌ No deals for {user['name']}")

# ---------------------------- EXAMPLE USAGE ------------------------------- #
if __name__ == "__main__":
    # Uncomment to add users
    # add_user("Naveen", "+91xxxxxxxxxx", "DEL", "DXB", 15000)
    # add_user("Amit", "+91xxxxxxxxxx", "DEL", "BOM", 5000)

    run_club()