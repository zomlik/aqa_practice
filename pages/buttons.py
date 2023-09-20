from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

LOCATER_SIMPLE_BUTTON = (By.ID, "submit-id-submit")
LOCATER_LOOK_LIKE_BUTTON = (By.CSS_SELECTOR, ".a-button")
LOCATER_DISABLED_BUTTON = (By.ID, "submit-id-submit")
LOCATER_DISABLED_BUTTON_SELECT = (By.ID, "id_select_state")


class SimpleButtons(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def simple_button_find(self):
        return self.find(LOCATER_SIMPLE_BUTTON)

    def simple_click(self):
        return self.simple_button_find().click()

    def simple_button_label(self):
        return self.simple_button_find().get_attribute('value')


class LookLikeButton(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def like_button_find(self):
        return self.find(LOCATER_LOOK_LIKE_BUTTON)

    def like_button_click(self):
        return self.like_button_find().click()

    def like_button_label(self):
        return self.like_button_find().text

class DisabledButton(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def disabled_button_find(self):
        return self.find(LOCATER_SIMPLE_BUTTON)

    def disabled_button_select(self, select_name):
        find_select_element = self.find(LOCATER_DISABLED_BUTTON_SELECT)
        select = Select(find_select_element)
        return select.select_by_value(select_name)
    
    def disabled_button_click(self):
        return self.disabled_button_find().click()
