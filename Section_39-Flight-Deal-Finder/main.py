from notification_manager import NotificationManager
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta



data_manager = DataManager()
sheet_data = data_manager.get_sheet()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# CONSTANT
ORIGIN_CITY_CODE = "LON"


tomorrow = datetime.now() + timedelta(days=1)
six_months = datetime.now() + timedelta(days=(6 * 30))

# Get prices for each destination
for airport in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_CODE,
        airport["IATA Code"],
        tomorrow,
        six_months
    )
    # Check for lowered prices for flights
    if flight is not None and flight.price < int(airport["Lowest Price"]):
        notification_manager.send_email(
            message=f"Subject: Low price alert! £{flight.price} {flight.desitination_city}\n\n"
                    f"Fly from {flight.flyfrom}-{flight.depart_airport_code},"
                    f"to {flight.desitination_city}-{flight.desitination_airport},"
                    f"from {flight.date_from} to {flight.date_to}.".encode('utf-8')
        )

