#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import time
import datetime as dt
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

start = dt.datetime.now() + dt.timedelta(days=1)
end = dt.datetime.now() + dt.timedelta(days=180)

data_manager = DataManager()
sheet_data = data_manager.get_data()
flight_search = FlightSearch()
flight_data = FlightData(start, end)

print(sheet_data)

for city in sheet_data:
    if city["iataCode"] == "" or city["iataCode"] != flight_search.city_search(city["city"]):
        city["iataCode"] = flight_search.city_search(city["city"])
        data_manager.update_destination_codes()
        data_manager.sheety_data = sheet_data
    print(f"Getting flights for {city["city"]}...")
    cheapest_flight = flight_data.find_cheapest_flight(city["iataCode"])
    city["lowestPrice"] = cheapest_flight
    print(f"{city["city"]}: {cheapest_flight}KRW")
    if flight_data.update:
        data_manager.update_price()
        notification_manager = NotificationManager(city["lowestPrice"], flight_data.departure_code, ["iataCode"], start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d"))
    flight_data.reset()


