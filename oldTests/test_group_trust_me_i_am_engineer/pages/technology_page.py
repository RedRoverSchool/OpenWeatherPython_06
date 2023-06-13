from pages.base_page import BasePage
from oldTests.test_group_trust_me_i_am_engineer.locators.page_locators import TechnologyPageLocators

class TechnologyPage(BasePage):
    URL_TECHNOLOGY = 'https://openweathermap.org/technology'
    detailed_report_link = 'https://openweathermap.org/accuracy-and-quality'
    locators = TechnologyPageLocators()

    def verify_link_detailed_report_clickability_redirection(self):
        self.driver.get(self.URL_TECHNOLOGY)
        self.driver.execute_script("window.scrollTo(0, 500)")
        detailed_report = self.driver.find_element(*self.locators.DETAILED_REPORT_LINK)
        self.driver.execute_script("arguments[0].click();", detailed_report)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.detailed_report_link, self.driver.current_url
