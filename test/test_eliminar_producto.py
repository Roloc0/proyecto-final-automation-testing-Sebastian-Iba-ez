import pytest
from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
import time

def test_cart_operations(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    # Inicia sesion
    login.open()
    login.login("standard_user", "secret_sauce")
    time.sleep(4)

    # Agregar producto e ir al carrito
    inventory.agregar_producto()
    inventory.ir_al_carrito()
    time.sleep(2)

    # Quitar el producto
    cart.remove_item()
    time.sleep(2)