from lib import utils

import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

class RCMLogin:
    def __init__(self, driver=False):
        if(not driver):
            self.driver = utils.StartChromeDriver()
        elif(isinstance(driver, webdriver.Chrome)):
            self.driver = driver
        elif(driver):
            self.driver = utils.StartChromeDriver(start=True)

    def login(self):
        if(not self.checkIfRCM()):
            self.driver.get("https://bookings.rentalcarmanager.com/dashboard")
        if(self.checkIfLoginPage()):
            config = utils.Config()
            config.loadConfig()
            self.driver.find_element(By.ID, "Username").send_keys(config.RCM_username)
            self.driver.find_element(By.ID, "Password").send_keys(config.RCM_password)
            self.driver.find_element(By.ID, "MainContent_LoginButton").click()

    def checkIfLoginPage(self) -> bool:
        return self.driver.current_url == "https://bookings.rentalcarmanager.com/account/login.aspx"
    
    def checkIfRCM(self) -> bool:
        return self.driver.current_url.replace("//", "").split("/")[0] == "https:bookings.rentalcarmanager.com"


# December Early Birds. Pay Later should be freezed for some discounts with percentages
# Upgrade requester web page