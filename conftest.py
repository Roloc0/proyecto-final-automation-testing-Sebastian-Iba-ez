import pytest
import os
import logging
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime


#LOGGING CONFIG
LOG_DIR = Path("reports/logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / "test.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


#FIXTURE DEL DRIVER
@pytest.fixture
def driver():
    logging.info("Inicializando el navegador")

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    yield driver

    logging.info("Cerrando el navegador")
    driver.quit()


#CONFIGURACIÓN DE SCREENSHOTS
SCREENSHOT_DIR = Path("reports/screenshots")
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)


#screenshots + HTML report
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Captura screenshot al fallar y lo agrega al reporte HTML."""
    
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            # Crear nombre archivo
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"{item.name}_{timestamp}.png"
            filepath = SCREENSHOT_DIR / filename

            # Guardar screenshot
            driver.save_screenshot(str(filepath))

            logging.error(f"Test FAILED → Screenshot guardado en {filepath}")

            # Adjuntar al reporte HTML
            if hasattr(report, "extra"):
                from pytest_html import extras
                report.extra.append(extras.image(str(filepath)))