from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


url = "https://www.amazon.com/One-Piece-Odyssey-PlayStation-5/dp/B09WK2BX5M/?_encoding=UTF8&pd_rd_w=KmYoV&content-id" \
      "=amzn1.sym.e4bd6ac6-9035-4a04-92a6-fc4ad60e09ad&pf_rd_p=e4bd6ac6-9035-4a04-92a6-fc4ad60e09ad&pf_rd_r" \
      "=6P04XGAYQ2ETS81K1SWE&pd_rd_wg=RYmLS&pd_rd_r=faef68bf-f970-4cc1-9800-1fcf9c1ed7a9&ref_=pd_gw_ci_mcx_mr_hp_atf_m "

chrome_driver_path = "D:\Development\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(url)
driver.implicitly_wait(10)

# Find Elements in webpage
# price = driver.find_element(By.ID, "priceblock_ourprice")
# Search more accurately by using XPATH
price = driver.find_element(By.XPATH, '//*[@id="priceblock_ourprice"]')
print(price.text)

driver.quit()
