from tests.group_files.group_lutz_squad.pages.members_page import MembersPage
from tests.group_files.group_lutz_squad.locators.members_page_lacators import MembersPageLocators


def test_TC_018_02_02_verify_that_the_list_of_fields_changes_when_the_radio_button_is_toggled(driver):
    page = MembersPage(driver, link=MembersPageLocators.MEMBERS_PAGE_LINK)
    page.open_page()
    page.check_individual_radiobutton_is_selected()
    page.fields_for_individual_are_visible()
    page.check_organisation_radiobutton_is_selected()
    page.fields_for_organisation_are_visible()