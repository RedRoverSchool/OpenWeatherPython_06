from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
URL = 'https://openweathermap.org/'
URL2 = 'https://home.openweathermap.org/users/sign_in'

def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url


def test_check_page_title(driver):
    driver.get(URL)
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'
    print(f'The site title is: {driver.title}')


def test_look_for_buttons(driver):
    driver.get(URL)
    search_button = driver.find_element(By.CSS_SELECTOR, "button[class='button-round dark']")
    weather_widget_weather_button = driver.find_element(By.XPATH, "//*[contains(text(),'Different Weather')]")
    weather_widget_metric_button = driver.find_element(By.XPATH, "//*[contains(text(),'Metric')]")
    weather_widget_imperial_button = driver.find_element(By.XPATH, "//*[contains(text(),'Imperial')]")
    expected_button1 = 'Search'
    expected_button2 = 'Different Weather?'
    expected_button3 = 'Metric: °C, m/s'
    expected_button4 = 'Imperial: °F, mph'
    assert search_button.text == expected_button1
    assert weather_widget_weather_button.text == expected_button2
    assert weather_widget_metric_button.text == expected_button3
    assert weather_widget_imperial_button.text == expected_button4
    print('\n')
    print(f'The Search button text is: {search_button.text}')
    print(f'The Weather button text is: {weather_widget_weather_button.text}')
    print(f'The Metric button text is: {weather_widget_metric_button.text}')
    print(f'The Imperial button text is: {weather_widget_imperial_button.text}')


def test_click_guide(driver):
    driver.get(URL)
    search_link_guide = driver.find_element(By.XPATH, '//*[@id="desktop-menu"]/ul/li[1]/a')
    action_chains = ActionChains(driver)
    action_chains.move_to_element(search_link_guide)
    driver.execute_script("arguments[0].click();", search_link_guide)
    assert driver.title == 'OpenWeatherMap API guide - OpenWeatherMap'
    print(f'Website page title is: {driver.title}')


def test_should_open_url2(driver):
    driver.get(URL2)
    assert driver.current_url == URL2


def test_documentation_button(driver):
    driver.get('https://home.openweathermap.org/marketplace')
    documentation_button = driver.find_element(By.XPATH,
                                               "//div[@class = 'product' and contains(., 'History Bulk')]"
                                               "//a[text()= 'Documentation']")
    documentation_button.click()
    driver.switch_to.window(driver.window_handles[1])
    assert 'https://openweathermap.org/history-bulk' in driver.current_url


def test_order_button(driver):
    driver.get('https://home.openweathermap.org/marketplace')
    order_button = driver.find_element(By.XPATH,
                                       "//div[@class = 'product' and contains(., 'History Bulk')]"
                                       "//a[text()= 'Place order']")
    order_button.click()
    assert 'https://home.openweathermap.org/history_bulks/new' in driver.current_url
