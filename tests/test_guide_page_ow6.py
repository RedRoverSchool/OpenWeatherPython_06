from pages.guide_page import GuidePage

class TestGuidePage:

    def test_TC_004_06_03_verify_redirection_industry_standard_apis_link(self, driver, wait):
        page = GuidePage(driver, GuidePage.link)
        page.open_page()
        page.industry_standard_apis_link_redirection()

    def test_TC_004_06_04_verify_redirection_one_call_api_by_call_link(self, driver, wait):
        page = GuidePage(driver, GuidePage.link)
        page.open_page()
        page.one_call_api_by_call_link_redirection()

    def test_TC_004_06_07_verify_button_subscribe_to_onecall_by_call_is_visible(self, driver, wait):
        page = GuidePage(driver, GuidePage.link)
        page.open_page()
        page.subscribe_to_onecall_by_call_button_is_visible()