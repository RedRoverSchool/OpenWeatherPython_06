from datetime import datetime, date
from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPage(BasePage):

    search_city_field = (By.CSS_SELECTOR, 'input[placeholder="Search city"]')
    search_button = (By.CSS_SELECTOR, 'button[class ="button-round dark"]')
    search_option = (By.XPATH, "//span[contains(text(), city)]")
    weekday_8_days_forecast = (By.XPATH, "//div//li[@data-v-5ed3171e]/span")

    def verify_weekdays_8days_forecast(self):
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

        week_day_8_days_forecast = self.driver.find_elements(*self.weekday_8_days_forecast)
        weekdays_on_app = []
        for day in week_day_8_days_forecast:
            weekdays_on_app.append(day.text[:3])

        assert weekdays_on_app == weekdays_expected



