from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


url = "https://www.python.org/events/python-events/"

chrome_driver_path = "D:\Development\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(url)
# driver.implicitly_wait(10)
titles = driver.find_elements(By.CSS_SELECTOR, "div.shrubbery h3.event-title")
times = driver.find_elements(By.CSS_SELECTOR, "div.shrubbery time")
events = {}

for num in range(len(titles)):
    events[num] = {
        "time": times[num].text,
        "name": titles[num].text
    }

print(events)

driver.quit()
