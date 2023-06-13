from pages.base_page import BasePage
from locators.locators import MembersLocators
from test_data.miscellaneous import MembersPageData


class MembersPage(BasePage):
    locator = MembersLocators()

    def verify_error_messages_for_empty_required_fields(self):
        error_messages = self.elements_are_visible(MembersLocators.CANT_BE_BLANK)
        assert len(error_messages) == MembersPageData.EXPECTED_NUMBER_OF_FIELDS, \
        "The number of fields with error massages do not match"
