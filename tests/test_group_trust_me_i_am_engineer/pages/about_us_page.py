from pages.base_page import BasePage
from tests.test_group_trust_me_i_am_engineer.locators.page_locators import MainPageLocators, AboutUsPageLocators

class AboutUsPage(BasePage):
    URL = "https://openweathermap.org/about-us"
    page_locators = AboutUsPageLocators

    def verify_correct_header_about_us_page(self, wait):
        self.element_is_visible(self.page_locators.HEADER)
        assert self.element_is_visible(self.page_locators.HEADER).text == "OpenWeather\nglobal services"

    def verify_image_beside_header_is_displayed(self, wait):
        image_beside_header = self.element_is_visible(self.page_locators.IMAGE_BESIDE_HEADER)
        assert image_beside_header.is_displayed(), "The image is not displayed beside the page header"

    def verify_five_headers_on_the_page_about_us_footer(self, wait):
        list_headers_on_page_footer = [el.text for el in self.elements_are_visible(self.page_locators.HEADERS_ON_PAGE_FOOTER)]
        assert list_headers_on_page_footer == ['Product Collections', 'Subscription', 'Company', 'Technologies', 'Terms & Conditions']

    def click_news_and_updates_button(self):
        self.element_is_clickable(self.page_locators.NEWS_AND_UPDATES_BUTTON).click()

    def verify_current_url(self, button, expected_link):
        self.driver.switch_to.window(self.driver.window_handles[1])
        button_url = self.driver.current_url
        assert button_url == expected_link, button + " button link is not correct"

    def click_on_app_store_button(self):
        self.element_is_clickable(self.page_locators.APP_STORE_BUTTON).click()

    def verify_element_on_current_url(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        expected_element = self.element_is_visible(self.page_locators.APP_TITLE)
        print(expected_element.text)
        assert expected_element.text == "OpenWeather 4+"





