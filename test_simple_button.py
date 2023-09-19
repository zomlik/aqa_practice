from selenium.webdriver.common.by import By
from pages.buttons import SimpleButtons

URL = 'https://www.qa-practice.com/elements/button/simple'


def test_simple_button_label(browser):
    simple_label = SimpleButtons(browser)
    simple_label.go_to(URL)
    simple_label.simple_button_find()
    assert simple_label.simple_button_label() == "Click"


def test_simple_button_click(browser):
    simple_click = SimpleButtons(browser)
    simple_click.go_to(URL)
    simple_click.simple_button_find()
    simple_click.simple_click()
    assert browser.find_element(By.ID, "result-text").text == "Submitted"


def test_button_is_enable(browser):
    simple_enable = SimpleButtons(browser)
    simple_enable.go_to(URL)
    assert simple_enable.simple_button_find().is_enabled()
