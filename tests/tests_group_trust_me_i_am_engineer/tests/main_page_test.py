from selenium.webdriver.common.by import By
from tests.tests_group_trust_me_i_am_engineer.pages.main_page import *
import pytest

URL = 'https://openweathermap.org/'
URL_WEATHER_API = 'https://openweathermap.org/api'
URL_MARKETPLACE = 'https://home.openweathermap.org/marketplace'
URL_OUR_INITIATIVES = 'https://openweathermap.org/our-initiatives'
URL_WEATHER_CONDITIONS = 'https://openweathermap.org/weather-conditions'
metric_button_loc = (By.XPATH, "//div[@class='switch-container']/div[contains(text(), 'Metric')]")
imperial_button_loc = (By.XPATH, "//div[@class='switch-container']/div[contains(text(), 'Imperial')]")
current_temp_loc = (By.CSS_SELECTOR, "div.current-temp span.heading")
loc_date_time = (By.XPATH, "//div[@class='current-container mobile-padding']/div/span[@class='orange-text']")
our_initiatives_link = (By.CSS_SELECTOR, '#desktop-menu ul li:nth-child(7)')
learn_more_link = (By.CSS_SELECTOR, 'a[class="ow-btn round btn-black"]')
learn_more_page_title = (By.CSS_SELECTOR, "h1[class='breadcrumb-title']")
weather_api_page_title = (By.CSS_SELECTOR, "h1.breadcrumb-title")
history_bulk_title = (By.XPATH, "//h5/a[contains(text(), 'History Bulk')]")
history_bulk_search_location = (By.ID, "firstSearch")
buttons_search_methods = (By.XPATH, "//div[@class='search-pop-up']/button")
button_by_location = (By.XPATH, "//button[contains(text(), 'By location')]")
button_by_coordinates = (By.XPATH, "//button[contains(text(), 'By coordinates')]")
input_latitude = (By.XPATH, "//input[@placeholder='Latitude']")
input_longitude = (By.XPATH, "//input[@placeholder='Longitude']")
latitude_on_map = (By.XPATH, "//div[@class='text']/p[1]")
longitude_on_map = (By.XPATH, "//div[@class='text']/p[2]")
search_pop_up = (By.CSS_SELECTOR, "div.search-pop-up")
first_search_items = (By.XPATH, "/html/body/div[4]/div[1]/span[2]/span")
search_results = (By.CSS_SELECTOR, "div.pac-container.pac-logo.hdpi")
search_pop_up_header = (By.XPATH, "//div[@class='pop-up-marker']/div[@class='pop-up-header']/h3")
headers_selector = (By.XPATH, "//h2[@style='margin-top: 0;']")
icon_list_description = (By.XPATH, "//table[@class='table table-bordered'][1]/tbody/tr/td[3]")
city_name = (By.CSS_SELECTOR, "div.current-container.mobile-padding div h2")
loc = (By.CSS_SELECTOR, "div.control-el svg.icon-current-location")
load_div = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
search_city_field_locator = (By.CSS_SELECTOR, 'input[placeholder="Search city"]')
search_button_locator = (By.CSS_SELECTOR, 'button[class ="button-round dark"]')
search_option_locator = (By.XPATH, "//span[contains(text(), city)]")
weekday_8_days_forecast_locator = (By.XPATH, "//div//li[@data-v-5ed3171e]/span")
map_button_loc = (By.XPATH, "//div[@class='gm-style-mtc']/button[contains(text(), 'Map')]")
footer_pricing_link = (By.XPATH, "//div[@class='inner-footer-container']//a[text()='Pricing']")
header_pricing = (By.XPATH, "//div[@id='desktop-menu']//a[text()='Pricing']")
pricing_page_title = (By.XPATH, "//h1[text()='Pricing']")
openweather_for_business_link = (By.XPATH, "//a[text()='OpenWeather for Business']")


def test_tc_001_04_06_1_verify_visibility_of_week_days_in_8_days_forecast(driver, open_and_load_main_page, wait):
    page = MainPage(driver)
    page.verify_weekdays_8days_forecast()