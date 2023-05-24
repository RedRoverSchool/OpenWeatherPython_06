
from tests.test_group_ducktales.pages.sign_in_page import SignInPage
from tests.test_group_ducktales.test_data.sign_in_page_data import *
from tests.test_group_ducktales.pages.API_keys_page import ApiKeysPage


class TestApiKey:

    def test_tc_017_04_01_module_create_api_key_is_visible(self, driver):
        sign_in_page = SignInPage(driver, LINK_SIGN_IN_PAGE)
        sign_in_page.open_page()
        sign_in_page.log_in()
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_module_create_api_key_is_visible()

    def test_tc_017_04_02_api_key_name_has_limit_20_characters(self, driver):
        sign_in_page = SignInPage(driver, LINK_SIGN_IN_PAGE)
        sign_in_page.open_page()
        sign_in_page.log_in()
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.open_popup_rename_api_key()
        api_keys_page.enter_new_api_name("New API name for test")
        api_keys_page.click_save_new_api_key_name_button()
        api_keys_page.check_limit_of_api_key_name()




