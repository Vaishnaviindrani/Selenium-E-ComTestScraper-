from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from login import Login_page
from homepage import Swag_Lab
from Cart import Cart_page
from Multiple_Items import Multiple_Items
from Scraping import Collections
from Check_out import CheckOut_info_page

options = Options()
options.add_argument("--incognito")

def main(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = Login_page(driver)
    login_page.Login("standard_user","secret_sauce")
    
    # homepage
    Total_Items = Swag_Lab(driver).Total_item()
    print(f"Total Items: {Total_Items}")

    #items adding into cart and updating
    Cart_page(driver,Total_Items).Add_to_cart()
    Cart_page(driver,Total_Items).At_cart()
    
    Multiple_Items(driver,Total_Items).Iterate_items()

    Collections(driver, Total_Items).collection_html()

    time.sleep(5)

if __name__ == "__main__":
    driver = webdriver.Chrome(options=options)
    main(driver)
    driver.quit()
