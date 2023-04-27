import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import datetime

test_email = 'chosenonex1@gmail.com'
test_password = 'gNrts5W?K_.qLFu'
API_key = '2c254a2efb0b9008ce295e94a0939a2f'
cities = ['Moscow', 'Paris']
URL = 'https://openweathermap.org/'

def test_open_page(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url # проверка наличия строки в url

def test_sing_in_empty_fields(driver):
    driver.get('https://home.openweathermap.org/users/sign_in')
    driver.find_element(By.XPATH, '//*[@id="new_user"]/input[3]').click()
    alert = driver.find_element(By.XPATH, '//*[@class="panel-body"]')
    assert alert.text == 'Invalid Email or password.'

def test_sing_in_positive(driver):
    driver.get('https://home.openweathermap.org/users/sign_in')
    email_form = driver.find_element(By.XPATH, '//*[@id = "user_email"]')
    email_form.click()
    email_form.send_keys(test_email)
    password_form = driver.find_element(By.XPATH, '//*[@id = "user_password"]')
    password_form.click()
    password_form.send_keys(test_password)
    remember_checkbox = driver.find_element(By.XPATH, '//*[@id = "user_remember_me"]')
    assert remember_checkbox.is_selected() == False
    driver.find_element(By.XPATH, '//*[@id="new_user"]/input[3]').click()
    driver.implicitly_wait(15)
    assert 'home.openweathermap' in driver.current_url
    alert = driver.find_element(By.XPATH, '//*[@class="panel-body"]')
    assert alert.text == 'Signed in successfully.'

def test_open_weather_map(driver):
    driver.get(URL)
    WebDriverWait(driver, 15).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    # driver.implicitly_wait(15)
    # zoom_map = WebDriverWait(driver, 15).until(
    #     EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "weathermap?zoom")]')))
    driver.find_element(By.XPATH, '//button[text()="Allow all"]').click()
    zoom_map = driver.find_element(By.XPATH, '//a[contains(@href, "weathermap?zoom")]')
    zoom_map.click()
    window_weathermap_zoom = driver.window_handles[1] # возвращаем дескриптор новой страницы
    driver.switch_to.window(window_weathermap_zoom) # переключаем selenium на новую страницу
    assert driver.title == 'Interactive weather maps - OpenWeatherMap'

@pytest.mark.parametrize('city', cities)
def test_current_weather_api(city):
    payload = {'q': f'{city}',
               'appid': f'{API_key}'}
    response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=payload)
    response_data = response.json()
    assert response.status_code == 200
    expected_keys = ['coord', 'weather', 'main', 'id', 'name']
    for key in expected_keys:
        assert key in response_data.keys()
    assert response.json()['name'] == city


def test_8_days_forecast(driver): # проверка, что отображается прогноз на 8 дней
    driver.get("https://openweathermap.org/")
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    amount_of_days = len(driver.find_elements(By.XPATH, '//*[@class="day-list"]/li'))
    assert amount_of_days == 8


def test_find_title_Olga():  # проверка заголовка статьи
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://openweathermap.org/')
    driver.maximize_window()
    title_article = driver.find_element(By.XPATH, '/html/body/main/div[13]/div/div[3]/h2')
    time.sleep(10)
    title_expect = "Forecast, Current and Historical"
    assert title_article.text == title_expect
