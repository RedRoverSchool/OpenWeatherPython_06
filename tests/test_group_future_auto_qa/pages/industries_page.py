from pages.base_page import BasePage


class IndustriesPage(BasePage):

    def check_email_link_in_talk_to_us_button(self, wait, button_locator, expected_link):
        self.driver.get("https://openweather.co.uk/industries")
        self.allow_all_cookies()
        simple_link = self.element_is_clickable(button_locator)
        link_href = simple_link.get_attribute('href')
        assert link_href == expected_link
