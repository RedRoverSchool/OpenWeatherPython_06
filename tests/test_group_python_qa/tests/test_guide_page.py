import time

from tests.test_group_python_qa.pages.guide_page import GuidePage


def test_TC_004_08_01_historical_collection_block_visibility(driver):
    page = GuidePage(driver)
    page.historical_collection_block_visibility()



def test_TC_004_08_02_link_to_history_archive_is_clickable(driver):
    page = GuidePage(driver, GuidePage.URL_GUIDE_PAGE)
    page.open_page()
    page.link_to_history_archive_is_clickable()