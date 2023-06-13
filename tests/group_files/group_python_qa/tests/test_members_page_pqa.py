from tests.group_files.group_python_qa.pages.members_page_pqa import Members
from tests.group_files.group_python_qa.links.links_all_pages import URL_SUBSCRIPTION_BASE
from tests.group_files.group_python_qa.locators.locators import MembersLocators


class TestMembersPage:

    def test_tc_018_01_02_verify_error_messages_for_empty_required_fields(self, driver):
        members_page = Members(driver, URL_SUBSCRIPTION_BASE)
        members_page.open_page()
        members_page.find_element_and_click(MembersLocators.CONTINUE_TO_PAYMENT_BUTTON)
        members_page.verify_error_messages_for_empty_required_fields()
