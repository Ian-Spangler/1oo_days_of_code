import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, price, departure_code, arrival_code, outbound_date, inbound_date):
        self.price = price
        self.departure_code = departure_code
        self.arrival_code = arrival_code
        self.outbound_date = outbound_date
        self.inbound_date =  inbound_date
        self.twilio_id = os.environ["TWILIO_SID"]
        self.twilio_auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        self.twilio_virtual_number = os.environ["TWILIO_VIRTUAL_NUMBER"]
        self.twilio_verified_number = os.environ["TWILIO_VERIFIED_NUMBER"]

    def send_emails(self, email_list, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(self.email, self.email_password)
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                )
