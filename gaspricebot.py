import logging
import time
import pandas as pd
from selenium import webdriver
from chromedriver_py import binary_path

logger = logging.getLogger(__file__)

PRICE_URL = 'https://calculator.aa.co.za/calculators-toolscol-1/fuel-pricing'

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-extensions")
