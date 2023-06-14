from pages.guide_page import GuidePage
from locators.locators import GuideLocators, BasePageLocators
from test_data.urls import GuidePageUrls
from test_data.all_links import Links


class TestGuidePage:

    def test_tc_004_08_01_historical_collection_block_visibility(self, driver):
        page = GuidePage(driver, GuidePageUrls.GUIDE_PAGE)
        page.open_page()
        page.element_is_visible(GuideLocators.HISTORICAL_COLLECTION_MODULE)

    def test_tc_004_08_02_link_to_history_archive_is_clickable(self, driver):
        page = GuidePage(driver, GuidePageUrls.GUIDE_PAGE)
        page.open_page()
        page.link_to_history_archive_is_clickable()

    def test_tc_004_08_03_historical_collection_link_redirects_correctly(self, driver):
        page = GuidePage(driver, GuidePageUrls.GUIDE_PAGE)
        page.open_page()
        page.footer_click_allow()
        page.find_element_and_click(GuideLocators.LINK_HISTORICAL_ARCHIVE)
        page.check_for_redirection(GuidePageUrls.URL_HISTORY_BULK)

    def test_tc_004_08_04_verify_all_historical_collection_links_same_color(self, driver):
        page = GuidePage(driver, GuidePageUrls.GUIDE_PAGE)
        page.open_page()
        page.verify_several_links_color(GuideLocators.HISTORICAL_COLLECTION_LINKS)

    def test_TC_002_01_01_return_from_guide_page_to_main_page_by_clicking_on_logo(self, driver):
        page = GuidePage(driver, GuidePageUrls.GUIDE_PAGE)
        page.open_page()
        page.check_link(BasePageLocators.LOGO_LOCATOR, Links.URL_MAIN_PAGE)

    def test_tc_002_03_03_01_open_guide(self, driver, open_and_load_main_page):
        guide_page = GuidePage(driver)
        guide_page.check_header_title("guide")
