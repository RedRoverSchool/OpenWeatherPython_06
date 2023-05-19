from pages.base_page import BasePage
from tests.test_group_100000.locators.api_page_locators import RoadRiskApi as R


class RoadRiskApi(BasePage):
    def check_redirect_to_page_section(self):
        self.driver.find_element(*R.LINK_HOW_TO_REQUEST_RR_API).click()
        section_title = self.driver.find_element(*R.TITLE_HOW_TO_RR_API)
        assert section_title.is_displayed(), 'Title Not Found'


