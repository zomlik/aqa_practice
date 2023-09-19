from pages.base_page import BasePage
from selenium.webdriver.common.by import By

LOCATER_SIMPLE_BUTTON = (By.ID, "submit-id-submit")


class SimpleButtons(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def simple_button_find(self):
        return self.find(LOCATER_SIMPLE_BUTTON)

    def simple_click(self):
        return self.simple_button_find().click()

    def simple_button_label(self):
        return self.simple_button_find().get_attribute('value')

