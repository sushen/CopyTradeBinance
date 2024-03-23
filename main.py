import time
import re
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
from driver.driver import Driver

driver = Driver().driver

driver.get("https://www.binance.com/en/trading-bots")

driver.implicitly_wait(10)
time.sleep(1)
driver.find_element(By.XPATH,
                    "(//div[@class='css-1fymml5'])[2]").click()

# input("Find Create Futures Grid Window :")

driver.implicitly_wait(10)
time.sleep(1)
header_element = driver.find_element(By.XPATH, "//div[contains(text(),'Create Futures Grid')]")
header_element.click()
print(header_element.text)

# input("Find Chart Elements:")

driver.implicitly_wait(10)
time.sleep(1)
chart_elements = driver.find_elements(By.XPATH, "//div[@data-highcharts-chart]")
for element in chart_elements:
    if len(element.text) > 1:
        # print(element.text)
        svg_html = element.get_attribute("outerHTML")
        match = re.search(r'<svg[^>]*>(.*?)</svg>', svg_html, re.DOTALL)
        svg = match.group(0)
        print(svg)
        # soup = BeautifulSoup(svg, 'html.parser')
        #
        # text_elements = soup.find_all('text')
        # # Extract text content from <text> elements
        # text_values = [text.get_text() for text in text_elements]
        # print(text_values)
        input("Find Something:")
