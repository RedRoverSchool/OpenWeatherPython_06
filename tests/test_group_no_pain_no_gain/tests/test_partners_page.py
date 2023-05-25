from tests.test_group_no_pain_no_gain.pages.partners_page import Partners
from tests.test_group_no_pain_no_gain import links
from tests.test_group_no_pain_no_gain.test_data.partners_page_data import PartnersPageData as PPD

class TestPartnersPage:
    def test_TC_011_01_01_verify_that_Partners_and_solutions_page_title_is_correct(self, driver):
        page = Partners(driver)
        page.check_page_title(links.PARTNERS_AND_SOLUTIONS, PPD.PARTNERS_PAGE_TITLE)
