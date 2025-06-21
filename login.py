from selenium.webdriver.common.by import By

class Login_page:
    def __init__(self, driver):
        self.driver = driver
        self.user = (By.ID, 'user-name' )
        self.password = (By.ID, 'password' )
        self.login = (By.ID, 'login-button')

    def Login(self, username, password):
        self.driver.find_element(*self.user).send_keys(username) 
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login).click()
