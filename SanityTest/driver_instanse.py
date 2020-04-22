from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import os

class Driver():
    _instance = None

    def __new__(self, url="",  is_headless='True', reset=False):
        if not self._instance or reset:
            self._instance = super(Driver, self).__new__(self)
            driver_location = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chromedriver')
            os.environ["webdriver.chrome.driver"] = driver_location
            if is_headless is 'True':
                chrome_options = Options()
              #  chrome_options.add_argument("--headless")
                chrome_options.add_argument("--no-sandbox")
                chrome_options.add_argument("disable-gpu")
                chrome_options.add_argument("--window-size=1920,1080")
                options.add_argument('headless')
                self.driver = webdriver.Chrome(driver_location, options=chrome_options)
            else:
                self.driver = webdriver.Chrome(driver_location)
                self.driver.maximize_window()

            self.driver.get(url)
        return self._instance

    def close_driver(self):
        self.driver.close()
        self._instance = None

    def get_driver(self):
        return self.driver
