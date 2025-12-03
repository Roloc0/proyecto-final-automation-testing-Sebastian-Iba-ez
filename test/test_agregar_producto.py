import pytest
from page.login_page import LoginPage
from page.inventory_page import InventoryPage
import time

def test_cart_operations(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    #Inicia sesion
    login.open()
    login.login("standard_user", "secret_sauce")
    time.sleep(3)

    #Agregar producto y ir al carrito
    inventory.add_product_to_cart(0)
    inventory.go_to_cart()
    time.sleep(7)