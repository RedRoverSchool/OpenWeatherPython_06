from tests.group_files.group_no_pain_no_gain.pages.partners_page import Partners
from tests.group_files.group_no_pain_no_gain import links
from tests.group_files.group_no_pain_no_gain.test_data.partners_page_data import PartnersPageData as PPD
from tests.group_files.group_no_pain_no_gain.locators.partners_page_locators import PartnersPageLocators as PPL
import pytest
class TestPartnersPage:
    def test_TC_011_01_01_verify_that_Partners_and_solutions_page_title_is_correct(self, driver):
        page = Partners(driver, link=links.PARTNERS_AND_SOLUTIONS)
        page.open_page()
        page.check_page_title(PPD.PARTNERS_PAGE_TITLE)

    def test_TC_011_20_01_verify_that_the_info_board_message_at_the_top_of_the_page_is_displayed(self, driver):
        page = Partners(driver, links.PARTNERS_AND_SOLUTIONS)
        page.open_page()
        page.get_text_content_of_the_element(PPL.PARTNERS_PAGE_INFO_BOARD, PPD.PARTNERS_PAGE_INFO_BOARD_TEXT)

    def test_TC_011_20_02_verify_the_color_of_the_info_board_message_at_the_top_of_the_page(self, driver):
        page = Partners(driver, links.PARTNERS_AND_SOLUTIONS)
        page.open_page()
        page.get_background_color_of_the_element(PPL.PARTNERS_PAGE_INFO_BOARD, PPD.INFO_BOARD_BACKGROUND_COLOR)

    def test_TC_011_01_02_verify_that_the_heading_of_the_page_equals_to_Partners_and_solutions(self, driver):
        page = Partners(driver, links.PARTNERS_AND_SOLUTIONS)
        page.open_page()
        page.get_text_content_of_the_element(PPL.PARTNERS_PAGE_HEADING, PPD.PARTNERS_PAGE_HEADING)

    def test_TC_011_12_01_verify_the_link_in_raspberry_is_visible_and_clickable(self, driver):
        page = Partners(driver, links.PARTNERS_AND_SOLUTIONS)
        page.open_page()
        page.link_visibility_and_clickability(PPL.RASPBERRY, links.RASPBERRY_GITHUB)

    def test_TC_011_06_01_verify_the_first_link_in_android_section_is_visible_and_clickable(self, driver):
        page = Partners(driver, links.PARTNERS_AND_SOLUTIONS)
        page.open_page()
        page.link_visibility_and_clickability(PPL.ANDROID_FIRST_LINK, links.ANDROID_WEATHER)

    def test_TC_011_20_03_verify_that_the_Github_link_in_the_info_board_message_is_visible_and_clickable(self, driver):
        page = Partners(driver, links.PARTNERS_AND_SOLUTIONS)
        page.open_page()
        page.link_visibility_and_clickability(PPL.INFO_BOARD_GITHUB_LINK, links.INFO_BOARD_GITHUB)

    def test_TC_011_20_04_Verify_that_the_Github_link_in_the_info_board_message_leads_to_correct_page(self, driver):
        page = Partners(driver, links.PARTNERS_AND_SOLUTIONS)
        page.open_page()
        page.check_link_in_new_window(PPL.INFO_BOARD_GITHUB_LINK, links.INFO_BOARD_GITHUB)

    def test_TC_011_17_01_verify_the_mobile_link_leads_to_correct_page(self, driver):
        page = Partners(driver, links.PARTNERS_AND_SOLUTIONS)
        page.open_page()
        page.scroll_to_the_element(PPL.MOBILE_APP_BLOCK)
        page.check_link(PPL.MOBILE_APP_LINK, links.MOBILE_APP)

    @pytest.mark.parametrize('anchor_locators', PPL.ANCHOR_LOCATORS)
    def test_TC_011_19_01_Verify_that_the_anchor_links_are_clickable(self, driver, anchor_locators):
        page = Partners(driver, links.PARTNERS_AND_SOLUTIONS)
        page.open_page()
        page.element_clickability(anchor_locators)

