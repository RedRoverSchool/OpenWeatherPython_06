from selenium.webdriver.common.by import By
URL = 'https://openweathermap.org/'


def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url


def test_check_page_title(driver):
    driver.get(URL)
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'
    print(f'The site title is: {driver.title}')



def test_click_guide(driver):
    driver.get(URL)
    search_button_guide = driver.find_element(By.XPATH, '//*[@id="desktop-menu"]/ul/li[1]/a')
    search_button_guide.click()
    assert driver.title == 'OpenWeatherMap API guide - OpenWeatherMap'
    print(f'The page site title is: {driver.title}')
