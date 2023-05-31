from pages.base_page import BasePage
from tests.test_group_trust_me_i_am_engineer.locators.page_locators import MainPageLocators, AboutUsPageLocators
from conftest import load_div
from selenium.webdriver.support import expected_conditions as EC

class AboutUsPage(BasePage):
    URL = "https://openweathermap.org/about-us"
    locators = MainPageLocators
    page_locators = AboutUsPageLocators

    def open_about_us_page(self):
        self.driver.get(self.URL)
        self.allow_all_cookies()

    def go_to_about_us_page(self, wait):
        self.driver.get(self.URL)
        wait.until_not(EC.presence_of_element_located(load_div))

        self.allow_all_cookies()
        self.element_is_clickable(self.locators.ABOUT_US_BUTTON).click()

    def verify_correct_header_about_us_page(self, wait):
        self.go_to_about_us_page(wait)

        self.element_is_visible(self.page_locators.HEADER)

        assert self.element_is_visible(self.page_locators.HEADER).text == "OpenWeather\nglobal services"

    def verify_image_beside_header_is_displayed(self, wait):
        self.go_to_about_us_page(wait)

        image_beside_header = self.element_is_visible(self.page_locators.IMAGE_BESIDE_HEADER)
        assert image_beside_header.is_displayed(), "The image is not displayed beside the page header"

    def verify_there_are_five_headers_on_the_page_about_us_footer(self, wait):
        self.go_to_about_us_page(wait)

        headers_on_page_footer = self.elements_are_visible(self.page_locators.HEADERS_ON_PAGE_FOOTER)
        list_headers_on_page_footer = [el.text for el in headers_on_page_footer]

        assert list_headers_on_page_footer == ['Product Collections', 'Subscription', 'Company', 'Technologies', 'Terms & Conditions']

    def click_news_and_updates_button(self):
        self.element_is_clickable(self.page_locators.NEWS_AND_UPDATES_BUTTON).click()

    def verify_current_url(self, button, expected_link):
        self.driver.switch_to.window(self.driver.window_handles[1])
        button_url = self.driver.current_url
        assert button_url == expected_link, button + " button link is not correct"



