from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class Footer(BasePage):

    title_locator = (By.XPATH, '//p[text()="Product Collections"]')

    def check_product_collections_module_title_is_visible(self):
        title = self.driver.find_element(*self.title_locator)
        assert title.is_displayed(), "Title is not visible"