from pages.base_page import BasePage
from locators.locators import MarketplaceLocators as M
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class MarketplacePage(BasePage):
    def select_state_field(self):
        self.element_is_clickable(M.SELECT_STATE_FIELD).click()

    def select_element_from_dropdown_list(self, locator):
        self.element_is_present(locator).click()

    def select_year_field(self):
        self.element_is_clickable(M.SELECT_YEAR_FIELD).click()

    def find_price_in_dropdown_menu(self, locator):
        submenu = self.element_is_present(locator)
        s = (submenu.text)
        price = s.split(' (')[0]
        return price

    def find_total_amount(self, locator):
        t = self.element_is_present(locator)
        total = t.text
        amount = total.split()[1]
        return f'${amount}'
