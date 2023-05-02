def test_should_open_given_link(driver):
    driver.get('https://openweathermap.org/')
    assert 'openweathermap' in driver.current_url


def test_check_page_title(driver):
    driver.get('https://openweathermap.org/')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'

def test_open_page(driver):
    driver.get('https://openweathermap.org/')
    driver.maximize_window()
    assert 'openweathermap' in driver.current_url
    print(driver.current_url)