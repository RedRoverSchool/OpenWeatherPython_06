from oldTests.test_group_roma.pages.api_page import ApiPage
from oldTests.test_group_roma import links



class TestApiPage:

      def test_TC_002_01_02_verify_returning_from_API_page_to_main_page_by_clicking_on_logo(self, driver):
          api_page = ApiPage(driver, links.API_PAGE)
          api_page.open_page()
          api_page.check_logo()