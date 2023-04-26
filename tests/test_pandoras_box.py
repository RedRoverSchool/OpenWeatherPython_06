from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
URL = 'https://openweathermap.org/'

def test_open_page(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url # проверка наличия строки в url

def test_current_time(driver): # проверка текущей даты и времени
    driver.get("https://openweathermap.org/")
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    current_time = datetime.datetime.now().strftime("%b %d, %I:%M%p").lower()
    current_time_from_page = driver.find_element(
        By.XPATH, '//div[@id="weather-widget"]//descendant::span[@class="orange-text"]').text.lower()
    assert current_time == current_time_from_page


def test_8_days_forecast(driver): # проверка, что отображается прогноз на 8 дней
    driver.get("https://openweathermap.org/")
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    amount_of_days = len(driver.find_elements(By.XPATH, '//*[@class="day-list"]/li'))
    assert amount_of_days == 8



