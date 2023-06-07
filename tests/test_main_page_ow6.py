import pytest

from pages.main_page import MainPage
from locators.locators import MainPageLocators
from test_data.urls import MainPageUrls


class TestMainPage:

    def test_example_search_city(self, driver, open_and_load_main_page):
        main_page = MainPage(driver)
        main_page.search_city('Almaty')

    def test_tc_001_04_01_visibility_of_8_lines_in_8_day_forecast_block(self, driver, open_and_load_main_page, wait):
        main_page = MainPage(driver)
        main_page.search_city("Paris")
        main_page.choose_1st_option(wait)
        main_page.switch_to_c_temp()
        main_page.check_8_lines_are_displayed()

    def test_tc_021_01_01_visibility_of_agriculture_analytics_link(self, driver, open_and_load_main_page, wait):
        main_page = MainPage(driver)
        main_page.element_is_displayed(MainPageLocators.AGRICULTURE_ANALYTICS_TITLE_LOCATOR, wait)

    def test_tc_003_03_03_historical_weather_data_link_visibility(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_historical_weather_data_link_is_visible()

    def test_tc_003_03_04_verify_weather_dashboard_link_visibility(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_weather_dashboard_link_is_visible()

    def test_tc_003_03_05_verify_weather_dashboard_link_clickability(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_weather_dashboard_link_is_clickable()

    def test_tc_003_06_03_verify_website_terms_and_conditions_link_visibility(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_website_terms_and_conditions_link_visibility()

    def test_tc_003_12_01_check_historical_weather_data_link_functionality(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_historical_weather_data_link_functionality()

    def test_tc_003_12_02_verify_weather_data_link_functionality(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_weather_dashboard_link_functionality()

    def test_tc_003_12_03_verify_weather_maps_link_functionality(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_weather_maps_link_functionality()

    def test_tc_003_12_08_verify_our_technology_link_functionality(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_our_technology_link_functionality()

    def test_tc_003_12_16_verify_accuracy_and_quality_of_weather_data_link_functionality \
                    (self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_accuracy_and_quality_of_weather_data_link_functionality()

    def test_tc_003_12_17_verify_connect_your_weather_station_link_functionality(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_connect_your_weather_station_link_functionality()

    def test_tc_003_12_18_verify_how_to_start_link_functionality(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_how_to_start_link_functionality()

    def test_tc_003_12_19_verify_subscribe_for_free_link_functionality_for_unauthorized_user \
                    (self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_subscribe_for_free_link_functionality()

    def test_tc_003_12_21_verify_openweather_for_business_link_functionality(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        expected_link = "https://openweather.co.uk/"
        page.check_openweather_for_business_link_functionality(expected_link)

    class TestFooterLinksFunctionality:
        def test_TC_003_12_04_current_and_forecast_apis_functionality(self, driver, open_and_load_main_page):
            page = MainPage(driver)
            page.check_current_and_forecast_apis_functionality()

        def test_TC_003_12_06_verify_privacy_policy_is_opened_after_click(self, driver, wait, open_and_load_main_page):
            main_page = MainPage(driver)
            main_page.verify_privacy_policy_is_opened_after_click(driver, wait)

    class TestFooterLinksclickability:
        def test_TC_003_03_02_verify_clickability_current_and_forecast_apis(self, driver, open_and_load_main_page):
            page = MainPage(driver)
            page.verify_clickability_current_and_forecast_apis()

        def test_tc_003_03_06_verify_widgets_clickability(self, driver, open_and_load_main_page, wait):
            page = MainPage(driver)
            page.verify_widgets_clickability()

    class TestHowToStartLink:
        def test_tc_003_05_02_verify_how_to_start_visibility(self, driver, open_and_load_main_page, wait):
            page = MainPage(driver)
            page.verify_how_to_start_visibility()

    class TestHeaderPage:
        def test_tc_002_02_07_placeholder_is_displayed_in_search_field(self, driver, open_and_load_main_page):
            main_page = MainPage(driver)
            main_page.check_placeholder_text_is_visible("Weather in your city")

        def test_tc_002_02_09_placeholder_disappears_if_symbol_is_typed_in_search_field(
                self, driver, open_and_load_main_page, wait):
            main_page = MainPage(driver)
            main_page.check_placeholder_disappears("a", "value")

        def test_tc_002_03_23_faq_link_is_visible_and_clickable(self, driver, open_and_load_main_page, wait):
            main_page = MainPage(driver)
            main_page.click_support_nav_menu()
            main_page.faq_submenu_should_be_visible(wait=wait)

    class TestMainPageFooter:
        link_product_collections = MainPageUrls.PRODUCT_COLLECTION_LINKS

        def test_tc_003_12_12_widgets_link_functionality(self, driver, open_and_load_main_page, wait):
            page = MainPage(driver)
            expected_link = "https://openweathermap.org/widgets-constructor"
            page.click_footer_product_collections_widgets(expected_link)

        @pytest.mark.parametrize("link_product_collection", link_product_collections)
        def test_tc_003_12_24_verify_product_collections_module_all_link_functionality(self, driver,
                                                                                       open_and_load_main_page, wait,
                                                                                       link_product_collection):
            page = MainPage(driver)
            expected_link = link_product_collection
            link_number = self.link_product_collections.index(expected_link)
            page.click_footer_product_collections_all_widgets(expected_link, link_number)

    class TestMainPageHourlyForecast:
        def test_tc_001_08_04_verify_chart_is_present(self, driver, open_and_load_main_page, wait):
            page = MainPage(driver)
            page.verify_chart_weather_is_present()

    def test_tc_003_11_01_verify_the_copyright_information_is_present_on_the_page(self, driver,
                                                                                  open_and_load_main_page):
        page = MainPage(driver)
        page.verify_the_copyright_information_is_present_on_the_page()
