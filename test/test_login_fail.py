from page.login_page import LoginPage
import time

#inicio de sesion
def test_login(driver):
    loginPage = LoginPage(driver)
    loginPage.open()
    loginPage.login("asd", "dsa")

    #Muestra el error
    error_message = loginPage.mensaje_error()
    assert "Username and password do not match" in error_message
    time.sleep(3)