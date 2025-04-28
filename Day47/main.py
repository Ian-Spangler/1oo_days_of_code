from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

AMAZON_URL = "https://appbrewery.github.io/instant_pot/"
SMTP_EMAIL = os.environ["SMTP_ADDRESS"]
MY_EMAIL = os.environ["EMAIL_ADDRESS"]
MY_PASSWORD = os.environ["EMAIL_PASSWORD"]


target_price = 100
# target_price = input("What is your target price?")

response = requests.get(AMAZON_URL)

amazon_webpage = response.text

soup = BeautifulSoup(amazon_webpage, "html.parser")

price_whole = str(soup.find(name="span", class_="a-price-whole")).split(">")[1].split("<")[0]
# print(price_whole)

price_fraction = soup.find(name="span", class_="a-price-fraction").getText()
# print(price_fraction)

price = float(f"{price_whole}.{price_fraction}")
# print(price)

title = soup.find(id="productTitle").getText().strip()
# print(title)

if price < target_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg=f"Subject:Amazon Price Alert!\n\nYour product is now ${price}")