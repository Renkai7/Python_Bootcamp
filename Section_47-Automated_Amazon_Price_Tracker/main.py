import requests
from bs4 import BeautifulSoup
import os
import smtplib

url = "https://www.amazon.com/One-Piece-Odyssey-PlayStation-5/dp/B09WK2BX5M/?_encoding=UTF8&pd_rd_w=KmYoV&content-id" \
      "=amzn1.sym.e4bd6ac6-9035-4a04-92a6-fc4ad60e09ad&pf_rd_p=e4bd6ac6-9035-4a04-92a6-fc4ad60e09ad&pf_rd_r" \
      "=6P04XGAYQ2ETS81K1SWE&pd_rd_wg=RYmLS&pd_rd_r=faef68bf-f970-4cc1-9800-1fcf9c1ed7a9&ref_=pd_gw_ci_mcx_mr_hp_atf_m "

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 "
                  "Safari/537.36 Edg/106.0.1370.47",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

TARGET_PRICE = 55


def check_price():
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find(id="productTitle").get_text(strip=True)
    price = soup.find(id="priceblock_ourprice")

    # Check for changes in HTML code for prices (the classes change from product to product)
    if price is None:
        price = soup.select_one(selector="span.a-offscreen").get_text(strip=True)
    else:
        price = price.get_text(strip=True)
    convert_price = float(price.strip("$"))

    if convert_price < TARGET_PRICE:
        send_email(title, price)
    else:
        print("No price drops.")


def send_email(product, sale_price):
    my_email = "pythonemailtest106@gmail.com"
    password = os.environ.get("PASSWORD")
    message = f"Subject: Amazon Price drop! {product}\n\n" \
              f"{product} new price: {sale_price}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="tonystark53150@gmail.com",
            msg=message
        )


check_price()
