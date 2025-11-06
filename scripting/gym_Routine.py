import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# ---------------------------- AUTHENTICATION ------------------------------- #
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# ---------------------------- SHEET SETUP ------------------------------- #
sheet = client.open("Workout Tracker").sheet1  # Sheet name must match
headers = sheet.row_values(1)
if not headers or headers != ["Date", "Exercise", "Reps", "Duration (min)"]:
    sheet.update("A1:D1", [["Date", "Exercise", "Reps", "Duration (min)"]])

# ---------------------------- LOG WORKOUT ------------------------------- #
def log_workout(exercise, reps, duration):
    today = datetime.now().strftime("%Y-%m-%d")
    sheet.append_row([today, exercise, reps, duration])
    print(f"✅ Logged: {exercise} | {reps} reps | {duration} min")

# ---------------------------- EXAMPLE ------------------------------- #
if __name__ == "__main__":
    log_workout("Push-ups", 30, 10)
    log_workout("Running", 0, 20)