##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import pandas
import random

my_email = "100daysofcodetestIan@gmail.com"
my_password = "AppPassword" # 9s6sA,$RK&+ykJG

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
birthdays = data.to_dict("records")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day
for birthday in birthdays:
    if month == birthday["month"] and day == birthday["day"]:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        random_template = random.randint(1,3)
        with open(f"letter_templates/letter_{random_template}.txt", "r") as file:
            letter = file.read()
            new_letter = letter.replace("[NAME]", birthday["name"])
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=birthday["email"],
                                        msg=f"Subject:Happy Birthday {birthday["name"]}!\n\n{new_letter}")



