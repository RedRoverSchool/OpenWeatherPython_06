from tests.test_group_qa_anna_prokhoda.pages.footer import Footer
from pages.base_page import BasePage


class TestPrivacyPolicyLink:

    def test_tc_003_06_01_verify_privacy_policy_link_is_clickable(self, driver, open_and_load_main_page):
        page = Footer(driver)
        page.check_privacy_policy_link_is_clickable()
