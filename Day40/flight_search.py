import os
import requests
from dotenv import load_dotenv

load_dotenv()

SEARCH_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_API_SECRET"]
        self._token = self.get_token()

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

    def city_search(self, city):
        search_paramas = {
            "keyword": city,
            "max": "2",
            "include": "AIRPORTS"
        }

        search_headers = {
            "Authorization": f"Bearer {self._token}"
        }
        search_response = requests.get(url=SEARCH_ENDPOINT, params=search_paramas, headers=search_headers)
        # print(f"Status code {search_response.status_code}. Airport IATA: {search_response.text}")
        try:
            code = search_response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city}.")
            return "Not Found"

        return code