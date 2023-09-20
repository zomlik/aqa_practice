from pages.buttons import LookLikeButton

URL = 'https://www.qa-practice.com/elements/button/like_a_button'


def test_look_like_button_click(browser):
    click_like_button = LookLikeButton(browser)
    click_like_button.go_to(URL)
    click_like_button.like_button_find()
    click_like_button.like_button_click()
    assert click_like_button.like_button_find().text == "Click"


def test_look_like_button_label(browser):
    lebel_like_button = LookLikeButton(browser)
    lebel_like_button.go_to(URL)
    assert lebel_like_button.like_button_label() == "Click"


def test_look_like_button_is_enable(browser):
    enable_like_button = LookLikeButton(browser)
    enable_like_button.go_to(URL)
    assert enable_like_button.like_button_find().is_enabled()
