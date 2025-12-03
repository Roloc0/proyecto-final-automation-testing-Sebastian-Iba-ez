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

    #Agregar producto e ir al carrito
    inventory.agregar_producto()
    inventory.ir_al_carrito()
    time.sleep(4)