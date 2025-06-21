from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# final overview page before placing order
class Overview:
    def __init__ (self,driver):
        self.driver = driver
        self.total = (By.XPATH, "//div[@class='summary_total_label']")
        self.cancel = (By.ID, "cancel")
        self.finish = (By.ID, "finish")

    def overview_page(self):
        # Ensure you are on the correct page and the element is loaded
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.total)
        )

        cancel_validation = self.driver.find_element(*self.cancel).text
        assert cancel_validation == "Cancel", "Did not find Cancel Button"
        time.sleep(2)
        self.driver.find_element(*self.finish).click()