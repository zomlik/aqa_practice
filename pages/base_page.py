import allure


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, args):
        return self.browser.find_element(*args)

    def go_to(self, url):
        with allure.step("Open page"):
            return self.browser.get(url)
