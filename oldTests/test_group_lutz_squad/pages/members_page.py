from pages.base_page import BasePage
from oldTests.test_group_lutz_squad.locators.members_page_lacators import MembersPageLocators
from oldTests.test_group_lutz_squad.test_data.members_page_data import names_of_fields_for_individual as ind,\
    names_of_fields_for_organisation as org

class MembersPage(BasePage):
    def check_individual_radiobutton_is_selected(self):
        individual_radiobutton = self.driver.find_element(*MembersPageLocators.INDIVIDUAL_RADIOBUTTON)
        assert individual_radiobutton.is_selected()

    def fields_for_individual_are_visible(self):
        actual_fields = self.driver.find_element(*MembersPageLocators.LEFT_FIELDS_FOR_SUBSCRIPTION)
        for n in ind:
            assert n in actual_fields.text

    def check_organisation_radiobutton_is_selected(self):
        organisation_radiobutton = self.driver.find_element(*MembersPageLocators.ORGANISATION_RADIOBUTTON)
        organisation_radiobutton.click()
        assert organisation_radiobutton.is_selected()

    def fields_for_organisation_are_visible(self):
        actual_fields = self.driver.find_element(*MembersPageLocators.LEFT_FIELDS_FOR_SUBSCRIPTION)
        for n in org:
            assert n in actual_fields.text
