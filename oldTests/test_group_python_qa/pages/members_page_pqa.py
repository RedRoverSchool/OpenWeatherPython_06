from pages.base_page import BasePage
from oldTests.test_group_python_qa.locators.locators import MembersLocators
from oldTests.test_group_python_qa.test_data.data_pqa import EXPECTED_NUMBER_OF_FIELDS


class Members(BasePage):
    locator = MembersLocators()

    def verify_error_messages_for_empty_required_fields(self):
        error_messages = self.elements_are_visible(MembersLocators.CANT_BE_BLANK)
        assert len(error_messages) == EXPECTED_NUMBER_OF_FIELDS, "The number of fields with error massages do not match"
