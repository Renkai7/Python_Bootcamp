import requests
import os
from twilio.rest import Client

open_weather_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")
account_sid = "AC421831cbeabdfc42de3f2e61896d91ba"
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": 39.535671,
    "lon": -76.348473,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
# API for OpenWeatherMap
open_weather_response = requests.get(open_weather_endpoint, params=parameters)
open_weather_response.raise_for_status()
weather_data = open_weather_response.json()
twelve_hour_weather = weather_data["hourly"][:11]


def will_need_umbrella():
    for hourly_weather in twelve_hour_weather:
        condition_code = hourly_weather["weather"][0]["id"]
        if condition_code < 700:
            return True
        else:
            return False


if will_need_umbrella():
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔",
        from_='+12136452581',
        to=os.environ.get("MY_NUMBER")
    )
    print(message.status)
