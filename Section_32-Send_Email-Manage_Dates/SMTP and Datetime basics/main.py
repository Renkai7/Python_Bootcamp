import random
import smtplib
import datetime as dt
import os

my_email = "pythonemailtest106@gmail.com"
# birthday_wisher app passcode
password = os.environ.get("PASSWORD")

# Setting up connection for sending an Email
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # Encrypts email being sent
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="tonystark53150@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )
# connection.close()

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
date_of_birth = dt.datetime(year=1992, month=4, day=6)

# print(day_of_week)
# print(date_of_birth)

# Send motivational quote on Monday
if day_of_week == 0:
    with open("quotes.txt") as quote_file:
        data = quote_file.readlines()
        quote_of_day = random.choice(data)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Encrypts email being sent
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="tonystark53150@gmail.com",
            msg=f"Subject:Motivational Monday\n\n{quote_of_day}"
        )
