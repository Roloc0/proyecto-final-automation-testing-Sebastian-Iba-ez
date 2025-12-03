from page.login_page import LoginPage
import time

#inicio de sesion
def test_login(driver):
    loginPage = LoginPage(driver)
    loginPage.open()
    loginPage.login("standard_user", "secret_sauce")
    time.sleep(3)