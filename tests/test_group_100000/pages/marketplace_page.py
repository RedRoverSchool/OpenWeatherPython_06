from pages.base_page import BasePage
from tests.test_group_100000.locators.marketplace_page_locators import MarketplaceLocators as M
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


    M = M()

    def click_marketplace_search_field(self):
        marketplace_search_field = self.driver.find_element(*self.M.SEARCH_FLD)
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(marketplace_search_field)
        self.driver.execute_script("arguments[0].click();", marketplace_search_field)
        return marketplace_search_field

    def select_by_location_method(self):
        by_location_button = self.driver.find_element(*self.M.BY_LOCATION_BTN)
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(by_location_button)
        self.driver.execute_script("arguments[0].click();", by_location_button)
        return by_location_button

    def fill_marketplace_search_field(self):
        input_city_name = self.driver.find_element(*self.M.SEARCH_FLD)
        input_city_name.click()
        input_city_name.send_keys(*self.M.REQUESTED_CITY)

    def select_city_from_dropdown_list(self, wait):
        wait.until(EC.visibility_of_element_located(self.M.CITY_NAME_FROM_DROPDOWN_MENU))
        city_name_from_dropdown_list = self.element_is_clickable(self.M.CITY_NAME_FROM_DROPDOWN_MENU)
        city_name_from_dropdown_list.click()
        return city_name_from_dropdown_list

    def find_displayed_text(self, wait):
        displayed_text = wait.until(EC.visibility_of_element_located(self.M.CITY_NAME_ON_MAP)).text
        return displayed_text

