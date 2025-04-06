# ISS Overhead Notifier
import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 37.566536 # Your latitude
MY_LONG = 126.977966 # Your longitude

my_email = "100daysofcodetestIan@gmail.com"
my_password = "AppPassword" # 9s6sA,$RK&+ykJG

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
def is_overhead():
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    if sunset <= time_now.hour or time_now.hour <= sunrise:
        return True
while True:
    time.sleep(60)
    if is_night() and is_overhead():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email,
                                msg="Subject:Look Up!\n\nISS is right above your head. Look up!")

