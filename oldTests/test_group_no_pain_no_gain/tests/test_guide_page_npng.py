from oldTests.test_group_no_pain_no_gain.pages.guide_page import GuidePage
from oldTests.test_group_no_pain_no_gain import links


class TestGuidePage:

    def test_TC_002_01_01_return_from_guide_page_to_main_page_by_clicking_on_logo(self, driver):
        guide_page = GuidePage(driver, links.GUIDE_PAGE)
        guide_page.open_page()
        guide_page.check_logo()
