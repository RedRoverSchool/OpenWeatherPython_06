import time

from tests.test_group_python_qa.links.links_all_pages import GUIDE_PAGE
from tests.test_group_python_qa.locators.locators import GuidePageLocators
from tests.test_group_python_qa.pages.guide_page import GuidePage


def test_TC_004_08_01_historical_collection_block_visibility(driver):
    page = GuidePage(driver)
    page.historical_collection_block_visibility()


def test_TC_004_08_02_link_to_history_archive_is_clickable(driver):
    page = GuidePage(driver, GuidePage.URL_GUIDE_PAGE)
    page.open_page()
    page.link_to_history_archive_is_clickable()

def test_tc_004_08_03_historical_collection_link_redirects_correctly(driver):
    page = GuidePage(driver, GUIDE_PAGE)
    page.open_page()
    page.footer_click_allow()
    page.find_element_and_click(GuidePageLocators.LINK_HISTORICAL_ARCHIVE)
    page.check_historical_collection_link_redirection()