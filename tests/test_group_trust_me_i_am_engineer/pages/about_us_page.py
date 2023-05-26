from tests.test_group_trust_me_i_am_engineer.locators.page_locators import MainPageLocators, AboutUsPageLocators
from tests.test_group_trust_me_i_am_engineer.pages.main_page import MainPage
from conftest import load_div
from selenium.webdriver.support import expected_conditions as EC

class AboutUsPage(MainPage):
    locators = MainPageLocators
    page_locators = AboutUsPageLocators

    def verify_correct_header_about_us_page(self, wait):
        self.driver.get(self.URL)
        wait.until_not(EC.presence_of_element_located(load_div))

        self.allow_all_cookies()
        self.element_is_clickable(self.locators.ABOUT_US_BUTTON).click()

        self.element_is_visible(self.page_locators.HEADER)

        assert self.element_is_visible(self.page_locators.HEADER).text == "OpenWeather\nglobal services"
