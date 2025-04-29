from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

# AMAZON_URL = "https://appbrewery.github.io/instant_pot/" # For test
AMAZON_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1" # Live website
SMTP_EMAIL = os.environ["SMTP_ADDRESS"]
MY_EMAIL = os.environ["EMAIL_ADDRESS"]
MY_PASSWORD = os.environ["EMAIL_PASSWORD"]


target_price = 100
# target_price = input("What is your target price?")

amazon_header={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.5",
    "Priority": "u=0, i",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0",
  }


response = requests.get(url=AMAZON_URL, headers=amazon_header)

amazon_webpage = response.text

soup = BeautifulSoup(amazon_webpage, "html.parser")

print(soup.prettify())

price_whole = str(soup.find(name="span", class_="a-price-whole")).split(">")[1].split("<")[0]
# print(price_whole)

price_fraction = soup.find(name="span", class_="a-price-fraction").getText()
# print(price_fraction)

price = float(f"{price_whole}.{price_fraction}")
print(price)

title = soup.find(id="productTitle").getText().strip().replace("\r\n", "").replace(" ", "")
print(title)

# This bit of code wouldn't work as I don't want an email to be sent
if price < target_price:
    with smtplib.SMTP(SMTP_EMAIL, port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg=f"Subject:Amazon Price Alert!\n\nYour product is now ${price}")