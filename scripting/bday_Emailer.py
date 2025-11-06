import smtplib
import pandas as pd
import datetime as dt
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ---------------------------- CONFIG ------------------------------- #
EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"  # Use Gmail App Password if 2FA is enabled

# ---------------------------- SEND EMAIL ------------------------------- #
def send_birthday_email(to_email, name):
    subject = "🎉 Happy Birthday!"
    body = f"Hi {name},\n\nWishing you a fantastic birthday filled with joy and success!\n\n🎂🎈🎁"

    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)
        print(f"✅ Sent birthday email to {name}")
    except Exception as e:
        print(f"❌ Failed to send email to {name}: {e}")

# ---------------------------- CHECK BIRTHDAYS ------------------------------- #
def check_birthdays():
    today = dt.datetime.now().strftime("%m-%d")
    data = pd.read_csv("birthdays.csv")  # Columns: name,email,month,day

    for _, row in data.iterrows():
        bday = f"{row['month']:02d}-{row['day']:02d}"
        if bday == today:
            send_birthday_email(row['email'], row['name'])

# ---------------------------- RUN DAILY ------------------------------- #
if __name__ == "__main__":
    check_birthdays()