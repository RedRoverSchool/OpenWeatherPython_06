from tests.test_group_python_qa.pages.partners_page_pqa import PartnersAndSolutionsPage
from tests.test_group_python_qa.links.links_all_pages import *


class TestPartnersAndSolutionsPage:

    def test_tc_011_09_01_link_see_library_visibility(self, driver, wait):
        partners_page = PartnersAndSolutionsPage(driver, PARTNERS_AND_SOLUTION_PAGE_URL)
        partners_page.link_see_library_visibility(wait)
