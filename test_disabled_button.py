from pages.buttons import DisabledButton
from selenium.webdriver.common.by import By

URL = "https://www.qa-practice.com/elements/button/disabled"


def test_button_select_is_disabled(browser):
    button_disabled = DisabledButton(browser)
    button_disabled.go_to(URL)
    assert browser.find_element(By.ID, "id_select_state").get_attribute("value") == "disabled"


def test_button_click(browser):
    click_button_disabled = DisabledButton(browser)
    click_button_disabled.go_to(URL)
    click_button_disabled.disabled_button_select(select_name="enabled")
    click_button_disabled.disabled_button_click()
    assert browser.find_element(By.ID, "result-text").text == "Submitted"


def test_button_disabled_enabled(browser):
    button = DisabledButton(browser)
    button.go_to(URL)
    button.disabled_button_select(select_name='enabled')
    assert browser.find_element(By.ID, "id_select_state").get_attribute("value") == "enabled"
    assert button.disabled_button_find().is_enabled
    button.disabled_button_select(select_name="disabled")
    assert browser.find_element(By.ID, "id_select_state").get_attribute("value") == "disabled"


