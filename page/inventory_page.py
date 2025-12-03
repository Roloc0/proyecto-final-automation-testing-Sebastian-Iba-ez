from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    _URL_CURRENT = "/inventory.html"
    _TITLE = (By.CLASS_NAME, "title") 
    _PRODUCTS = (By.CLASS_NAME, "inventory_item") 
    _ADD_BUTTONS = (By.CSS_SELECTOR, "button[data-test*='add-to-cart']") 
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge") 
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link") 

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def agregar_producto(self):
        primer_boton = self.driver.find_elements(*self._ADD_BUTTONS)[0] 
        primer_boton.click() 
        return self

    def ir_al_carrito(self):
        self.driver.find_element(*self._CART_LINK).click()