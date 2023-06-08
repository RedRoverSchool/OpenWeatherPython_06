from selenium.webdriver.common.by import By


class DashboardLocators:
    URL = 'https://openweathermap.org/'
    DASHBOARD_URL = 'https://openweathermap.org/weather-dashboard'
    dashboard_button_locator = (By.CSS_SELECTOR, '#mobile-menu > li:nth-child(4) > a')
    hourly_forecast_api_locator = (By.CSS_SELECTOR, 'div.col-lg-3 a')
