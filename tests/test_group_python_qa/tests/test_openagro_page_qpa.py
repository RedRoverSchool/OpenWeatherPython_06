from tests.test_group_python_qa.links.links_all_pages import OPENAGRO_PAGE
from tests.test_group_python_qa.pages.openagro_page_pqa import OpeAgroPage


class TestOpenAgro:

    def test_tc_021_01_05_request_data_button_display_check(self, driver):
        openagro_page = OpeAgroPage(driver, OPENAGRO_PAGE)
        openagro_page.open_page()
        openagro_page.there_is_more_than_one_element_displayed_check(driver)


