Proyecto Final – Automatización de Pruebas (QA)

Este proyecto implementa un conjunto completo de pruebas automatizadas de UI (Selenium) y API (Requests), junto con generación de reportes HTML, capturas de pantalla automáticas y sistema de logging.  
El objetivo es demostrar el uso de buenas prácticas en automatización, estructura profesional del framework y ejecución de pruebas integradas.

Tecnologías Utilizadas
    -Python
    -Pytest
    -Selenium WebDriver
    -Requests
    -Pytest-HTML
    -Google Chrome + Chromedriver
    -Logging (módulo estándar de Python)
    -Page Object Model (POM)

Estructura del Proyecto
📂Carpeta principal del proyecto
    📂page (Carpeta donde se encuentran los POM)
        📄login_page.py
        📄inventory_page.py
        📄cart_page.py
        📄checkout_page.py
    📂test (Carpeta donde se encuentran los Tests UI con Selenium)
        📄test_login.py
        📄test_login_fail.py
        📄test_inventory.py
        📄test_cart.py
        📄test_checkout.py
    📂test_api (Carpeta de test API con Requests)
        📄test_api_get.py
        📄test_api_put.py
        📄test_api_delete.py
    📂reports (reportes generados de las pruebas, tanto screenshots, como logs y reporte HTML)
        📂Screenshots
        📂Logs
        📄report.HTML
    📄conftest.py
    📄README.md

¿Cómo instalar las dependencias?
Ejecutar "pip install selenium pytest requests pytest-html"

¿Cómo ejecutar las pruebas?
Ejecutar "pytest -v -s" iniciara todas las pruebas
Ejecutar "pytest --html=reports/report.html --self-contained-html -v -s" iniciara todas las pruebas y genera un reporte HTML