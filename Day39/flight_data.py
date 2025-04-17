import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import datetime as dt

load_dotenv()

DATA_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_API_SECRET"]
        self._token = self.get_token()
        self.cheapest_price = 0

    def get_token(self):
        token_paramas = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }

        token_headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        token_response = requests.post(url=TOKEN_ENDPOINT, data=token_paramas, headers=token_headers)
        # print(f"Your token is {token_response.json()['access_token']}")
        # print(f"Your token expires in {token_response.json()['expires_in']} seconds")
        return token_response.json()["access_token"]

    def find_cheapest_flight(self, code):
        start = dt.datetime.now() + dt.timedelta(days=1)
        end = dt.datetime.now() + dt.timedelta(days=180)

        data_paramas = {
            "originLocationCode": "ICN",
            "destinationLocationCode": code,
            "departureDate": start.strftime("%Y-%m-%d"),
            "returnDate": end.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "KRW",
            "max": "10"
        }

        data_headers = {
            "Authorization": f"Bearer {self._token}"
        }

        data_response = requests.get(url=DATA_ENDPOINT, params=data_paramas, headers=data_headers)

        if data_response.status_code != 200:
            print(f"check_flights() response code: {data_response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", data_response.text)
            return None
        # self.cheapest_price = data_response.json()
        for data in data_response.json()["data"]:
            data["price"]
        return data_response.json()