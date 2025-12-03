import pytest
from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
from page.checkout_page import CheckoutPage
import time

def test_cart_operations(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    #Inicia sesion
    login.open()
    login.login("standard_user", "secret_sauce")
    time.sleep(3)

    #Agregar producto e ir al carrito
    inventory.agregar_producto()
    inventory.ir_al_carrito()

    #Va al checkout
    cart.click_checkout()

    #Llenar los datos y continuar
    checkout.agregar_datos("Jose", "Rodriguez", "6848")
    checkout.continuar()
    time.sleep(4)