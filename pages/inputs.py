import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

LOCATER_TEXT_INPUT = (By.ID, "id_text_string")
LOCATER_RESULT = (By.CSS_SELECTOR, "#result-text")
LOCATER_ERROR = (By.CSS_SELECTOR, "#error_1_id_text_string strong")


class TextInput(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Поиск текстового поля")
    def find_text_input(self):
        return self.find(LOCATER_TEXT_INPUT)

    @allure.step("Отправка текста")
    def send_text_to_field(self, keys: str):
        return self.find_text_input().send_keys(keys)

    @allure.step("Нажатие кнопки Enter")
    def send_keys_enter(self):
        return self.find_text_input().send_keys(Keys.ENTER)

    @allure.step("Сообщение об ошибки")
    def error_message(self):
        return self.find(LOCATER_ERROR).text

    @allure.step("Проверка результата")
    def results(self):
        return self.find(LOCATER_RESULT).text
