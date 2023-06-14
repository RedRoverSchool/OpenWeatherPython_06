from pages.members_page import MembersPage
from test_data.urls import MembersPageUrls
from locators.locators import MembersLocators


class TestMembersPage:

    def test_tc_018_01_02_verify_error_messages_for_empty_required_fields(self, driver):
        members_page = MembersPage(driver, MembersPageUrls.URL_SUBSCRIPTION_BASE)
        members_page.open_page()
        members_page.find_element_and_click(MembersLocators.CONTINUE_TO_PAYMENT_BUTTON)
        members_page.verify_error_messages_for_empty_required_fields()


class TestMembersPage:
    def test_TC_018_02_02_verify_that_the_list_of_fields_changes_when_the_radio_button_is_toggled(self, driver):
        page = MembersPage(driver, MembersPageUrls.MEMBERS_PAGE_LINK)
        page.open_page()
        page.check_individual_radiobutton_is_selected()
        page.fields_for_individual_are_visible()
        page.check_organisation_radiobutton_is_selected()
        page.fields_for_organisation_are_visible()

