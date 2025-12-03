import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)

    yield driver
    driver.quit()
