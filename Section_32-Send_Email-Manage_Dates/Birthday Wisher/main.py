import pandas
import datetime as dt
import random
import smtplib
import os

my_email = "pythonemailtest106@gmail.com"
password = os.environ.get("PASSWORD")

letter_list = ["letter_1", "letter_2", "letter_3"]
birthday_data = pandas.read_csv("birthdays.csv")
birthday_dict = birthday_data.to_dict(orient="records")

now = dt.datetime.now()
day = now.day
month = now.month


def write_letter(birth_day_name):
    letter = random.choice(letter_list)
    with open(f"letter_templates/{letter}.txt") as starter_letter:
        letter_template = starter_letter.read()
        print(letter_template)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="tonystark53150@gmail.com",
            msg=f"Subject:Happy Birthday\n\n{letter_template.replace('[NAME]', birth_day_name)}"
        )


for name in birthday_dict:
    if name["day"] == day and name["month"] == month:
        write_letter(name['name'])
