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

    def test_TC_004_06_02_verify_visibility_and_clickability_One_Call_API_by_call_link(self, driver):
        page = GuidePage(driver, GuidePageUrls.GUIDE_PAGE)
        page.open_page()
        page.one_call_api_link_is_visible()
        page.one_call_api_link_is_clickable()

    def test_TC_004_06_03_verify_redirection_industry_standard_apis_link(self, driver, wait):
        page = GuidePage(driver, Links.GUIDE_PAGE)
        page.open_page()
        page.industry_standard_apis_link_redirection()

    def test_TC_004_06_04_verify_redirection_one_call_api_by_call_link(self, driver, wait):
        page = GuidePage(driver, Links.GUIDE_PAGE)
        page.open_page()
        page.one_call_api_by_call_link_redirection()

    def test_TC_004_06_07_verify_button_subscribe_to_onecall_by_call_is_visible(self, driver, wait):
        page = GuidePage(driver, Links.GUIDE_PAGE)
        page.open_page()
        page.subscribe_to_onecall_by_call_button_is_visible()

    def test_TC_002_01_01_return_from_guide_page_to_main_page_by_clicking_on_logo(self, driver):
        page = GuidePage(driver, GuidePageUrls.GUIDE_PAGE)
        page.open_page()
        page.check_link(BasePageLocators.LOGO_LOCATOR, Links.URL_MAIN_PAGE)

    def test_tc_004_05_01(self, driver):
        driver.get(GuideLocators.GUIDE_URL)
        for url_locators in GuideLocators.guide_fast_way_links_locators:
            link_fast_way = driver.find_element(*url_locators)
            assert link_fast_way.is_displayed()
    def test_tc_002_03_03_01_open_guide(self, driver, open_and_load_main_page):
        guide_page = GuidePage(driver)
        guide_page.check_header_title("guide")
