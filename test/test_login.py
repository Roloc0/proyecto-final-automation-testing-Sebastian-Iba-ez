from page.login_page import LoginPage
import time

#inicio de sesion
def test_login(driver):
    loginPage = LoginPage(driver)
    loginPage.open()
    loginPage.login()
    time.sleep(5)