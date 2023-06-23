from pages.base_page import BasePage
from locators.locators import ApiPageLocators as APL
from test_data.all_links import Links
from test_data.urls import ApiPageUrls

class APIPage(BasePage):

    def click_button_api_doc_history_full_archive(self):
        btn_history_api = self.driver.find_element(*APL.button_history_api_full_archive)
        self.action_move_to_element(btn_history_api)
        self.driver.execute_script("arguments[0].click();", btn_history_api)

    def check_title_history_api_full_archive(self):
        actual_title_history_full = self.driver.find_element(*APL.DISPLAYED_TITLE).text
        expected_title_history_full_archive = "History API Full archive"
        assert actual_title_history_full == expected_title_history_full_archive

    def click_button_api_doc_in_global_weather_alerts(self):
        btn_api = self.driver.find_element(*APL.button_weather_alerts_api_doc)
        self.action_move_to_element(btn_api)
        self.driver.execute_script("arguments[0].click();", btn_api)

    def check_title_features_global_weather_alert(self):
        actual_title_features = self.driver.find_element(*APL.actual_title_features).text
        expected_title_features = "Features of Global Weather Alerts"
        assert expected_title_features == actual_title_features

    def verify_redirection_one_call_api_3_link(self):
        self.driver.get(APL.API_PAGE)
        self.driver.find_element(*APL.ONE_CALL_API_3).click()
        expected_link = APL.ONE_CALL_API_LINK
        assert self.driver.current_url == expected_link, "This link is not correct"


    def verify_present_api_calls_and_responses(self):
        counter = 0
        for api_block in APL.history_api_full_archive_calls_and_response:
            counter += 1
            block = self.driver.find_element(*api_block)
            assert block.is_displayed(), f"Block {counter} is missing"


    def verify_visibility_button_get_access(self):
        btn_get_access = self.driver.find_element(*APL.button_get_access)
        self.driver.find_element(*APL.button_get_access)
        assert btn_get_access.is_displayed()

    def check_logo(self):
        self.driver.find_element(*APL.API_LOGO).click()
        assert self.driver.current_url == Links.URL_MAIN_PAGE

    def verify_get_access_redirects_to_valid_page(self):
        self.driver.execute_script("window.scrollTo(0, 500)")
        self.driver.find_element(*APL.button_get_access).click()
        expected_link = ApiPageUrls.GET_ACCESS_API_LINK
        actual_link = self.driver.current_url
        print(f"This link is not correct, expected link should be {expected_link}")
        assert actual_link != expected_link
