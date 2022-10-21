from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://en.wikipedia.org/wiki/Main_Page"
sign_up_url = "http://secure-retreat-92358.herokuapp.com/"

chrome_driver_path = "D:\Development\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(sign_up_url)


# article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# article_count.click()

# site_news = driver.find_element(By.LINK_TEXT, "Site news")
# site_news.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

def auto_sign_up(f_name, l_name, email):
    first_name = driver.find_element(By.NAME, "fName")
    first_name.send_keys(f_name)
    last_name = driver.find_element(By.NAME, "lName")
    last_name.send_keys(l_name)
    email_addr = driver.find_element(By.NAME, "email")
    email_addr.send_keys(email)
    email_addr.submit()


auto_sign_up("Mike", "Spencer", "tnystrk@email.com")

# driver.quit()
