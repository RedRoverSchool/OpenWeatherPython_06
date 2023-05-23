from pages.base_page import BasePage
from tests.test_group_trust_me_i_am_engineer.locators.page_locators import OurInitiativesPageLocators

class OurInitiativesPage(BasePage):
    URL_OUR_INITIATIVES = 'https://openweathermap.org/our-initiatives'
    locators = OurInitiativesPageLocators()
    def verify_learn_more_link_redirects_to_valid_page(self):
        self.driver.get(self.URL_OUR_INITIATIVES)
        self.driver.execute_script("window.scrollTo(0, 500)")
        self.driver.find_element(*self.locators.LEARN_MORE_LINK).click()
        pricing_text = self.driver.find_element(*self.locators.LEARN_MORE_PAGE_TITLE).text
        assert pricing_text == "Student initiative"
