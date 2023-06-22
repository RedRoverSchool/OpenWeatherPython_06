import random
import string

from pages.api_keys_page import ApiKeysPage


class TestApiKey:

    def test_tc_017_04_01_module_create_api_key_is_visible(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_module_create_api_key_is_visible()

    def test_tc_017_04_02_api_key_name_has_limit_20_characters(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_limit_of_created_api_key_name()

    def test_tc_017_04_03_api_key_name_is_required(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_create_api_key_field_is_required()

    def test_tc_017_04_04_api_key_generate_button_is_clickable(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_is_generate_button_clickable()

    def test_tc_017_04_05_api_key_is_generated(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.enter_created_api_key_name("Generate name")
        initial_api_keys_table_length = api_keys_page.get_length_of_table_api_keys()
        api_keys_page.click_generate_api_key_name_button()
        api_keys_page.check_is_api_key_generated(initial_api_keys_table_length)
        api_keys_page.delete_api_key("Generate name")

    def test_tc_017_05_01_verify_visability_clickability_icon_for_deleting_selected_API_key(self, driver):
        api_key_name = ''.join(random.choices(string.ascii_letters, k=8))
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.enter_created_api_key_name(api_key_name)
        api_keys_page.click_generate_api_key_name_button()
        api_keys_page.verify_visability_clickability_icon_for_deleting(api_key_name)
        api_keys_page.delete_api_key(api_key_name)

    def test_tc_017_05_02_verify_modal_window_opening_with_confirmation_API_key_deletion(self, driver):
        api_key_name = ''.join(random.choices(string.ascii_letters, k=8))
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.enter_created_api_key_name(api_key_name)
        api_keys_page.click_generate_api_key_name_button()
        api_keys_page.verify_modal_window_opening_with_confirmation_API_key_deletion(api_key_name)
        api_keys_page.delete_api_key(api_key_name)

    def test_tc_017_05_03_verify_notice_message_about_API_key_deletion(self, driver):
        api_key_name = ''.join(random.choices(string.ascii_letters, k=8))
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.enter_created_api_key_name(api_key_name)
        api_keys_page.click_generate_api_key_name_button()
        api_keys_page.verify_notice_message_about_API_key_deletion(api_key_name)

    def test_tc_017_05_04_verify_that_selected_api_key_was_deleted(self, driver):
        api_key_name = ''.join(random.choices(string.ascii_letters, k=8))
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.enter_created_api_key_name(api_key_name)
        api_keys_page.click_generate_api_key_name_button()
        api_keys_page.delete_api_key(api_key_name)
        api_keys_page.verify_that_selected_api_key_was_deleted(api_key_name)