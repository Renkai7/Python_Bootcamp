import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://orteil.dashnet.org/cookieclicker/"

chrome_driver_path = "D:\Development\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(url)

lang = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "langSelect-EN")))
lang.click()


def cookie_click():
    while True:
        try:
            driver.find_element(By.XPATH, '//*[@id="bigCookie"]').click()
        except:
            pass
        try:
            list_upgrades = driver.find_elements(By.CSS_SELECTOR, "div.upgrades")
            list_upgrades[-1].click()
        except:
            pass
        try:
            list_upd = driver.find_elements(By.CSS_SELECTOR, "div.enabled")
            list_upd[-1].click()
        except:
            pass


cookie_click()
