from pages.base_page import BasePage
from locators.locators import AboutUsPageLocators


class AboutUsPage(BasePage):
    locators = AboutUsPageLocators()

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
