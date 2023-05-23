from pages.base_page import BasePage
from tests.test_group_future_auto_qa.locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    locators = MainPageLocators()

    def get_header_search_field_attribute(self, attribute):
        search_placeholder = self.driver.find_element(*self.locators.HEADER_SEARCH_FIELD)
        return search_placeholder.get_attribute(attribute)

    def fill_city_search_field(self, city):
        input_city = self.driver.find_element(*self.locators.HEADER_SEARCH_FIELD)
        input_city.send_keys(city)

    def click_header_search_field(self):
        self.driver.find_element(*self.locators.HEADER_SEARCH_FIELD).click()


    def click_support_nav_menu(self):
        return self.driver.find_element(*self.locators.SUPPORT_MENU).click()

    def click_faq_submenu(self, wait):
        submenu = wait.until(EC.visibility_of_element_located(self.locators.SUPPORT_FAQ_SUBMENU)).click()
        actions = ActionChains(self.driver)
        actions.click(submenu).perform()
        return submenu

    def faq_submenu_should_be_visible(self, wait):
        element = wait.until(EC.visibility_of_element_located(self.locators.SUPPORT_FAQ_SUBMENU))
        assert element.is_displayed() and element.is_enabled(), f'"{element}" link is not visible or clickable'

    def assert_current_url(self, expected_url):
        current_url = self.driver.current_url
        assert current_url == expected_url, f"URL does not match. Actual: {current_url}"

    def correct_header_is_displayed(self, text):
        element_text = self.driver.find_element(*self.locators.HEADER).text
        assert element_text == text, f'"{text}" is not present.'

    def click_footer_product_collections_widgets(self, expected_link):
        self.allow_all_cookies()
        widgets_link = self.element_is_clickable(self.locators.FOOTER_WIDGETS)
        link_href = widgets_link.get_attribute('href')
        assert link_href == expected_link, "Incorrect link"
