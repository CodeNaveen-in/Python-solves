import smtplib
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ---------------------------- CONFIG ------------------------------- #
EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"  # Use App Password if 2FA is enabled
TO_EMAIL = "recipient@example.com"

# ---------------------------- MESSAGE ------------------------------- #
def send_motivation():
    subject = "🌟 Monday Motivation"
    quote = "Believe you can and you're halfway there. – Theodore Roosevelt"

    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = TO_EMAIL
    msg['Subject'] = subject

    body = f"Hi there,\n\nHere's your Monday motivation:\n\n{quote}\n\nHave a great week ahead! 💪"
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)
        print("✅ Motivational email sent!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

# ---------------------------- SCHEDULER ------------------------------- #
schedule.every().monday.at("09:00").do(send_motivation)

print("📅 Scheduler started. Waiting for Monday 9AM...")
while True:
    schedule.run_pending()
    time.sleep(60)