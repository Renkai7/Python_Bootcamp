import requests
from flight_data import FlightData
import os

API_KEY = os.environ.get("TEQUILA_API_KEY")
flight_endpoint = "https://api.tequila.kiwi.com"
flight_headers = {
    "apikey": API_KEY,
    # "accept": "application/json"
}


class FlightSearch:
    def check_flights(self, origin_city_code, dest_city_code, from_time, to_time):
        search_endpoint = f"{flight_endpoint}/v2/search"
        search_headers = {
            "apikey": API_KEY,
        }
        search_params = {
            "fly_from": origin_city_code,
            "fly_to": dest_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "curr": "GBP",
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "max_stopovers": 0,
            "one_for_city": 1
        }

        search_response = requests.get(url=search_endpoint, params=search_params, headers=search_headers)
        try:
            data = search_response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {dest_city_code}")
            return None

        flight_data = FlightData(
            origin_city=data["route"][0]["cityFrom"],
            price=data["price"],
            depart_airport_code=data["route"][0]["flyFrom"],
            desitination_city=data["route"][0]["cityTo"],
            desitination_airport=data["route"][0]["flyTo"],
            date_from=data["route"][0]["local_departure"].split("T")[0],
            date_to=data["route"][1]["local_departure"].split("T")[0]
        )

        print(f"{flight_data.desitination_city}: £{flight_data.price}")
        return flight_data

    def get_iata_code(self, city_name):
        location_endpoint = f"{flight_endpoint}/locations/query"
        flight_params = {
            "term": city_name,
            "location_types": "city"
        }

        flight_response = requests.get(url=location_endpoint, params=flight_params, headers=flight_headers)
        data = flight_response.json()["locations"]
        code = data[0]["code"]

        return code
