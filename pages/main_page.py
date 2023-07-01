from pages.base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPageLocators, BasePageLocators
from test_data.all_links import Links
from datetime import datetime, date
from zoneinfo import ZoneInfo
from test_data.main_page_data import *


class MainPage(BasePage):
    locators = MainPageLocators()

    def fill_city_search_field(self, city):
        input_city = self.driver.find_element(*self.locators.SEARCH_CITY_FIELD)
        input_city.send_keys(city)

    def search_city(self, city):
        self.fill_city_search_field(city)
        self.driver.find_element(*self.locators.SEARCH_BUTTON).click()

    def check_seach_city_result(self, wait, city):
        self.click_search_button(city)
        expected_city = city
        expected_error_message = f'No results for {city}'
        if self.element_is_displayed(self.locators.NO_RESULTS_NOTIFICATION, wait):
            actual_error_message = wait.until(EC.visibility_of_element_located(self.locators.NO_RESULTS_NOTIFICATION))
            actual_error_message_text = actual_error_message.text
            assert actual_error_message_text == expected_error_message
        else:
            wait.until(EC.element_to_be_clickable(self.locators.SEARCH_DROPDOWN_OPTION)).click()
            wait.until(EC.text_to_be_present_in_element(self.locators.DISPLAYED_CITY, city))
            actual_city = self.driver.find_element(*self.locators.DISPLAYED_CITY).text
            assert expected_city in actual_city

    def go_to_about_us_page_from_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.allow_all_cookies()
        main_page.element_is_clickable(self.locators.ABOUT_US_BUTTON).click()

    def choose_1st_option(self, wait):
        wait.until(EC.element_to_be_clickable(self.locators.SEARCH_DROPDOWN_OPTION)).click()

    def switch_to_c_temp(self):
        self.driver.find_element(*self.locators.C_TEMP_LOCATOR).click()

    def check_8_lines_are_displayed(self):
        lines = self.driver.find_elements(*self.locators.LINE_IN_8_DAYS_FORECAST_LOCATOR)
        for line in lines:
            assert line.is_displayed()

    def check_footer_is_present(self):
        footer_common_kit = self.element_is_present(self.locators.FOOTER_COMMON_KIT)
        assert footer_common_kit is not None, "Footer is not present in the DOM tree"

    def check_product_collections_section_is_visible(self):
        product_collections_section = self.element_is_visible(self.locators.PRODUCT_COLLECTIONS_SECTION)
        assert product_collections_section, "The Product Collections Section is not visible"

    def check_subscription_section_is_visible(self):
        subscription_section = self.element_is_visible(self.locators.SUBSCRIPTION_SECTION)
        assert subscription_section, "The Subscription Section is not visible"

    def check_company_section_is_visible(self):
        company_section = self.element_is_visible(self.locators.COMPANY_SECTION)
        assert company_section, "The Company Section is not visible"

    def check_technologies_section_is_visible(self):
        technologies_section = self.element_is_visible(self.locators.TECHNOLOGIES_SECTION)
        assert technologies_section, "The Technologies Section is not visible"

    def check_terms_and_conditions_section_is_visible(self):
        terms_and_conditions_section = self.element_is_visible(self.locators.TERMS_AND_CONDITIONS_SECTION)
        assert terms_and_conditions_section, "The Terms & Conditions Section is not visible"

    def check_single_links_section_is_visible(self):
        single_links_section = self.element_is_visible(self.locators.SINGLE_LINKS_SECTION)
        assert single_links_section, "The single links section is not visible"

    def check_historical_weather_data_link_is_visible(self):
        historical_weather_data_link = self.element_is_visible(self.locators.HISTORICAL_WEATHER_DATA_LINK)
        assert historical_weather_data_link, "The Historical Weather Data link is not visible"

    def check_historical_weather_data_link_is_clickable(self):
        self.driver.find_element(*self.locators.COOKIES).click()
        historical_weather_data_link = self.driver.find_element(*self.locators.HISTORICAL_WEATHER_DATA_LINK)
        assert historical_weather_data_link.is_enabled(), "The Historical Weather Data link is not clickable"

    def check_historical_weather_data_link_functionality(self):
        historical_weather_data_link = self.driver.find_element(*self.locators.HISTORICAL_WEATHER_DATA_LINK)
        self.go_to_element(historical_weather_data_link)
        historical_weather_data_link.click()
        assert '/api#history' in self.driver.current_url, \
            "The Historical Weather Data link leads to an incorrect page"

    def check_weather_dashboard_link_is_visible(self):
        weather_dashboard_link = self.element_is_visible(self.locators.WEATHER_DASHBOARD_LINK)
        assert weather_dashboard_link, "The Weather Dashboard link is not visible"

    def check_current_and_forecast_apis_link_is_visible(self):
        current_and_forecast_apis_link = self.element_is_visible(self.locators.CURRENT_AND_FORECAST_APIS_LINK)
        assert current_and_forecast_apis_link, "The Current and Forecast APIs link is not visible"

    def check_weather_dashboard_link_is_clickable(self):
        self.driver.find_element(*self.locators.COOKIES).click()
        weather_dashboard_link = self.driver.find_element(*self.locators.WEATHER_DASHBOARD_LINK)
        assert weather_dashboard_link.is_enabled(), "The Weather dashboard link is not clickable"

    def check_weather_dashboard_link_functionality(self):
        weather_dashboard_link = self.driver.find_element(*self.locators.WEATHER_DASHBOARD_LINK)
        self.go_to_element(weather_dashboard_link)
        weather_dashboard_link.click()
        assert '/weather-dashboard' in self.driver.current_url, \
            "The Weather Dashboard link leads to an incorrect page"

    def check_weather_maps_link_is_visible(self):
        weather_maps_link = self.element_is_visible(self.locators.WEATHER_MAPS_LINK)
        assert weather_maps_link, "The Weather Maps link is not visible"

    def check_weather_maps_link_functionality(self):
        weather_maps_link = self.driver.find_element(*self.locators.WEATHER_MAPS_LINK)
        self.go_to_element(weather_maps_link)
        weather_maps_link.click()
        assert '/api#maps' in self.driver.current_url, \
            "The Weather Maps link leads to an incorrect page"

    def check_widgets_link_is_visible(self):
        widgets_link = self.element_is_visible(self.locators.WIDGETS_LINK)
        assert widgets_link, "The Widgets link is not visible"

    def check_our_technology_link_functionality(self):
        our_technology_link = self.driver.find_element(*self.locators.OUR_TECHNOLOGY_LINK)
        self.go_to_element(our_technology_link)
        our_technology_link.click()
        assert '/technology' in self.driver.current_url, \
            "The Our technology link leads to an incorrect page"

    def check_accuracy_and_quality_of_weather_data_link_functionality(self):
        accuracy_and_quality_of_weather_data_link = \
            self.driver.find_element(*self.locators.ACCURACY_AND_QUALITY_OF_WEATHER_DATA_LINK)
        self.go_to_element(accuracy_and_quality_of_weather_data_link)
        accuracy_and_quality_of_weather_data_link.click()
        assert '/accuracy-and-quality' in self.driver.current_url, \
            "The Accuracy and quality of weather data link leads to an incorrect page"

    def check_connect_your_weather_station_link_functionality(self):
        connect_your_weather_station_link = self.driver.find_element(*self.locators.CONNECT_YOUR_WEATHER_STATION_LINK)
        self.go_to_element(connect_your_weather_station_link)
        connect_your_weather_station_link.click()
        assert '/stations' in self.driver.current_url, \
            "The Connect your weather station link leads to an incorrect page"

    def check_how_to_start_link_functionality(self):
        how_to_start_link = self.driver.find_element(*self.locators.HOW_TO_START_LINK)
        self.go_to_element(how_to_start_link)
        how_to_start_link.click()
        assert '/appid' in self.driver.current_url, \
            "The How to start link leads to an incorrect page"

    def check_subscribe_for_free_link_functionality(self):
        subscribe_for_free_link = self.driver.find_element(*self.locators.SUBSCRIBE_FOR_FREE_LINK)
        self.go_to_element(subscribe_for_free_link)
        subscribe_for_free_link.click()
        assert '/users/sign_up' in self.driver.current_url, \
            "The Subscribe for free link leads to an incorrect page"

    def check_openweather_for_business_link_functionality(self, expected_link):
        self.allow_all_cookies()
        blog_link = self.element_is_clickable(self.locators.OPENWEATHER_FOR_BUSINESS_LINK)
        link_href = blog_link.get_attribute('href')
        assert link_href == expected_link, "Incorrect link"

    def check_terms_and_conditions_module_title_visibility(self):
        terms_and_conditions_module_title = \
            self.driver.find_element(*self.locators.TERMS_AND_CONDITIONS_TITLE)
        assert terms_and_conditions_module_title.is_displayed(), \
            "The Terms & Conditions module title is not visible"

    def check_website_terms_and_conditions_link_visibility(self):
        website_terms_and_conditions_link = self.driver.find_element(*self.locators.WEBSITE_TERMS_AND_CONDITIONS_LINK)
        assert website_terms_and_conditions_link.is_displayed(), "The Website terms and conditions link is not visible"

    def check_about_us_link_is_visible(self):
        about_us_link = self.driver.find_element(*self.locators.ABOUT_US_LINK)
        assert about_us_link.is_displayed(), "The About us link is not visible"

    def check_about_us_link_is_clickable(self):
        about_us_link = self.driver.find_element(*self.locators.ABOUT_US_LINK)
        assert about_us_link.is_enabled(), "The About us link is not clickable"

    def check_blog_link_functionality(self, expected_link):
        self.allow_all_cookies()
        blog_link = self.element_is_clickable(self.locators.BLOG_LINK)
        link_href = blog_link.get_attribute('href')
        assert link_href == expected_link, "Incorrect link"

    def check_product_collections_module_is_visible(self):
        product_collections_module = self.driver.find_element(*self.locators.PRODUCT_COLLECTIONS)
        assert product_collections_module.is_displayed(), \
            "The footer is not displayed or does not contain the expected text"

    def get_header_search_field_attribute(self, attribute):
        '''To retrieve the value of a specific attribute from Header Search field'''
        search_placeholder = self.driver.find_element(*self.locators.HEADER_SEARCH_FIELD)
        return search_placeholder.get_attribute(attribute)

    def check_placeholder_text_is_visible(self, expected_value):
        '''To retrieve the value of a specific attribute from Header Search field'''
        search_placeholder_text = self.get_header_search_field_attribute("placeholder")
        assert search_placeholder_text == expected_value, \
            "Password field placeholder text is incorrect or missing"

    def click_header_search_field(self):
        self.driver.find_element(*self.locators.HEADER_SEARCH_FIELD).click()

    def check_placeholder_disappears(self, symbol, attribute):
        search_placeholder_text = self.get_header_search_field_attribute("placeholder")
        self.click_header_search_field()
        self.fill_city_search_field(symbol)
        assert search_placeholder_text not in self.get_header_search_field_attribute(attribute), \
            "The placeholder text is still visible in the search field after typing a symbol"

    def check_current_and_forecast_apis_functionality(self):
        current_and_forecast_apis = self.driver.find_element(*self.locators.CURRENT_AND_FORECAST_APIS)
        self.go_to_element(current_and_forecast_apis)
        current_and_forecast_apis.click()
        assert '/api#current' in self.driver.current_url, \
            "The link 'current_and_forecast_apis' leads to incorrect page"

    def verify_clickability_current_and_forecast_apis(self):
        self.driver.find_element(*self.locators.COOKIES).click()
        current_and_forecast_apis = self.driver.find_element(*self.locators.CURRENT_AND_FORECAST_APIS)
        assert current_and_forecast_apis.is_displayed() and current_and_forecast_apis.is_enabled(), \
            "The 'current_and_forecast_apis' link is not displayed on the page or is not clickable"

    def verify_widgets_clickability(self):
        self.driver.find_element(*self.locators.COOKIES).click()
        widgets = self.driver.find_element(*self.locators.WIDGETS)
        assert widgets.is_displayed() and widgets.is_enabled(), \
            "The 'widgets' link is not displayed on the page or is not clickable"

    def verify_how_to_start_visibility(self):
        how_to_start = self.driver.find_element(*self.locators.HOW_TO_START)
        assert how_to_start.is_displayed(), "The How to start link is not visible"

    def verify_privacy_policy_is_opened_after_click(self, driver, wait):
        privacy_policy_button = wait.until(EC.element_to_be_clickable(self.locators.XPATH_PRIVACY_POLICY_BUTTON))
        self.driver.execute_script("arguments[0].click();", privacy_policy_button)
        self.driver.switch_to.window(driver.window_handles[1])
        assert self.driver.current_url == Links.PRIVACY_POLICY_URL

    def click_support_link(self):
        return self.driver.find_element(*self.locators.SUPPORT_MENU).click()

    def faq_submenu_should_be_visible(self, wait):
        element = wait.until(EC.visibility_of_element_located(BasePageLocators.FAQ_OPTION))
        assert element.is_displayed() and element.is_enabled(), f'"{element}" link is not visible or clickable'

    def click_footer_product_collections_widgets(self, expected_link):
        self.allow_all_cookies()
        widgets_link = self.element_is_clickable(self.locators.WIDGETS)
        link_href = widgets_link.get_attribute('href')
        assert link_href == expected_link, "Incorrect link"

    def click_footer_product_collections_all_widgets(self, expected_link, link_number):
        self.allow_all_cookies()
        widgets_link = self.element_is_clickable(self.locators.product_collection[link_number])
        link_href = widgets_link.get_attribute('href')
        assert link_href in expected_link, "Incorrect link"

    def verify_chart_weather_is_present(self):
        assert self.element_is_present(self.locators.CHART_WEATHER), "Chart weather is not present"

    def verify_the_copyright_information_is_present_on_the_page(self):
        self.allow_all_cookies()
        expected_footer_text = "© 2012 — 2023 OpenWeather"
        footer = self.driver.find_element(*FooterLocators.FOOTER_COPYRIGHT)
        assert footer.is_displayed() and expected_footer_text in footer.text, \
            "The footer is not displayed or does not contain the expected text"
    def about_us_link_leads_to_correct_page(self):
        about_us_link = self.driver.find_element(*MainPageLocators.ABOUT_US_LINK)
        self.go_to_element(about_us_link)
        about_us_link.click()
        assert '/about-us' in self.driver.current_url, "The about us link leads to an incorrect page"

    def checking_the_temperature_system_switching(self, system):
        match system:
            case "°C":
                self.driver.find_element(*self.locators.METRIC_BUTTON).click()
            case "°F":
                self.driver.find_element(*self.locators.IMPERIAL_BUTTON).click()
        current_temp = self.driver.find_element(*self.locators.CURRENT_TEMP)
        assert system in current_temp.text, f"The current temperature does not correspond to the {system} system"

    def verify_temperature_button_displayed_clickable(self, system):
        match system:
            case "°C":
                metric_button = self.locators.METRIC_BUTTON
            case "°F":
                metric_button = self.locators.IMPERIAL_BUTTON
        assert self.element_is_clickable(metric_button) \
               and self.element_is_visible(metric_button), \
            "The temperature switch button in the metric system is not displayed or is not clickable"

    def verify_the_current_date_and_time(self):
        date_time = self.driver.find_element(*self.locators.LOC_DATE_TIME)
        date_time_str = f'{str(datetime.now(ZoneInfo("Europe/London")).year)} {date_time.text}'
        date_time_site = datetime.strptime(date_time_str, '%Y %b %d, %I:%M%p').replace(tzinfo=ZoneInfo('Europe/London'))
        date_time_now = datetime.now(ZoneInfo('Europe/London'))
        assert (date_time_now - date_time_site).total_seconds() <= 600, \
            "The current date and time does not match the date and time specified on the page"

    def verify_current_location(self, wait):
        expected_city_name = "Chicago, US"
        self.driver.execute_cdp_cmd(
            "Browser.grantPermissions",
            {
                "origin": Links.URL_MAIN_PAGE,
                "permissions": ["geolocation"]
            },
        )
        self.driver.execute_cdp_cmd(
            "Emulation.setGeolocationOverride",
            {
                "latitude": 41.8781,
                "longitude": -87.6298,
                "accuracy": 100,
            },
        )
        self.driver.find_element(*self.locators.LOC).click()
        wait.until_not(EC.presence_of_element_located(self.locators.LOAD_DIV))
        current_city_name = self.driver.find_element(*self.locators.CITY_NAME)
        assert expected_city_name == current_city_name.text, \
            "The current name of the city does not match the expected name of the city"

    def click_faq_option(self, wait):
        submenu = wait.until(EC.visibility_of_element_located(BasePageLocators.FAQ_OPTION))
        actions = ActionChains(self.driver)
        actions.click(submenu).perform()
        return submenu

    def check_correct_header_is_displayed(self, text):
        element_text = self.driver.find_element(*BasePageLocators.HEADER).text
        assert element_text == text, f'""Expected {text} is not present or is incorrect.'

    def check_faq_link_opens_opens_correct_page(self, wait, link):
        self.click_support_link()
        self.click_faq_option(wait=wait)
        self.check_header_link(link), "The current URL doesn't match expected link."

    def click_how_to_start_option(self, wait):
        submenu = wait.until(EC.visibility_of_element_located(BasePageLocators.HOW_TO_START_OPTION))
        actions = ActionChains(self.driver)
        actions.click(submenu).perform()
        return submenu

    def check_how_to_start_link_opens_opens_correct_page(self, wait, link):
        self.click_support_link()
        self.click_how_to_start_option(wait=wait)
        self.check_header_link(link), "The current URL doesn't match expected link."

    def check_manage_cookies_link_is_visible(self):
        manage_cookies_btn = self.element_is_visible(self.locators.MANAGE_COOKIES_BTN)
        assert manage_cookies_btn.is_displayed(), "The Manage cookies module is not visible"

    def check_manage_cookies_link_is_functionality(self):
        manage_cookies_btn = self.find_element_and_click(self.locators.MANAGE_COOKIES_BTN)
        current_url = self.driver.current_url
        expected_url = "https://openweathermap.org/cookies-settings"
        assert current_url == expected_url, f"The Manage cookie link leads to an incorrect page. Actual: {current_url}"

    def verify_how_to_start_link_is_clickable(self):
        how_to_start = self.driver.find_element(*self.locators.HOW_TO_START_LINK)
        assert how_to_start.is_enabled(), "The 'How to start' link does not clickable"

    def get_day_by_weak(self):
        element = self.element_is_visible(self.locators.FIRST_DAY_IN_8_DAY_FORECAST).text[:3]
        return element

    def get_day_by_computer(self):
        day_by_computer = datetime.now().weekday()
        today = WEEKDAYS[day_by_computer]
        return today

    def check_day(self):
        day_by_weak = self.get_day_by_weak()
        day_by_computer = self.get_day_by_computer()
        assert day_by_weak == f'{day_by_computer}', 'Module Search city widget contains the wrong day of the week '

    def go_to_module_download_openweather_app(self):
        module_download_openweather_app = self.driver.find_element(*self.locators.MODULE_DOWNLOAD_OPENWEATHER_APP)
        self.go_to_element(module_download_openweather_app)
        return module_download_openweather_app

    def check_module_title_download_openweather_app(self):
        module_download_openweather_app = self.go_to_module_download_openweather_app()
        assert module_download_openweather_app.is_displayed(), "Module title Download openweather app is not display"

    def check_app_store_brand_link_display(self):
        self.go_to_module_download_openweather_app()
        app_store_brand_link = self.driver.find_element(*self.locators.APP_STORE_BRAND_LINK)
        assert app_store_brand_link.is_displayed(), "The brand-link for Download on the App Store is not displaying"

    def check_buttons_displayed_and_enabled(self):
        imperial_button = self.driver.find_element(*self.locators.IMPERIAL_BUTTON)
        metric_button = self.driver.find_element(*self.locators.METRIC_BUTTON)
        assert all(button.is_displayed() and button.is_enabled() for button in [metric_button, imperial_button]), \
            "Toggle buttons are not displayed or enabled"

    def check_app_store_brand_link_clickable(self):
        initial_page_number = len(self.driver.window_handles)
        self.go_to_module_download_openweather_app()
        app_store_brand_link = self.driver.find_element(*self.locators.APP_STORE_BRAND_LINK)
        app_store_brand_link.click()
        actual_page_number = len(self.driver.window_handles)
        assert actual_page_number == initial_page_number + 1, \
            "The new web tab does not opened after click App Store brand-link's"

    def check_google_play_brand_link_clickable(self):
        initial_page_number = len(self.driver.window_handles)
        self.go_to_module_download_openweather_app()
        google_play_brand_link = self.driver.find_element(*self.locators.GOOGLE_PLAY_BRAND_LINK)
        google_play_brand_link.click()
        actual_page_number = len(self.driver.window_handles)
        assert actual_page_number == initial_page_number + 1, \
            "The new web tab does not opened after click Google Play brand-link's"

    def check_google_play_brand_link_display(self):
        self.go_to_module_download_openweather_app()
        google_play_brand_link = self.driver.find_element(*self.locators.GOOGLE_PLAY_BRAND_LINK)
        assert google_play_brand_link.is_displayed(), "Google Play brand-link is not displaying"

    def get_months(self):
        month = self.element_is_visible(self.locators.FIRST_DAY_IN_8_DAY_FORECAST).text[5:-3]
        return month

    def get_months_by_computer(self):
        month_by_computer = datetime.now().month
        current_month = MONTHS[month_by_computer - 1]
        return current_month

    def check_months(self):
        page_month = self.get_months()
        page_month_by_computer = self.get_months_by_computer()
        assert page_month in f'{page_month_by_computer}'

    def find_search_city_input(self, key):
        self.driver.find_element(*self.locators.SEARCH_CITY_FIELD).send_keys(key)

    def click_btn_search(self):
        element = self.driver.find_element(*self.locators.SEARCH_BUTTON)
        action = ActionChains(self.driver)
        action.click(on_element=element)
        action.perform()

    def check_dropdown_options(self):
        self.find_search_city_input(KEYS_FOR_SEARCH_CITY_INPUT)
        self.click_btn_search()
        dropdown_list = self.driver.find_elements(*self.locators.SEARCH_DROPDOWN)
        for i in dropdown_list:
            assert 'California' in i.text, 'Not all search suggestions in the drop-down list contain "California"'

    def click_first_element_dropdown_menu(self, wait):
        element_dropdown_menu = wait.until(EC.element_to_be_clickable(self.locators.SEARCH_DROPDOWN))
        element_dropdown_menu.click()
        self.element_is_present(self.locators.DISPLAYED_CITY, 10)

    def get_city_text(self, wait):
        wait.until(EC.text_to_be_present_in_element(self.locators.DISPLAYED_CITY, 'Atchison'))
        displayed_city = self.driver.find_element(*self.locators.DISPLAYED_CITY).text
        return displayed_city

    def check_city_name_displayed_by_zip(self, wait):
        self.find_search_city_input(KEYS_FOR_SEARCH_CITY_INPUT_ZIP)
        self.click_btn_search()
        self.click_first_element_dropdown_menu(wait)
        displayed_city = self.get_city_text(wait)
        assert displayed_city == EXPECTED_CITY

    def number_day_by_computer(self):
        return datetime.now().day

    def check_leap_year_for_february_days(self):
        year = datetime.now().year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            last_num = 29
        else:
            last_num = 28
        return last_num

    def find_number_of_days_in_a_month(self):
        month = self.get_months_by_computer()
        if month in MONTH_28:
            self.check_leap_year_for_february_days()
        elif month in MONTH_31:
            last_num = 31
        elif month in MONTH_30:
            last_num = 30
        return last_num

    def get_correct_list_num_days(self):
        correct_list = []
        first_num = self.number_day_by_computer()
        correct_list.append(first_num)
        number_of_days_in_a_month = self.find_number_of_days_in_a_month()
        for i in range(first_num + 1, first_num + 8):
            if i <= number_of_days_in_a_month:
                correct_list.append(i)
        len_correct_list = len(correct_list)
        if len_correct_list < 8:
            for i in range(1, 9 - len_correct_list):
                correct_list.append(i)
        return correct_list

    def get_num_days_by_page(self, driver):
        self.driver.find_element(*self.locators.LIST_DAYS_IN_8_DAY_FORECAST).location_once_scrolled_into_view
        days_by_page = []
        days = driver.find_elements(*self.locators.DAYS_IN_8_DAY_FORECAST_NUM)
        for day in days:
            days_by_page.append(day.text[-2:])
        days_by_page = list(map(int, days_by_page))
        return days_by_page

    def check_in_day_list_numbers_days(self, driver):
        expected_list = self.get_correct_list_num_days()
        actual_list = self.get_num_days_by_page(driver)
        assert actual_list == expected_list, 'Module Search city widget 8-day-forecast contains invalid day numbers'

    def verify_in_day_list_first_element_number_day(self):
        number_day = self.driver.find_element(*self.locators.FIRST_DAY_IN_8_DAY_FORECAST).text[-2:]
        if number_day.startswith('0'):
            number_day = number_day[1:]
        number_day_by_computer = datetime.now().day
        assert number_day == f'{number_day_by_computer}'

    def verify_in_day_list_days_of_the_week(self):
        days_by_page = []
        days = self.driver.find_elements(*self.locators.DAYS_IN_8_DAY_FORECAST)
        for day in days:
            days_by_page.append(day.text[:3])
        number_day = datetime.now().weekday()
        days_by_computer = WEEKDAYS[number_day:] + WEEKDAYS[:number_day] + WEEKDAYS[(number_day):(number_day + 1):]
        assert days_by_page == days_by_computer

    def enter_city_in_weather_in_your_city_field(self, city):
        input_city = self.driver.find_element(*self.locators.FIELD_WEATHER_IN_YUOR_CITY)
        input_city.send_keys(city)


    def check_footer_website_is_displayed(self, element):
        assert element.is_displayed() and self.driver.title not in 'Page not found (404) - OpenWeatherMap', \
            f'\nFooter is not present on the page - {self.driver.current_url}'

    def check_copyright_is_displayed(self, element):
        copyright_expected_result = ['©', '2012 — 2023', 'OpenWeather', '® All rights reserved']
        copyright_actual_result = element.text
        copyright_flag = 1
        for i in copyright_expected_result:
            if i not in copyright_actual_result:
                copyright_flag = 0
        assert element.is_displayed() and copyright_flag == 1, f'\nCopyright is not present (actual) on the page - {self.driver.current_url}'

    def check_leads_link_Googl_Play(self):
        self.driver.execute_script("window.scrollTo(100,document.body.scrollHeight);")
        google_play = self.driver.find_element(*self.locators.GOOGLE_PLAY_BRAND_LINK)
        self.driver.execute_script("arguments[0].click();", google_play)
        self.driver.switch_to.window(self.driver.window_handles[1])
        expected_title = 'OpenWeather'
        assert '/play.google' in self.driver.current_url and expected_title in self.driver.title

    def check_description_weather_block(self, text):
        description_weather = self.driver.find_element(*self.locators.ACTUAL_WEATHER)
        description_weather_text = description_weather.text
        assert description_weather.is_displayed() and text in description_weather_text

    def dropdown_contain_city_temperature(self):
        search_city_input = self.driver.find_element(*self.locators.SEARCH_CITY_FIELD)
        search_city_input.click()
        search_city_input.send_keys(*self.locators.KEY_SEARCH_CITY)
        self.driver.find_element(*self.locators.SEARCH_BUTTON).click()
        dropdown_list = self.driver.find_elements(*self.locators.SEARCH_DROPDOWN)
        for city in dropdown_list:
            assert '°C' in city.text

    def verify_marketplace_link_redirects_to_valid_page(self):
        self.click_header_link("marketplace")
        assert self.driver.current_url == Links.URL_MARKETPLACE

    def check_logo_is_visible(self):
        logo = self.driver.find_element(*self.locators.LOGO_LOCATOR)
        assert logo.is_displayed(), "Logo is not visible"

    def check_product_collections_module_title_is_visible(self):
        title = self.driver.find_element(*self.locators.TITLE_LOCATOR)
        assert title.is_displayed(), "Title is not visible"

    def graphic_hourly_forecast_is_displayed(self, wait):
        graphic_hourly_forecast = self.driver.find_element(*self.locators.CHART_WEATHER)
        self.go_to_element(graphic_hourly_forecast)
        assert self.element_is_visible

    def weather_items_are_displayed(self, wait):
        self.driver.get('https://openweathermap.org/')
        weather_items = self.driver.find_elements(*self.locators.WEATHER_ITEMS_LOCATOR)
        self.driver.execute_script("arguments[0].scrolldown;", weather_items)
        assert self.weather_items_are_displayed
