from bs4 import BeautifulSoup
import requests
import lxml
import os
from dotenv import load_dotenv
import smtplib

# Getting ENV variables
load_dotenv()
smtp_address = os.getenv("SMTP_ADDRESS")
email_address = os.getenv("EMAIL_ADDRESS")
email_password = os.getenv("EMAIL_PASSWORD")
url = "https://appbrewery.github.io/instant_pot/"

#Setting the soup and picking price
response = requests.get(url)
pot_page = response.text
soup = BeautifulSoup(pot_page, "html.parser")
price_bytes = soup.find(class_="a-offscreen").getText() #Set 0 so that only top value is chosen else whole list
price = float(price_bytes.replace("$", "").replace(",", ""))
title_bytes = soup.find( name= "span", id="productTitle")
title = title_bytes.getText()

shana = soup.select(".a-offscreen")
for s in shana:
    print(s.getText())

print(smtp_address, email_address, email_password)

# function for sending mail
def send_mail(subject, body, recipient):
    with smtplib.SMTP(smtp_address, port=25) as server: #has set port of free server because could not open google one
        server.starttls()
        server.login(email_address, email_password)
        message = f"Subject: {subject} \n\n {body}"
        server.sendmail(email_address, recipient, message)

# Price Check and decision
if (price < 170):
    print("Smaller finally")
    subject = f"Price Lowered of {title [:10]}"
    body = f"Price has been lowered and is finally {price}. \nHurry up and but {title} \n\n Warm Regards \nNaveen"
    send_mail(subject, body, email_address)
else:
    print(price, " Large and we have ", title)
