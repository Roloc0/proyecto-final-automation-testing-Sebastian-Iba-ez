from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

_URL = "https://www.saucedemo.com/"

class LoginPage:
    
    _INPUT_NAME = (By.NAME, "user-name") 
    _INPUT_PASSWORD = (By.NAME, "password") 
    _LOGIN_BUTTON = (By.NAME, "login-button")
    _ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")

    def __init__(self, driver): 
       self.driver = driver

    def open(self):
        self.driver.get(_URL)

    def login(self, username, password):

        WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable(self._INPUT_NAME)
        ).send_keys(username)

        WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable(self._INPUT_PASSWORD)
        ).send_keys(password)

        WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable(self._LOGIN_BUTTON)
        ).click()
    
    def mensaje_error(self):
        try:
            error_element = self.driver.find_element(*self._ERROR_MESSAGE)
            return error_element.text
        except:
            return ""