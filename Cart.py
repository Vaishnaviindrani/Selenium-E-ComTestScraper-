from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from Check_out import CheckOut_info_page

#First Page of adding to cart
class Cart_page:
    def __init__ (self,driver,Total_Items):
        self.driver = driver
        self.total_item = Total_Items #total items in entire website
        self.add = (By.CSS_SELECTOR, ".btn.btn_primary.btn_small.btn_inventory") # add button in homepage
        self.cart = (By.ID ,"shopping_cart_container")# button used to get into cart page
        self.cart_items = (By.CLASS_NAME,"cart_item_label") # get the total items in the cart page
        self.remove = (By.CSS_SELECTOR,".btn.btn_secondary.btn_small.cart_button")# remove button in cart page
        self.continue_button = (By.ID,"continue-shopping")# continue button in cart page
        self.check_out_button = (By.ID ,"checkout") #
        self.check_title = (By.CLASS_NAME, "title")

        
    #Adding Items to the cart
    def Add_to_cart(self):
        for i in range(min(2,self.total_item)):
            items=self.driver.find_elements(*self.add)
            items[i].click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((self.cart))
        )
        self.driver.find_element(*self.cart).click()
        time.sleep(2)

    #updating the cart to check the remove button functioning and the continue shopping button
    def At_cart(self):
        count = len(self.driver.find_elements(*self.cart_items))
        for i in range(count):
            if i%2 == 0:
                self.driver.find_element(*self.remove).click()
                self.driver.find_element(*self.continue_button).click()
                self.Add_to_cart()
            
            else:
                self.driver.find_element(*self.check_out_button).click()
                a = self.driver.find_element(*self.check_title).text
                time.sleep(1)
                CheckOut_info_page(self.driver,a).checkout()# redirecting to checkout page to add the address details
      