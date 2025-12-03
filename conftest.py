import pytest
import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

SCREENSHOT_DIR = Path("reports/screenshots")
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Captura screenshots automáticamente cuando un test falla."""
    
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"{item.name}_{timestamp}.png"
            filepath = SCREENSHOT_DIR / filename

            driver.save_screenshot(str(filepath))
            print(f"\n📸 Screenshot guardado en: {filepath}\n")