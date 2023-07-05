from pages.base_page import BasePage
from locators.locators import AboutUsPageLocators
from test_data.urls import AboutUsPage_urls

class AboutUsPage(BasePage):
    locators = AboutUsPageLocators()
    ABOUT_US_URL = 'https://openweathermap.org/about-us'
    urls = AboutUsPage_urls()

    def verify_correct_header_about_us_page(self):
        self.element_is_visible(self.locators.HEADER)

        assert self.element_is_visible(self.locators.HEADER).text == "OpenWeather\nglobal services"

    def verify_image_beside_header_is_displayed(self):
        image_beside_header = self.element_is_visible(self.locators.IMAGE_BESIDE_HEADER)

        assert image_beside_header.is_displayed(), "The image is not displayed beside the page header"

    def verify_five_headers_on_the_page_about_us_footer(self):
        list_headers_on_page_footer = [el.text for el in
                                       self.elements_are_visible(self.locators.HEADERS_ON_PAGE_FOOTER)]

        assert list_headers_on_page_footer == ['Product Collections', 'Subscription', 'Company', 'Technologies',
                                               'Terms & Conditions']

    def click_news_and_updates_button(self):
        self.element_is_clickable(self.locators.NEWS_AND_UPDATES_BUTTON).click()

    def click_on_app_store_button(self):
        self.element_is_clickable(self.locators.APP_STORE_BUTTON).click()

    def check_cursor_style_transformation(self, element):
        element = element
        self.action_move_to_element(element)
        cursor_style = element.value_of_css_property("cursor")

        assert cursor_style == "pointer", "Cursor is not transformed into a hand pointer."

    def contact_us_button_is_visible_and_clickable(self):
        self.driver.get(self.ABOUT_US_URL)
        self.allow_all_cookies()
        link = self.element_is_clickable(self.locators.CONTACT_US_BUTTON)
        assert link.is_enabled(), "The 'Contact us' button is not clickable"

    def verify_redirection_contact_us_button_to_the_new_webpage(self):
        self.driver.get(self.ABOUT_US_URL)
        self.allow_all_cookies()
        self.find_element_and_click(self.locators.CONTACT_US_BUTTON)
        self.switch_to_new_window()
        contact_us_button_link = self.driver.current_url
        assert contact_us_button_link == "https://home.openweathermap.org/questions"

    def verify_4_orange_buttons_are_visible_and_clickable(self):
        self.driver.get(self.ABOUT_US_URL)
        find_4_buttons = self.driver.find_elements(*self.locators.ORANGE_BUTTONS)
        assert [i.is_displayed() and i.is_enabled() for i in find_4_buttons]

    def verify_3_orange_buttons_redirection(self):
        for locator, expected_url in zip(self.locators.ORANGE_BUTTONS_1_2_3, self.urls.ORANGE_BUTTONS_URLS_1_2_3):
            self.driver.get(self.ABOUT_US_URL)
            self.scroll_to_the_element(self.locators.WHERE_TO)
            link = self.driver.find_element(*locator)
            link.click()
            assert expected_url == self.driver.current_url

    def verify_redirection_of_news_and_updates_button(self):
        self.driver.get(self.ABOUT_US_URL)
        self.allow_all_cookies()
        self.check_link_in_new_window(self.locators.NEWS_AND_UPDATES, self.urls.NEWS_AND_UPDATES_URL)


