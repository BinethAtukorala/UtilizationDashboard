from lib.login import RCMLogin
from lib import utils

import sys
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class UtilizationEntry:
    def __init__(self, category:str, avg_rate:float, util:float):
        self.category: str = ""
        self.avg_rate: float = 0.0
        self.util: float = 0
    
    def __str__(self):
        return f"{self.category} ${self.avg_rate} {self.util}%"

class Utilization:
    def __init__(self, driver=False):
        if(driver == False):
            self.driver = utils.StartChromeDriver()
        elif(isinstance(driver, webdriver.Chrome)):
            self.driver = driver
        elif(driver==True):
            self.driver = utils.StartChromeDriver(start=True)

        self.report_path = "https://bookings.rentalcarmanager.com/report/untilizationreport"

    def main(self):

        self.gotoUtilizationReport()

        self.setRegion("N")
        start_date = datetime.datetime.strptime("2025-08-01", "%Y-%M-%d")
        end_date = datetime.datetime.strptime("2025-08-31", "%Y-%M-%d")

        self.setDates(start_date, end_date)
        self.runReport()

        

    def scrapeReport(self, source):
        soup = BeautifulSoup(source, "html.parser")

        utils = []

        for row in soup.find_all("tr"):
            columns = row.find_all("td")
            if(columns[0].isnumeric()):
                utils.append(UtilizationEntry(columns[1], float(columns[6].replace("$", "")), float(columns[9].replace("%"))))



    def gotoUtilizationReport(self):
        # Log in to RCM
        login = RCMLogin()
        login.login()
        while(self.driver.current_url != self.report_path):
            self.driver.get(self.report_path)
            sleep(0.2)

    def runReport(self):
        self.driver.find_element(By.ID, "butRunReport").click()

    def setRegion(self, keys:str):
        region_in = self.driver.find_element(By.ID, "txtRegionID")
        region_in.send_keys(keys)

    def setDates(self, start_date: datetime.datetime, end_date: datetime.datetime):
        start_day_input = self.driver.find_element(By.ID, "lbltxtStartingday").find_element(By.CLASS_NAME, "day ")
        start_month_input = self.driver.find_element(By.ID, "lbltxtStartingday").find_element(By.CLASS_NAME, "month ")
        start_year_input = self.driver.find_element(By.ID, "lbltxtStartingday").find_element(By.CLASS_NAME, "year ")
        
        end_day_input = self.driver.find_element(By.ID, "lbltxtEndingDay").find_element(By.CLASS_NAME, "day ")
        end_month_input = self.driver.find_element(By.ID, "lbltxtEndingDay").find_element(By.CLASS_NAME, "month ")
        end_year_input = self.driver.find_element(By.ID, "lbltxtEndingDay").find_element(By.CLASS_NAME, "year ")

        # Year
        start_year = start_date.strftime("%Y")
        start_year_input.send_keys(str(start_year))

        end_year = end_date.strftime("%Y")
        end_year_input.send_keys(str(end_year))

        # Month
        start_month = start_date.strftime("%b")
        start_month_input.send_keys(start_month)
        
        end_month = end_date.strftime("%b")
        end_month_input.send_keys(end_month)

        # Day

        # ----- Start
        start_day = start_date.day
        if(start_day == 1):
            start_day_input.send_keys("19")
            start_year_input.send_keys(str(start_year))
            start_day_input.send_keys("1")
        elif(start_day == 2):
            start_day_input.send_keys("29")
            start_year_input.send_keys(str(start_year))
            start_day_input.send_keys("2")
        elif(start_day == 3):
            start_day_input.send_keys("20")
            start_year_input.send_keys(str(start_year))
            start_day_input.send_keys("1")
            start_year_input.send_keys(str(start_year))
            start_day_input.send_keys("3")
        elif(start_day == 11):
            start_day_input.send_keys("30")
            start_year_input.send_keys(str(start_year))
            start_day_input.send_keys("111")
        elif(start_day == 22):
            start_day_input.send_keys("30")
            start_year_input.send_keys(str(start_year))
            start_day_input.send_keys("2222")
        else:
            start_day_input.send_keys(str(start_day))

        # ----- End
        end_day = end_date.day
        if(end_day == 1):
            end_day_input.send_keys("19")
            end_year_input.send_keys(str(end_year))
            end_day_input.send_keys("1")
        elif(end_day == 2):
            end_day_input.send_keys("29")
            end_year_input.send_keys(str(end_year))
            end_day_input.send_keys("2")
        elif(end_day == 3):
            end_day_input.send_keys("20")
            end_year_input.send_keys(str(end_year))
            end_day_input.send_keys("1")
            end_year_input.send_keys(str(end_year))
            end_day_input.send_keys("3")
        elif(end_day == 11):
            end_day_input.send_keys("30")
            end_year_input.send_keys(str(end_year))
            end_day_input.send_keys("111")
        elif(end_day == 22):
            end_day_input.send_keys("30")
            end_year_input.send_keys(str(end_year))
            end_day_input.send_keys("2222")
        else:
            end_day_input.send_keys(str(end_day))







