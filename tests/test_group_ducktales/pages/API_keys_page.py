from pages.base_page import BasePage
from ..locators.API_keys_locators import ApiKeysLocator


class ApiKeysPage(BasePage):
    pass

    def open_api_keys_page(self):
        api_key_tab = self.driver.find_element(*ApiKeysLocator.TAB_API_KEYS)
        api_key_tab.click()

    def check_module_create_api_key_is_visible(self):
        module_create_api_key = self.driver.find_element(*ApiKeysLocator.MODULE_API_KEY_CREATE)
        assert module_create_api_key.is_displayed(), "module with title “Create key“ does not visible"
