import allure


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, args):
        return self.browser.find_element(*args)

    @allure.step("Открытие страницы")
    def go_to(self, url: str):
        return self.browser.get(url)
