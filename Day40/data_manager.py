import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

PRICES_ENDPOINT = "https://api.sheety.co/694eca749af33d4ccab82f41656232e0/ianSpanglerCapstoneProject1/prices"
USERS_ENDPOINT = "https://api.sheety.co/694eca749af33d4ccab82f41656232e0/ianSpanglerCapstoneProject1/users"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.username = os.environ["SHEETY_USERNAME"]
        self.password = os.environ["SHEETY_PASSWORD"]
        self.authorization = HTTPBasicAuth(self.username, self.password)
        self.sheety_data = {}
        self.customer_data = {}

    def get_data(self):
        sheety_response = requests.get(url=PRICES_ENDPOINT, auth=self.authorization)
        print(sheety_response.json())
        self.sheety_data = sheety_response.json()["prices"]
        return self.sheety_data

    def update_destination_codes(self):
        for city in self.sheety_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            update_response = requests.put(
                url= f"{PRICES_ENDPOINT}/{city['id']}",
                json= new_data
            )
            # print(update_response.text)

    def update_price(self):
        for city in self.sheety_data:
            new_data = {
                "price": {
                    "lowestPrice": city["lowestPrice"]
                }
            }
            update_response = requests.put(
                url=f"{PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )

    def get_customer_emails(self):
        sheety_response = requests.get(url=USERS_ENDPOINT, auth=self.authorization)
        self.customer_data = sheety_response.json()["users"]
        return self.customer_data