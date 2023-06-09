from pages.base_page import BasePage
from locators.locators import MembersPageLocators
from test_data.miscellaneous import MembersPageData
from test_data.members_page_data import names_of_fields_for_individual as ind,\
    names_of_fields_for_organisation as org


class MembersPage(BasePage):

    def verify_error_messages_for_empty_required_fields(self):
        error_messages = self.elements_are_visible(MembersPageLocators.CANT_BE_BLANK)
        assert len(error_messages) == MembersPageData.EXPECTED_NUMBER_OF_FIELDS, \
            "The number of fields with error massages do not match"

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
