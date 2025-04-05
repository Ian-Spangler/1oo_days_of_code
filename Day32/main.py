# import smtplib
#
# my_email = "100daysofcodetestIan@gmail.com"
# my_password = "AppPassword" # 9s6sA,$RK&+ykJG
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="naItsetedocfosyad100@yahoo.com",
#                         msg="Subject:Hello\n\nThis is the body of my email.")

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# if year > 2025:
#     print("What are you doing, nostalgia?")
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=2004, month=1, day=1)
# print(date_of_birth)

import datetime as dt
import smtplib
import random

my_email = "100daysofcodetestIan@gmail.com"
my_password = "AppPassword" # 9s6sA,$RK&+ykJG

now = dt.datetime.now()

with open("quotes.txt", "r") as file:
    quotes = file.readlines()
    quotes_stripped = [quote.strip("\n") for quote in quotes]

if now.weekday() == 1:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:Monday Motivation\n\n{random.choice(quotes_stripped)}")