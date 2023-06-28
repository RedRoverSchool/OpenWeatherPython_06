from pages.base_page import BasePage
from locators.locators import GlobalWeatherAlertsLocators as GWAL
from test_data.urls import GlobalWeatherAlertsUrls as GWAU


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
