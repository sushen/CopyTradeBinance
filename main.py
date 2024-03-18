import time
import re

from selenium.webdriver.common.by import By
from driver.driver import Driver

driver = Driver().driver

driver.get("https://www.binance.com/en/trading-bots")

driver.implicitly_wait(10)
time.sleep(4)
driver.find_element(By.XPATH, ("//div[contains(.,'SOLUSDT Perpetual')]/ancestor::div[contains(@class,'css-1fymml5')]")).click()

input("End:")