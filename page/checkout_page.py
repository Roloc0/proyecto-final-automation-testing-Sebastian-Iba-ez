from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    _URL_CURRENT = "/checkout-step-one.html"
    _FIRST_NAME_INPUT = (By.ID, 'first-name')
    _LAST_NAME_INPUT = (By.ID, 'last-name')
    _POSTAL_CODE_INPUT = (By.ID, 'postal-code')
    _CONTINUE_BUTTON = (By.ID, 'continue')
    _CANCEL_BUTTON = (By.ID, 'cancel')
    _ERROR_MESSAGE = (By.CLASS_NAME, 'error-message-container')

    def __init__(self, driver):
        self.driver = driver

    def agregar_datos(self, first_name, last_name, postal_code):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self._FIRST_NAME_INPUT)
        ).send_keys(first_name)
        self.driver.find_element(*self._LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self._POSTAL_CODE_INPUT).send_keys(postal_code)

    def continuar(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self._CONTINUE_BUTTON)
        ).click()

    def cancelar(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self._CANCEL_BUTTON)
        ).click()