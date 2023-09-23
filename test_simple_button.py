from pages.buttons import SimpleButtons
from selenium.webdriver.common.by import By
import allure

URL = 'https://www.qa-practice.com/elements/button/simple'


@allure.feature("Simple button")
@allure.story("label")
def test_simple_button_label(browser):
    simple_label = SimpleButtons(browser)
    simple_label.go_to(URL)
    simple_label.simple_button_find()
    with allure.step("Label is 'Click"):
        assert simple_label.simple_button_label() == "Click"


@allure.feature("Simple button")
@allure.story("click")
def test_simple_button_click(browser):
    simple_click = SimpleButtons(browser)
    simple_click.go_to(URL)
    simple_click.simple_button_find()
    simple_click.simple_click()
    with allure.step('Button is clicked'):
        assert browser.find_element(By.ID, "result-text").text == "Submitted"


@allure.feature("Simple button")
@allure.story("enable")
def test_button_is_enable(browser):
    simple_enable = SimpleButtons(browser)
    simple_enable.go_to(URL)
    with allure.step("Simple button is enabled"):
        assert simple_enable.simple_button_find().is_enabled()
