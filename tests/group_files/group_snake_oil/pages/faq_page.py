from pages.base_page import BasePage
from tests.group_files.group_snake_oil.locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from tests.group_files.group_snake_oil.links.all_links import FAQ_URL


class FAQPage(BasePage):
    locators = MainPageLocators

    def open_Support_dropdown(self):
        wait(self.driver, timeout=10).until(EC.invisibility_of_element_located(self.locators.OVERLAY_LOCATOR))
        dropdown = wait(self.driver, timeout=10).until(EC.element_to_be_clickable(self.locators.SUPPORT_DROPDOWN))
        dropdown.click()

    def check_redirection_of_FAQ_element(self):
        element = wait(self.driver, timeout=10).until(EC.visibility_of_element_located(self.locators.FAQ_ELEMENT))
        element.click()
        current_url = self.driver.current_url
        wait(self.driver, timeout=10).until(EC.url_to_be(FAQ_URL))
        assert current_url == FAQ_URL, f"Redirection is failed. Expected: {FAQ_URL}, Actual: {self.driver.current_url}"
