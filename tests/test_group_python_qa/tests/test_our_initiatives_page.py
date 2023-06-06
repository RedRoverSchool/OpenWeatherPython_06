from tests.group_files.group_python_qa import MAIN_LOGO
from tests.test_group_python_qa.pages.our_initiatives_page_pqa import OurInitiativesPage
from tests.test_group_python_qa.links.links_all_pages import URL_OUR_INITIATIVES_PAGE


class TestOurInitiativesPage:


    def test_002_01_11_verify_main_logo(self, driver):
        our_initiatives_page = OurInitiativesPage(driver, URL_OUR_INITIATIVES_PAGE)
        our_initiatives_page.open_page()
        our_initiatives_page.find_element_and_click(MAIN_LOGO)
        our_initiatives_page.verify_main_logo()

