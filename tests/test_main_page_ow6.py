import pytest

from pages.main_page import MainPage
from locators.locators import MainPageLocators, FooterLocators, BasePageLocators, PartnersLocators
from test_data.urls import MainPageUrls, SuitsUrls
from test_data.all_links import Links
from test_data.main_page_data import *


class TestMainPage:
    URLs = SuitsUrls.URLs

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

    def test_tc_003_01_03_footer_presence_in_the_dom_tree(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_footer_is_present()

    @pytest.mark.parametrize('URL', URLs)
    def test_tc_003_02_02_verify_display_of_product_collections_module_on_pages(self, driver,
                                                                                open_and_load_main_page, URL):
        page = MainPage(driver, link=URL)
        page.check_product_collections_section_is_visible()

    def test_tc_003_03_03_historical_weather_data_link_visibility(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_historical_weather_data_link_is_visible()

    def test_tc_003_03_04_verify_weather_dashboard_link_visibility(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_weather_dashboard_link_is_visible()

    def test_tc_003_03_05_verify_weather_dashboard_link_clickability(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_weather_dashboard_link_is_clickable()

    def test_tc_003_03_07_verify_current_and_forecast_apis_link_visibility(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_current_and_forecast_apis_link_is_visible()

    def test_tc_003_03_08_verify_historical_weather_data_link_clickability(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_historical_weather_data_link_is_clickable()

    def test_tc_003_03_10_verify_weather_maps_link_visibility(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_weather_maps_link_is_visible()

    def test_tc_003_03_11_verify_widgets_link_visibility(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_widgets_link_is_visible()

    def test_tc_003_06_02_verify_terms_and_conditions_module_title_visibility(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_terms_and_conditions_module_title_visibility()

    def test_tc_003_06_03_verify_website_terms_and_conditions_link_visibility(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_website_terms_and_conditions_link_visibility()

    @pytest.mark.parametrize('URL', URLs)
    def test_tc_003_08_05_about_us_link_is_visible_on_each_page_specified_in_data(self, driver,
                                                                                  open_and_load_main_page, URL):
        page = MainPage(driver, link=URL)
        page.check_about_us_link_is_visible()

    @pytest.mark.parametrize('URL', URLs)
    def test_tc_003_08_06_verify_about_us_link_clickability(self, driver, open_and_load_main_page, URL):
        page = MainPage(driver, link=URL)
        page.check_about_us_link_is_clickable()

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

    def test_tc_003_12_20_verify_blog_link_functionality(self, driver, open_and_load_main_page, wait):
        page = MainPage(driver)
        expected_link = Links.URL_BLOG_WEATHER
        page.check_blog_link_functionality(expected_link)

    def test_tc_003_12_21_verify_openweather_for_business_link_functionality(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        expected_link = Links.URL_OPENWEATHER_FOR_BUSINESS
        page.check_openweather_for_business_link_functionality(expected_link)

    def test_TC_003_13_01_verify_cookies_management_module_is_visible(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_manage_cookies_link_is_visible()

    def test_TC_003_14_02_manage_cookies_link_functionality(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_manage_cookies_link_is_functionality()

    @pytest.mark.skip('Build failed')
    def test_TC_001_02_01_verify_temperature_switched_on_metric_system(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.checking_the_temperature_system_switching("°C")

    @pytest.mark.skip('Build failed')
    def test_TC_001_02_02_verify_temperature_switched_on_imperial_system(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.checking_the_temperature_system_switching("°F")

    def test_TC_001_02_03_verify_temperature_metric_button_displayed_clickable(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.verify_temperature_button_displayed_clickable("°C")

    def test_TC_001_02_04_verify_temperature_imperial_button_displayed_clickable(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.verify_temperature_button_displayed_clickable("°F")

    @pytest.mark.skip('Build failed')
    def test_TC_001_05_01_verify_the_current_date_and_time(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.verify_the_current_date_and_time()

    @pytest.mark.skip('Build failed')
    def test_TC_001_05_02_verify_current_location(self, driver, open_and_load_main_page, wait):
        page = MainPage(driver)
        page.verify_current_location(wait)

    @pytest.mark.skip('Build failed')
    def test_tc_001_01_01_verify_city_name_displayed_by_zip(self, driver, wait, open_and_load_main_page):
        page = MainPage(driver)
        page.check_city_name_displayed_by_zip(wait)

    def test_tc_001_01_02_main_page_search_city_dropdown_options_valid_value(self, driver):
        page = MainPage(driver, Links.URL_MAIN_PAGE)
        page.open_page()
        page.check_dropdown_options()

    def test_tc_001_02_04_01_switch_toggle_buttons(self, driver):
        page = MainPage(driver, Links.URL_MAIN_PAGE)
        page.open_page()
        page.check_buttons_displayed_and_enabled()

    def test_tc_001_04_03_verify_in_day_list_first_element_day_by_week(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_day()

    def test_tc_001_04_04_verify_in_day_list_first_element_month(self, driver, open_and_load_main_page):
        page = MainPage(driver, Links.URL_MAIN_PAGE)
        page.open_page()
        page.check_months()

    def test_tc_001_04_05_verify_in_day_list_first_element_number_day(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.verify_in_day_list_first_element_number_day()

    def test_tc_001_04_06_verify_in_day_list_days_of_the_week(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.verify_in_day_list_days_of_the_week()

    def test_tc_001_04_07_verify_day_list_elements_numbers_days(self, driver, wait, open_and_load_main_page):
        page = MainPage(driver)
        page.check_in_day_list_numbers_days(driver)

    def test_tc_003_09_01_the_module_title_display(self, driver):
        page = MainPage(driver, Links.URL_MAIN_PAGE)
        page.open_page()
        page.check_module_title_download_openweather_app()

    def test_tc_003_09_02_app_store_brand_link_display(self, driver):
        page = MainPage(driver, Links.URL_MAIN_PAGE)
        page.open_page()
        page.check_app_store_brand_link_display()

    def test_tc_003_09_03_app_store_brand_link_clickable(self, driver):
        page = MainPage(driver, Links.URL_MAIN_PAGE)
        page.open_page()
        page.check_app_store_brand_link_clickable()

    def test_tc_003_09_04_google_play_brand_link_clickable(self, driver):
        page = MainPage(driver, Links.URL_MAIN_PAGE)
        page.open_page()
        page.check_google_play_brand_link_clickable()

    def test_tc_003_09_04_google_play_brand_link_display(self, driver):
        page = MainPage(driver, Links.URL_MAIN_PAGE)
        page.open_page()
        page.check_google_play_brand_link_display()

    def test_TC_001_05_04_verify_description_weather_for_current_location(self, driver, open_and_load_main_page, wait):
        actual_weather = MainPage(driver)
        actual_weather.check_description_weather_block('Feels like')

    def test_TC_001_01_08_dropdown_list_contain_city_temperature(self, driver, open_and_load_main_page, wait):
        search_result = MainPage(driver)
        search_result.dropdown_contain_city_temperature()

    class TestFooterLinksFunctionality:
        def test_TC_003_12_04_current_and_forecast_apis_functionality(self, driver, open_and_load_main_page):
            page = MainPage(driver)
            page.check_current_and_forecast_apis_functionality()

        def test_TC_003_12_06_verify_privacy_policy_is_opened_after_click(self, driver, wait, open_and_load_main_page):
            main_page = MainPage(driver)
            main_page.verify_privacy_policy_is_opened_after_click(driver, wait)

        def test_TC_003_12_07_about_us_link_leads_to_correct_page(self, driver, open_and_load_main_page):
            page = MainPage(driver)
            page.about_us_link_leads_to_correct_page()

        def test_TC_003_12_11_link_Google_Play_leads_to_correct_page_in_GP(self, driver, open_and_load_main_page, wait):
            google_link = MainPage(driver)
            google_link.check_leads_link_Googl_Play()

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

        def test_tc_003_05_03_verify_how_to_start_link_is_clickable(self, driver, open_and_load_main_page, wait):
            page = MainPage(driver)
            page.verify_how_to_start_link_is_clickable()

        def test_tc_002_03_10_01_how_to_start_link_leads_to_correct_page(self, driver, open_and_load_main_page, wait):
            main_page = MainPage(driver)
            main_page.check_how_to_start_link_opens_opens_correct_page(wait, Links.HOW_TO_START_URL)
            main_page.check_correct_header_is_displayed("How to start using professional collections")

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
            main_page.click_support_link()
            main_page.faq_submenu_should_be_visible(wait=wait)

        def test_tc_002_03_09_01_faq_link_leads_to_correct_page(self, driver, open_and_load_main_page, wait):
            main_page = MainPage(driver)
            main_page.check_faq_link_opens_opens_correct_page(wait, Links.FAQ_URL)
            main_page.check_correct_header_is_displayed("Frequently Asked Questions")

        def test_TC_002_03_22_partners_link_is_visible_and_clickable(self, driver, open_and_load_main_page):
            page = MainPage(driver)
            page.link_visible_and_clickable(BasePageLocators.PARTNERS_LINK)

        def test_TC_002_03_21_partners_link_leads_to_page_with_correct_header(self, driver, open_and_load_main_page):
            page = MainPage(driver)
            page.link_leads_to_page_with_correct_header(BasePageLocators.PARTNERS_LINK,
                                                        PartnersLocators.PARTNERS_PAGE_HEADING)

        def test_TC_002_03_07_marketplace_link_redirects_to_valid_page(self, driver, open_and_load_main_page):
            main_page = MainPage(driver)
            main_page.verify_marketplace_link_redirects_to_valid_page()

        @pytest.mark.parametrize('page', data["pages"])
        def test_TC_002_01_03_Logo_is_visible(self, driver, page):
            main_page = MainPage(driver, f'{Links.URL_MAIN_PAGE}{page}')
            main_page.open_page()
            main_page.check_logo_is_visible()

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

        @pytest.mark.parametrize('page', data["pages"])
        def test_TC_003_01_01_verify_footer_is_visible_from_all_pages_specified_in_data(self, driver, page):
            footer = MainPage(driver, f'{Links.URL_MAIN_PAGE}{page}')
            footer.open_page()
            footer_actual_result = footer.find_element(FooterLocators.FOOTER_WEBSITE)
            footer.go_to_element(footer_actual_result)
            footer.check_footer_website_is_displayed(footer_actual_result)

        @pytest.mark.parametrize('page', data["pages"])
        def test_TC_003_01_02_verify_copyright_is_visible_from_all_pages_specified_in_data(self, driver, page):
            footer = MainPage(driver, f'{Links.URL_MAIN_PAGE}{page}')
            footer.open_page()
            copyright_actual_result = footer.find_element(FooterLocators.FOOTER_COPYRIGHT)
            footer.go_to_element(copyright_actual_result)
            footer.check_copyright_is_displayed(copyright_actual_result)

        def test_TC_003_08_02_ask_a_question_link_is_visible(self, driver, open_and_load_main_page):
            page = MainPage(driver)
            page.element_is_visible(MainPageLocators.ASK_A_QUESTION_LINK)

        def test_TC_003_08_03_ask_a_question_link_is_clickable(self, driver, open_and_load_main_page):
            page = MainPage(driver)
            page.element_is_clickable(MainPageLocators.ASK_A_QUESTION_LINK)

        def test_TC_003_12_05_ask_a_question_link_leads_to_correct_page(self, driver, open_and_load_main_page):
            page = MainPage(driver)
            page.scroll_down_the_page()
            page.check_link_in_new_window(MainPageLocators.ASK_A_QUESTION_LINK, MainPageUrls.ASK_A_QUESTION_PAGE)

        @pytest.mark.parametrize('page', data["pages"])
        def test_TC_003_03_01_Product_Collections_title_is_visible(self, driver, page):
            footer = MainPage(driver, f'{Links.URL_MAIN_PAGE}{page}')
            footer.open_page()
            footer.check_product_collections_module_title_is_visible()

    class TestMainPageHourlyForecast:
        def test_tc_001_08_04_verify_chart_is_present(self, driver, open_and_load_main_page, wait):
            page = MainPage(driver)
            page.verify_chart_weather_is_present()

    def test_tc_001_017_01_visibility_of_nwp_block(self, driver):
        page = MainPage(driver, MainPageUrls.QUALITY_INFO_PAGE)
        page.open_page()
        page.element_is_visible(MainPageLocators.NWP_MODEL)

    class TestMainPageGraphicAndWeather:
        def test_tc_001_08_01_graphic_hourly_forecast_is_displayed(self, driver, open_and_load_main_page, wait):
            page = MainPage(driver)
            page.graphic_hourly_forecast_is_displayed(wait=wait)

        def test_tc_001_08_02_weather_items_are_displayed(self, driver, open_and_load_main_page, wait):
            page = MainPage(driver)
            page.weather_items_are_displayed(wait=wait)
