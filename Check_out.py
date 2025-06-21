from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

from Overview import Overview

#Adding details of delivery 
class CheckOut_info_page:
    def __init__ (self,driver,a):
        self.driver = driver
        self.excepted = a
        self.actual = (By.CLASS_NAME, "title")
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID,"last-name")
        self.zip_code = (By.ID,"postal-code")
        self.continue_button = (By.ID, "continue")
        self.cancel_button = (By.ID,"cancel")

    def checkout(self):#function used to fill the address details
        actual= self.driver.find_element(*self.actual).text
        assert actual == self.excepted ,"error"
        print(f"the {actual} page")

        first = self.driver.find_element(*self.first_name)
        first.send_keys("ABC")

        last =  self.driver.find_element(*self.last_name)
        last.send_keys("XYZ")

        pin = self.driver.find_element(*self.zip_code)
        pin.send_keys("56")

        Cancel_Validation = self.driver.find_element(*self.cancel_button).text
        assert Cancel_Validation == "Cancel" ,"Cancel Button is Not Working"

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((self.continue_button))
        )

        continue_Validation = self.driver.find_element(*self.continue_button).get_attribute("value") 
        assert continue_Validation == "Continue" ,"Continue Button is Not Working"
        self.driver.find_element(*self.continue_button).click()

        Overview(self.driver).overview_page()




        
