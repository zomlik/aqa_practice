from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture()
def chrome_option():
    option = Options()
    option.add_argument("--headless")
    return option


@pytest.fixture()
def browser(chrome_option):
    chrome_browser = webdriver.Chrome(chrome_option)
    chrome_browser.implicitly_wait(10)
    yield chrome_browser
    chrome_browser.quit()
