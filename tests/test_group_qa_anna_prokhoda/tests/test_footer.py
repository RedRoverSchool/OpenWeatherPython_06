from tests.test_group_qa_anna_prokhoda.pages.footer import Footer
from tests.test_group_qa_anna_prokhoda.links.links import main_page_url
from tests.test_group_qa_anna_prokhoda.locators.footer_locators import FooterLocators as FL


class TestFooter:
    def test_TC_003_06_01_privacy_policy_link_is_visible(self, driver, open_and_load_main_page, wait):
        page = Footer(driver)
        page.element_visibility(FL.privacy_policy_link)

    def test_TC_003_06_01_privacy_policy_link_is_clickable(self, driver, open_and_load_main_page, wait):
        page = Footer(driver)
        page.element_clickability(FL.privacy_policy_link)
