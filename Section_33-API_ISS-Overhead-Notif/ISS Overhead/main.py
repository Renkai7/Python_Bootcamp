import requests
from datetime import datetime
import smtplib
import time
import os

my_email = "pythonemailtest106@gmail.com"
password = os.environ.get("PASSWORD")

# Constants
MY_LAT = 51.507351
MY_LONG = -0.127758

# API for sunrise/sunset
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

# Datetime
time_now = datetime.now()
hour_now = time_now.hour


def is_iss_overhead():
    # API for ISS
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # Show error if error raises
    iss_response.raise_for_status()

    iss_data = iss_response.json()

    longitude = float(iss_data["iss_position"]["longitude"])
    latitude = float(iss_data["iss_position"]["latitude"])
    if -5 < abs(longitude - MY_LONG) < 5 and -5 < abs(latitude - MY_LAT) < 5:
        return True


def is_nighttime():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    if sunset <= hour_now or hour_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_nighttime():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            # Encrypts email being sent
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="tonystark53150@gmail.com",
                msg="Subject:ISS Overhead Alert\n\nThe ISS is above you in the sky."
            )
