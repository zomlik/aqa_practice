from pages.buttons import LookLikeButton
import allure

URL = 'https://www.qa-practice.com/elements/button/like_a_button'


@allure.feature("Look like button")
@allure.title("Look like button click")
def test_look_like_button_click(browser):
    click_like_button = LookLikeButton(browser)
    click_like_button.go_to(URL)
    click_like_button.like_button_find()
    click_like_button.like_button_click()
    with allure.step("Label button is 'Click'"):
        assert click_like_button.like_button_find().text == "Click"


@allure.feature("Look like button")
@allure.title("Look like button label")
def test_look_like_button_label(browser):
    lebel_like_button = LookLikeButton(browser)
    lebel_like_button.go_to(URL)
    with allure.step("Button is clicked"):
        assert lebel_like_button.like_button_label() == "Click"


@allure.feature("Look like button")
@allure.title("Look like button is enabled")
def test_look_like_button_is_enable(browser):
    enable_like_button = LookLikeButton(browser)
    enable_like_button.go_to(URL)
    with allure.step("button is enabled"):
        assert enable_like_button.like_button_find().is_enabled()
