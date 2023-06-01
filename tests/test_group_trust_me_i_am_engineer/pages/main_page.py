from selenium.webdriver.support import expected_conditions as EC
from pages import base_page
from pages.base_page import BasePage
from tests.test_group_trust_me_i_am_engineer.locators.page_locators import MainPageLocators
from datetime import datetime, date
from zoneinfo import ZoneInfo
from conftest import load_div


class MainPage(BasePage):
    URL = 'https://openweathermap.org/'
    locators = MainPageLocators()
    linkedin_link = 'https://www.linkedin.com/company/openweathermap/'

    def verify_weekdays_in_8_days_forecast(self):
        list_weekdays = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon')
        today = datetime.now()
        num_today_weekday = date.weekday(today)
        weekdays_expected = []
        num_next_day_weekday = num_today_weekday
        for i in range(8):
            if num_next_day_weekday > 7:
                num_next_day_weekday = num_next_day_weekday - 7
                weekdays_expected.append(list_weekdays[num_next_day_weekday])
            else:
                weekdays_expected.append(list_weekdays[num_next_day_weekday])
            num_next_day_weekday += 1

        week_day_8_days_forecast = self.driver.find_elements(*self.locators.WEEKDAY_IN_8_DAYS_FORECAST)
        weekdays_on_app = []
        for day in week_day_8_days_forecast:
            weekdays_on_app.append(day.text[:3])

        assert weekdays_on_app == weekdays_expected

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
        assert (date_time_now - date_time_site).total_seconds() <= 240, \
            "The current date and time does not match the date and time specified on the page"

    def verify_current_location(self, wait):
        expected_city_name = "Chicago, US"
        self.driver.execute_cdp_cmd(
            "Browser.grantPermissions",
            {
                "origin": self.URL,
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

    def verify_pricing_link_leads_to_a_correct_page(self):
        pricing_link = self.driver.find_element(*self.locators.FOOTER_PRICING_LINK)
        self.go_to_element(pricing_link)
        pricing_link.click()
        assert '/price' in self.driver.current_url, \
            "The link 'Pricing' leads to incorrect page"

    def check_a_visibility_of_pricing_page_title(self):
        expected_pricing_page_title = "Pricing"
        self.click_header_link("pricing")
        pricing_page_title = self.element_is_visible(self.locators.PRICING_PAGE_TITLE)
        assert pricing_page_title.text == expected_pricing_page_title, \
            "The title of the Pricing page does not match the expected title"

    def verify_the_link_openweather_for_business_is_visible(self):
        for_business_link = self.driver.find_element(*self.locators.FOR_BUSINESS_LINK)
        self.go_to_element(for_business_link)
        assert self.element_is_visible(self.locators.FOR_BUSINESS_LINK), \
            "OpenWeather for Business is not visible on the page"

    def verify_link_LinkedIn_leads_to_the_correct_page(self):
        self.driver.execute_script("window.scrollTo(0, 500)")
        linkedin_element = self.driver.find_element(*self.locators.FOOTER_LINKEDIN_LINK)
        self.driver.execute_script("arguments[0].click();", linkedin_element)
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert self.linkedin_link, self.driver.current_url

    def go_to_about_us_page(self, wait):
        self.driver.get(self.URL)
        wait.until_not(EC.presence_of_element_located(load_div))

        self.allow_all_cookies()
        self.element_is_clickable(self.locators.ABOUT_US_BUTTON).click()

