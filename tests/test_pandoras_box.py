from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import pytz
URL = 'https://openweathermap.org/'

def test_open_page(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url # проверка наличия строки в url

def test_current_time(driver): # проверка текущей даты и времени
    driver.get("https://openweathermap.org/")
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    search_city_field.send_keys('Minsk')
    search_button = driver.find_element(By.CSS_SELECTOR, "button[class ='button-round dark']")
    search_button.click()
    search_option = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')))
    search_option.click()
    current_time = datetime.datetime.now(pytz.timezone('Europe/Moscow')).strftime("%b %d, %I:%M%p").lower()[:12]
    print(current_time)
    current_time_from_page = driver.find_element(
        By.XPATH, '//div[@id="weather-widget"]//descendant::span[@class="orange-text"]').text.lower()[:12]
    assert current_time == current_time_from_page


def test_8_days_forecast(driver): # проверка, что отображается прогноз на 8 дней
    driver.get("https://openweathermap.org/")
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    amount_of_days = len(driver.find_elements(By.XPATH, '//*[@class="day-list"]/li'))
    assert amount_of_days == 8



