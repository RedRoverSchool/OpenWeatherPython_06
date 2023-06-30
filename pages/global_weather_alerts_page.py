from pages.base_page import BasePage
from locators.locators import GlobalWeatherAlertsLocators as GWAL
from test_data.urls import GlobalWeatherAlertsUrls as GWAU
from test_data.urls import ApiPageUrls as APU
from test_data.global_weather_alerts_page_data import body_link_color


class GlobalWeatherAlertsPage(BasePage):

    def verify_redirection_of_7_anchor_links(self):
        for anchor_locator, expected_url in zip(GWAL.SEVEN_ANCHOR_LOCATORS, GWAU.SEVEN_ANCHOR_LINKS):
            address_bar = "https://openweathermap.org/api/push-weather-alerts#"
            link = self.driver.find_element(*anchor_locator)
            self.action_move_to_element(link)
            link.click()
            print(self.driver.current_url)
            link_href = link.get_attribute('href')
            assert address_bar in self.driver.current_url and self.driver.current_url == expected_url, \
                f'Redirection of the anchor link "{link_href}" is not successful'

    def verify_visibility_and_headings_correctness_of_5_blocks_(self):
        for block_locator, expected_heading in GWAL.BODY_HEADINGS.items():
            block = self.driver.find_element(*block_locator)
            print(block)
            assert block.is_displayed() and block.text == expected_heading, \
                f'"{block.text}" is not displayed or has wrong text'

    def verify_16_body_links_have_the_same_color(self):
        self.check_several_elements_color(GWAL.SIXTEEN_BODY_LINKS, body_link_color)

    def verify_16_body_links_are_visible_and_clickable(self):
        self.verify_links_are_visible_and_clickable(GWAL.SIXTEEN_BODY_LINKS)

    def verify_redirection_of_9_body_links(self):
        address_bar = APU.GLOBAL_WEATHER_ALERTS_LINK
        self.allow_all_cookies(timeout=3)
        for locator, expected_url in zip(GWAL.NINE_BODY_LINKS_LOCATORS, GWAU.NINE_BODY_LINKS):
            link = self.driver.find_element(*locator)
            self.action_move_to_element(link)
            link_href = link.get_attribute('href')
            link.click()
            if link_href in GWAU.NINE_BODY_LINKS and link_href != GWAU.MAIL1:
                assert self.driver.current_url == expected_url, \
                   f'Redirection of the link "{link_href}" is not successful'
                if address_bar not in self.driver.current_url:
                    self.driver.execute_script("window.history.go(-1)")
            elif link_href == GWAU.MAIL1:
                print(f'{link_href} is an email')
            else:
                print(f'Wrong {link_href}')

