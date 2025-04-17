#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import time
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

data_manager = DataManager()
sheet_data = data_manager.get_data()
flight_search = FlightSearch()
flight_data = FlightData()

for city in sheet_data:
    if city["iataCode"] == "":
        city["iataCode"] = flight_search.city_search(city["city"])
    cheapest_flight = flight_data.find_cheapest_flight(city["iataCode"])
    # print(f"{city["city"]}: {cheapest_flight.price}KRW")
    time.sleep(2)

data_manager.sheety_data = sheet_data
data_manager.update_destination_codes()