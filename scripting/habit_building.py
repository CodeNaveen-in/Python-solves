import requests
from datetime import datetime

# ---------------------------- CONFIG ------------------------------- #
USERNAME = "naveengarg"
TOKEN = "your_secret_token"  # Choose a secure token
GRAPH_ID = "habitgraph"

# ---------------------------- CREATE USER ------------------------------- #
def create_user():
    endpoint = "https://pixe.la/v1/users"
    payload = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    response = requests.post(endpoint, json=payload)
    print("User creation:", response.text)

# ---------------------------- CREATE GRAPH ------------------------------- #
def create_graph():
    endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"
    headers = {"X-USER-TOKEN": TOKEN}
    payload = {
        "id": GRAPH_ID,
        "name": "Coding Minutes",
        "unit": "minutes",
        "type": "int",
        "color": "shibafu"  # green
    }
    response = requests.post(endpoint, json=payload, headers=headers)
    print("Graph creation:", response.text)

# ---------------------------- ADD HABIT ENTRY ------------------------------- #
def add_pixel(quantity):
    endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"
    headers = {"X-USER-TOKEN": TOKEN}
    today = datetime.now().strftime("%Y%m%d")
    payload = {
        "date": today,
        "quantity": str(quantity)
    }
    response = requests.post(endpoint, json=payload, headers=headers)
    print("Pixel added:", response.text)

# ---------------------------- RUN ------------------------------- #
if __name__ == "__main__":
    # Uncomment these once to initialize
    # create_user()
    # create_graph()

    # Log today's habit
    add_pixel(60)  # e.g., 60 minutes of coding