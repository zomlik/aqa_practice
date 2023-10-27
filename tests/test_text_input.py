import allure
from pages.inputs import TextInput
from selenium.webdriver.common.by import By

_URL = "https://www.qa-practice.com/elements/input/simple"


@allure.title("Текстовое поле на 1 символ")
def test_1_simbols_text_input(browser, keys="a"):
    text_1simbols = TextInput(browser)
    text_1simbols.go_to(_URL)
    text_1simbols.find_text_input()
    text_1simbols.send_text_to_field(keys=keys)
    text_1simbols.send_keys_enter()
    assert text_1simbols.error_message() == "Please enter 2 or more characters"


@allure.title("Текстовое поле на 2 символа")
def test_2_simbols_text_input(browser, keys="a_"):
    text_2simbols = TextInput(browser)
    text_2simbols.go_to(_URL)
    text_2simbols.find_text_input()
    text_2simbols.send_text_to_field(keys=keys)
    text_2simbols.send_keys_enter()
    assert text_2simbols.results() == keys


@allure.title("Текстовое поле на 2 символа")
def test_25_simbols_text_input(browser):
    keys = "asfrgdfgdhdffh13_dsgfdg-3"
    text_25simbols = TextInput(browser)
    text_25simbols.go_to(_URL)
    text_25simbols.find_text_input()
    text_25simbols.send_text_to_field(keys=keys)
    text_25simbols.send_keys_enter()
    assert text_25simbols.results() == keys


