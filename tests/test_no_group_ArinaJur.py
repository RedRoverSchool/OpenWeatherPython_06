from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_default_city(driver):
    wait = WebDriverWait(driver, 15)

    driver.get('https://openweathermap.org/')
    wait.until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))

    actual_city = driver.find_element(By.CSS_SELECTOR, '.current-container.mobile-padding > div > h2').text
    assert actual_city == 'London, GB'

def test_default_units(driver):
    wait = WebDriverWait(driver, 15)

    driver.get('https://openweathermap.org/')
    wait.until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))

    actual_units = driver.find_element(By.CSS_SELECTOR,'div.current-temp > span').text[-2:]
    assert  actual_units == '°C'

def test_city_name_changed_as_expected_after_search(driver):
    wait = WebDriverWait(driver, 15)

    driver.get('https://openweathermap.org/')
    wait.until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))

    # get default city and set new city
    default_city = driver.find_element(By.CSS_SELECTOR, '.current-container.mobile-padding > div > h2').text
    new_city = 'Rome, IT'

    # get search options for new city
    search_field = driver.find_element(By.CSS_SELECTOR, 'div.search-container > input')
    search_field.click()
    search_field.send_keys(new_city)
    search_field.send_keys(Keys.ENTER)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.search-dropdown-menu > li > span')))

    # select city from options
    city_choice_xpath = "//ul[@class = 'search-dropdown-menu']/li/span[contains(text(),'{}')]".format(new_city)
    driver.find_element(By.XPATH, city_choice_xpath).click()

    # search the weather in chosen city
    driver.find_element(By.CSS_SELECTOR, 'div.search > button').click()

    # wait for city name changed
    wait.until_not(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.current-container.mobile-padding > div > h2'), default_city))

    # assert city is new city"
    assert driver.find_element(By.CSS_SELECTOR, '.current-container.mobile-padding > div > h2').text == new_city

