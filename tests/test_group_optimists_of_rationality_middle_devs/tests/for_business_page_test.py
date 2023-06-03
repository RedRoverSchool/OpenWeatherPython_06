from pages.base_page import BasePage
from tests.test_group_optimists_of_rationality_middle_devs.locators.for_business_page_locators import ForBusinessPageLocators
from tests.test_group_optimists_of_rationality_middle_devs.pages.for_business_page import ForBusinessPage

class TestBusinessPage:

    def test_tc_012_01_08_01_verify_the_buttons_are_clickable(self, driver):
        business_page = ForBusinessPage(driver, ForBusinessPageLocators.FOR_BUSINESS_PAGE_URL)
        business_page.open_page()
        business_page.assert_elements_are_clickable()