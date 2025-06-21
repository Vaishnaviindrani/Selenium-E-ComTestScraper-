from selenium.webdriver.common.by import By
import time


class Multiple_Items():
    def __init__(self, driver, Total_Items):
        self.driver = driver
        self.total_item = Total_Items
        self.item = (By.CLASS_NAME,"inventory_item_name ")
        self.button = (By.ID, "back-to-products")

    def Iterate_items(self):
    
        for i in range(self.total_item):
            Items = self.driver.find_elements(*self.item)
            Items[i].click()
            time.sleep(1)
            self.driver.find_element(*self.button).click()
            time.sleep(2)