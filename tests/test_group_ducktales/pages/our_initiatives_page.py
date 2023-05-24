from pages.base_page import BasePage
from tests.test_group_ducktales.locators.our_initiatives_page_locators import OurInitiativesPageLocators


class OurInitiativesPage(BasePage):
    locators = OurInitiativesPageLocators()

    def get_section_element(self, section):
        section_locator = (self.locators.SECTION[0], self.locators.SECTION[1].format(section))
        return self.element_is_present(section_locator)

    def click_initiatives_link(self):
        our_initiatives_link = self.element_is_present(self.locators.INITIATIVES)
        our_initiatives_link.click()

    def click_education_learn_more(self):
        education_learn_more = self.element_is_present(self.locators.EDUCATION_LEARN_MORE)
        self.driver.execute_script("window.scrollBy(0, 500);")
        self.action_move_to_element(education_learn_more)
        education_learn_more.click()
