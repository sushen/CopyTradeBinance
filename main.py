import time
import re

from selenium.webdriver.common.by import By
from driver.driver import Driver

driver = Driver().driver

driver.get("https://www.binance.com/en/trading-bots")

driver.implicitly_wait(10)
time.sleep(1)
driver.find_element(By.XPATH, ("//div[contains(.,'SOLUSDT Perpetual')]/ancestor::div[contains(@class,'css-1fymml5')]")).click()

# input("Find Create Futures Grid Window :")

driver.implicitly_wait(10)
time.sleep(1)
header_element = driver.find_element(By.XPATH, ("//div[contains(text(),'Create Futures Grid')]"))
header_element.click()
print(header_element.text)

# input("Find Chart Elements:")

driver.implicitly_wait(10)
time.sleep(1)
chart_elements = driver.find_elements(By.XPATH, ("//div[@data-highcharts-chart]"))
for element in chart_elements:
    if len(element.text)> 1:
        print(element.text)
        print(element.get_attribute("outerHTML"))
        input("Find Something:")

