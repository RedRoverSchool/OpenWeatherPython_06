
from tests.test_group_future_auto_qa.pages.about_us_page import AboutUsPage


def test_TC_001_15_08_contact_us_button_is_clickable(driver):
    about_us_page = AboutUsPage(driver)
    about_us_page.open()
    about_us_page.scroll_to_contact_us_button()
    assert about_us_page.contact_us_button_is_clickable()
