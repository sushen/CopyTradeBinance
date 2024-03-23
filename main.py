import time
import re
import xml.etree.ElementTree as ET

from selenium.webdriver.common.by import By
from driver.driver import Driver  # Assuming you have your custom driver module

# Initialize the driver
driver = Driver().driver

# Navigate to the desired URL
driver.get("https://www.binance.com/en/trading-bots")

# Wait for the page to load
driver.implicitly_wait(10)
time.sleep(1)

# Click on the desired element to reveal the "Create Futures Grid" option
driver.find_element(By.XPATH, "(//div[@class='css-1fymml5'])[2]").click()

# Wait for the element to become visible
driver.implicitly_wait(10)
time.sleep(1)

# Click on the "Create Futures Grid" option
header_element = driver.find_element(By.XPATH, "//div[contains(text(),'Create Futures Grid')]")
header_element.click()

# Wait for the chart elements to load
driver.implicitly_wait(10)
time.sleep(1)

# Find all chart elements
chart_elements = driver.find_elements(By.XPATH, "//div[@data-highcharts-chart]")


def extract_numbers_from_svg(svg_html):
    numbers = []
    try:
        root = ET.fromstring(svg_html)
        for path_element in root.iter('{http://www.w3.org/2000/svg}path'):
            d_attribute = path_element.get('d')
            if d_attribute:
                # Extract data points from the d attribute (you may need a more sophisticated approach here)
                # For simplicity, let's just extract numbers separated by spaces
                data_points = [float(x) for x in d_attribute.split() if x.replace('.', '').replace('-', '').isdigit()]
                numbers.extend(data_points)
    except ET.ParseError as e:
        print("Error parsing SVG:", e)
    return numbers


# Iterate over chart elements
for element in chart_elements:
    if len(element.text) > 1:
        svg_html = element.get_attribute("outerHTML")
        match = re.search(r'<svg[^>]*>(.*?)</svg>', svg_html, re.DOTALL)
        if match:
            svg = match.group(0)
            # Extract numbers from SVG paths
            numbers = extract_numbers_from_svg(svg)
            print("Extracted numbers:", numbers)
        else:
            print("SVG not found in HTML")
        input("Find Something:")
