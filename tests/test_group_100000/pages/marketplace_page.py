from pages.base_page import BasePage
from tests.test_group_100000.locators.marketplace_page_locators import MarketplaceLocators as M


class MarketplacePage(BasePage):
    def select_state_field(self):
        self.element_is_clickable(M.SELECT_STATE_FIELD).click()
        self.element_is_present(M.STATE_TEXAS).click()