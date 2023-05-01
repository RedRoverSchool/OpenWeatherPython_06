from selenium.webdriver.common.by import By



def test_should_open_given_link(driver):
    driver.get('https://openweathermap.org/')
    assert 'openweathermap' in driver.current_url


def test_check_page_title(driver):
    driver.get('https://openweathermap.org/')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


def test_fill_search_city_field(driver):
    driver.get('https://openweathermap.org/')
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    assert search_city_field.is_enabled()


def test_open_page(driver):
    driver.get('https://openweathermap.org/')
    driver.maximize_window()
    assert 'openweathermap' in driver.current_url
    print(driver.current_url)

