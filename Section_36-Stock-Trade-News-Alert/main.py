import requests
import os
import datetime as dt
from email.message import EmailMessage
import smtplib

my_email = "pythonemailtest106@gmail.com"
password = os.environ.get("PASSWORD")

news_api_key = os.environ.get("NEWS_API_KEY")
news_endpoint = "https://newsapi.org/v2/everything"
stock_api_key = os.environ.get("STOCK_API_KEY")
stock_endpoint = "https://www.alphavantage.co/query"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

news_parameters = {
    "q": COMPANY_NAME,
    "pageSize": 3,
    "apiKey": news_api_key
}

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key
}

# Get Stock data
stock_response = requests.get(stock_endpoint, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()

# Get Yesterday date
yesterday = str(dt.date.today() - dt.timedelta(days=1))
day_before_yesterday = str(dt.date.today() - dt.timedelta(days=2))

# Get Yesterday and day before yesterday Stock
yesterday_stock = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
day_before_yesterday_stock = float(stock_data["Time Series (Daily)"][day_before_yesterday]["4. close"])

# Check if stock increased or decreased by 5%
stock_value_difference = abs(yesterday_stock - day_before_yesterday_stock)
percentage_difference = round((stock_value_difference / day_before_yesterday_stock) * 100, 2)

if percentage_difference > 5:
    # Get News data
    news_response = requests.get(news_endpoint, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()

    if yesterday_stock - day_before_yesterday_stock > 0:
        up_down = "🔺"
    else:
        up_down = "🔻"

    for news in news_data["articles"]:
        subject = f"Subject:{STOCK}: {up_down}{percentage_difference}%, {news['title']}"
        body = f"{news['description']}"
        message = EmailMessage()
        message.add_header("From", my_email)
        message.add_header("To", "tonystark53150@gmail.com")
        message.add_header("Subject", subject)
        message.set_payload(body, "utf-8")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.send_message(message, from_addr=my_email, to_addrs="tonystark53150@gmail.com")


