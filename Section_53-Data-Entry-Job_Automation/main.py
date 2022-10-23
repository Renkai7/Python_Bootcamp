import time
from bs4 import BeautifulSoup
import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

form_url = "https://forms.gle/8jQGSryV586V5UAA6"
zillow_url = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22" \
             "%3A%7B%22west%22%3A-122.63844160954663%2C%22east%22%3A-122.23400740544507%2C%22south%22%3A37" \
             ".70025587595928%2C%22north%22%3A37.84110504809168%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue" \
             "%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C" \
             "%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22" \
             "%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22" \
             "%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22" \
             "%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 "
                  "Safari/537.36 Edg/106.0.1370.47",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# Setup Selenium
chrome_driver_path = "D:\Development\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

response = requests.get(zillow_url, headers=header)

# Get Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

data = json.loads(
    soup.select_one("script[data-zrr-shared-data-key]")
    .contents[0]
    .strip("!<>-")
)

results_list = data["cat1"]["searchResults"]["listResults"]

# Get URL Links
house_links = [result["detailUrl"] for result in results_list]
reformatted_house_links = [
    link.replace(link, "https://www.zillow.com" + link)
    if not link.startswith("http")
    else link
    for link in house_links
]
# Get address
home_addresses = [result["address"] for result in results_list]

# Get Prices
rent_prices = [
    (result["units"][0]["price"]).strip("+")
    if "units" in result
    else result["price"].strip("/mo")
    for result in results_list
]

# Fill out form
for i in range(len(results_list)):
    # Reload form each pass
    driver.get(form_url)
    # Pause for form to load
    time.sleep(2)
    address = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

    address.send_keys(home_addresses[i])
    price.send_keys(rent_prices[i])
    link.send_keys(reformatted_house_links[i])
    submit_button.click()

