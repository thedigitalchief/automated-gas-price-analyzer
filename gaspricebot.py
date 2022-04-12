import logging
import time
import pandas as pd
from selenium import webdriver
from chromedriver_py import binary_path

logger = logging.getLogger(__file__)

PRICE_URL = 'https://calculator.aa.co.za/calculators-toolscol-1/fuel-pricing'

#so Chrome or gas webpage doesnt know this is a bot
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-extensions")


#function that loads, clicks, retrieves data
def get_prices(driver: webdriver):
    """
    Get Price Data from AA Website.

    :param driver: Chromedriver
    :return:
    """
    
    fuel_price_data = []
    driver.get(PRICE_URL)
    location_elements = driver.find_elements_by_xpath("//div[@id='edit-location']/div/input")
    locations = [location.get_attribute("value") for location in location_elements]
    fuel_elements = driver.find_elements_by_xpath("//select[@id='edit-fuel-type']/option")
    fuel_types = [fuel_.get_attribute("value") for fuel_ in fuel_elements]
    year_elements = driver.find_elements_by_xpath("//select[@id='edit-year']/option")
    years = [year.get_attribute("value") for year in year_elements]
    
    for location in locations:
        driver.find_element_by_xpath(f"//input[@value='{location}']/following-sibling::label").click()
        for fuel in fuel_types:
            driver.find_element_by_xpath(f"//select[@id='edit-fuel-type']/option[@value='{fuel}']").click()
            for year in years:
                driver.find_element_by_xpath(f"//select[@id='edit-year']/option[@value='{year}']").click()
                driver.find_element_by_xpath("//input[@value='Get Fuel Price']").click()
                print(f"Getting Data for {location}:{fuel}:{year}.")
                time.sleep(3)
                rows = driver.find_elements_by_xpath("//tbody/tr")
                for row in rows:
                    _row = row.get_attribute("innerText").split("\n")
                    fuel_price_data.append(_row + [location, fuel, year])
