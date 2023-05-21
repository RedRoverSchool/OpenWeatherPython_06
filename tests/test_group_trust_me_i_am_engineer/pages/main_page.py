from selenium.webdriver.support import expected_conditions as EC
from OpenWeatherPython_06.pages import base_page
from OpenWeatherPython_06.pages.base_page import BasePage
from OpenWeatherPython_06.tests.test_group_trust_me_i_am_engineer.locators.page_locators import MainPageLocators
from datetime import datetime, date
from zoneinfo import ZoneInfo

class MainPage(BasePage):
    URL = 'https://openweathermap.org/'
    locators = MainPageLocators()

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
