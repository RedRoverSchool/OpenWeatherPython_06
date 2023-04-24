from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_fill_search_city_field(driver):
    driver.get('https://openweathermap.org/')
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    search_city_field.send_keys('New York')
    search_button = driver.find_element(By.CSS_SELECTOR, "button[class ='button-round dark']")
    search_button.click()
    search_option = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')))
    search_option.click()
    expected_city = 'New York City, US'
    WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2'), 'New York'))
    displayed_city = driver.find_element(By.CSS_SELECTOR, '.grid-container.grid-4-5 h2').text
    assert displayed_city == expected_city


def test_check_page_title(driver):
    driver.get('https://openweathermap.org')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'

def test_authorization(driver):
    driver.get('https://openweathermap.org/')
    assert 'openweathermap' in driver.current_url, 'openweathermap is not in URL'
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    driver.find_element(By.CSS_SELECTOR, '.user-li').click()
    assert 'users/sign_in' in driver.current_url, 'wrong URL'
    assert driver.title == 'Members', 'wrong title'
    driver.find_element(By.CSS_SELECTOR, '.input-group #user_email').send_keys('jnksdcj')
    driver.find_element(By.CSS_SELECTOR, '.input-group #user_password').send_keys('adnai')
    driver.find_element(By.CSS_SELECTOR, 'input[value="Submit"]').click()
    assert 'Invalid Email or password.' in driver.find_element(By.CSS_SELECTOR, '.panel-body').text,\
        'trouble with hint - negative case'
    driver.find_element(By.CSS_SELECTOR, '.input-group #user_email').clear()
    driver.find_element(By.CSS_SELECTOR, '.input-group #user_email').send_keys('danya92656@gmail.com')
    driver.find_element(By.CSS_SELECTOR, '.input-group #user_password').clear()
    driver.find_element(By.CSS_SELECTOR, '.input-group #user_password').send_keys('007007007')
    driver.find_element(By.CSS_SELECTOR, 'input[value="Submit"]').click()
    assert 'Signed in successfully.' in driver.find_element(By.CSS_SELECTOR, '.panel-body').text, 'wrong hint - signed was succeced'