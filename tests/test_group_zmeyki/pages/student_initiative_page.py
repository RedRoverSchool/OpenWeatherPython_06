from pages.base_page import BasePage
from tests.test_group_zmeyki.locators.student_initiative_locators import StudentInitiativeLocators


class StudentInitiativePage(BasePage):
    locators = StudentInitiativeLocators()


    def verify_website_link_redirects_to_main_page(self, wait):
        self.driver.get(self.locators.STUDENT_INITIATIVE_URL)
        website_link = self.driver.find_element(*self.locators.website_link_locator)
        self.driver.execute_script("arguments[0].click();", website_link)
        assert self.driver.current_url == 'https://openweathermap.org/'


