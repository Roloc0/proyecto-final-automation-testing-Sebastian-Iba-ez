from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    _URL_CURRENT = "/cart.html"
    _CART_ITEMS = (By.CLASS_NAME, "cart_item")
    _ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    _CHECKOUT_BUTTON = (By.ID, "checkout")
    _REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def lista_productos(self): 
        elementos_nombre = self.driver.find_elements(*self._ITEM_NAMES) 
        return [elemento.text for elemento in elementos_nombre] 

    def click_checkout(self): 
        self.driver.find_element(*self._CHECKOUT_BUTTON).click() 
        return self
    
    def remove_item(self, item_index=0):
        remove_buttons = self.driver.find_elements(*self._REMOVE_BUTTON)
        if remove_buttons and item_index < len(remove_buttons):
            remove_buttons[item_index].click()