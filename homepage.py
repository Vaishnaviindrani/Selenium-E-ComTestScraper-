from selenium.webdriver.common.by import By
import time

class Swag_Lab():
    def __init__(self, driver):
        self.driver = driver
        self.item = (By.CLASS_NAME,"inventory_item_description")
        self.menu = (By.ID, "react-burger-menu-btn")
        self.cross = (By.ID, "react-burger-cross-btn")
        
    def Total_item(self):
        self.driver.find_element(*self.menu).click()
        time.sleep(1)
        self.driver.find_element(*self.cross).click()
        total = len(self.driver.find_elements(*self.item))
        time.sleep(1)
        return total
        