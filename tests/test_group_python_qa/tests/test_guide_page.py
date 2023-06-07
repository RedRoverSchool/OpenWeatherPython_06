from tests.test_group_python_qa.links.links_all_pages import GUIDE_PAGE, URL_HISTORY_BULK
from tests.test_group_python_qa.locators.locators import GuidePageLocators
from tests.test_group_python_qa.pages.guide_page import GuidePage


class TestGuidePage:

    def test_tc_004_08_01_historical_collection_block_visibility(self, driver):
        page = GuidePage(driver, GUIDE_PAGE)
        page.open_page()
        page.element_is_visible(GuidePageLocators.HISTORICAL_COLLECTION_MODULE)

    def test_tc_004_08_02_link_to_history_archive_is_clickable(self, driver):
        page = GuidePage(driver, GUIDE_PAGE)
        page.open_page()
        page.link_to_history_archive_is_clickable()

    def test_tc_004_08_03_historical_collection_link_redirects_correctly(self, driver):
        page = GuidePage(driver, GUIDE_PAGE)
        page.open_page()
        page.footer_click_allow()
        page.find_element_and_click(GuidePageLocators.LINK_HISTORICAL_ARCHIVE)
        page.check_for_redirection(URL_HISTORY_BULK)
