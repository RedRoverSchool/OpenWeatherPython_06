
from oldTests.test_group_future_auto_qa.pages.about_us_page import AboutUsPage


def test_TC_001_15_08_contact_us_button_is_clickable(driver):
    about_us_page = AboutUsPage(driver)
    about_us_page.open()
    about_us_page.scroll_to_contact_us_button()
    assert about_us_page.contact_us_button_is_clickable()

def test_TC_001_15_06_Verify_correct_redirection_of_the_contact_us_button(driver):
    about_us_page = AboutUsPage(driver)
    about_us_page.open()
    # Allow all cookies so that the test can interact with the Contact Us button
    about_us_page.allow_all_cookies()
    about_us_page.verify_redirection_contact_us_button_to_the_new_webpage()

