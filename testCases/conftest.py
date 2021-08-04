import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROME_EXECUTABLE_PATH = './chromedriver.exe'

@pytest.fixture()
def setup():
    print("Intentando abrir navegador.")
    driver_options = Options()
    driver_options.add_argument('--start-maximized')
    driver_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(CHROME_EXECUTABLE_PATH, options=driver_options)
    return driver