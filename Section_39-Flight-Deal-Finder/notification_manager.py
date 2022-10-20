import smtplib
import os

my_email = "pythonemailtest106@gmail.com"
password = os.environ.get("PASSWORD")

class NotificationManager:

    def send_email(self, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="tonystark53150@gmail.com",
                msg=message
            )
