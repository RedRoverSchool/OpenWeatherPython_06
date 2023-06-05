from pages.main_page import MainPage



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

    class TestHeaderPage:
        def test_tc_002_02_07_placeholder_is_displayed_in_search_field(self, driver, open_and_load_main_page, wait):
            main_page = MainPage(driver)
            search_placeholder_text = main_page.get_header_search_field_attribute("placeholder")
            assert search_placeholder_text == "Weather in your city", \
                "Password field placeholder text is incorrect or missing"
