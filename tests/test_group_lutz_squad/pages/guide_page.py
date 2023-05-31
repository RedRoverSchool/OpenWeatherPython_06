from pages.base_page import BasePage
from tests.test_group_lutz_squad.locators.guide_page_locators import GuidePageLocators


class GuidePage(BasePage):

    def industry_apis_link_is_visible_and_clickable(self):
        self.element_is_visible(GuidePageLocators.INDUSTRY_APIS_LOCATOR)
        assert self.element_is_clickable(GuidePageLocators.INDUSTRY_APIS_LOCATOR)
