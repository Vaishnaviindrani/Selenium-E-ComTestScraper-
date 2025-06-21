from selenium.webdriver.common.by import By
import time
import os

class Collections():
    def __init__(self, driver, Total_Items):
        self.driver = driver
        self.total_item = Total_Items
        self.item = (By.CLASS_NAME,"inventory_item_name ")
        self.button = (By.ID, "back-to-products")

    def collection_html(self):
        os.makedirs("Data", exist_ok=True)  # Ensures folder exists
        for i in range(self.total_item):
            Items = self.driver.find_elements(*self.item)
            Items[i].click()
            time.sleep(1)
            with open(f"Data/item{i}.html", "w" ,encoding="utf-8") as f :
                f.write(self.driver.page_source)
            self.driver.find_element(*self.button).click()
            time.sleep(2)