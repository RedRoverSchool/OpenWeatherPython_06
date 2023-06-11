from pages.members_page import MembersPage
from test_data.urls import MembersPageUrls
from locators.locators import MembersLocators


class TestMembersPage:

    def test_tc_018_01_02_verify_error_messages_for_empty_required_fields(self, driver):
        members_page = MembersPage(driver, MembersPageUrls.URL_SUBSCRIPTION_BASE)
        members_page.open_page()
        members_page.find_element_and_click(MembersLocators.CONTINUE_TO_PAYMENT_BUTTON)
        members_page.verify_error_messages_for_empty_required_fields()
