import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://openweathermap.org/'
WRONG_LOGIN = 'error@gmail.com'
WRONG_PASSWORD = 'error'
SIGN_IN_PAGE = 'https://home.openweathermap.org/users/sign_in'

def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url

def test_check_page_title(driver):
    driver.get(URL)
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'

def test_check_logo_visibility(driver):
    driver.get(URL)
    logo = driver.find_element(By.CSS_SELECTOR, "#first-level-nav > li.logo > a > img")
    assert logo.is_displayed() == True

def test_wrong_login_password(driver):
    driver.get(SIGN_IN_PAGE)
    element = driver.find_element(By.XPATH, "//div[@class='input-group']//input[@id='user_email']")
    text = element.get_attribute('placeholder')
    assert text == 'Enter email'
    element.send_keys(WRONG_LOGIN)
    element = driver.find_element(By.XPATH, "//div[@class='input-group']//input[@id='user_password']")
    text = element.get_attribute('placeholder')
    assert text == 'Password'
    element.send_keys(WRONG_PASSWORD)
    cssValue = driver.find_element(By.XPATH, "//input[@value='Submit']").value_of_css_property(
        "cursor"
    )
    assert cssValue == "pointer"
    driver.find_element(By.XPATH, "//input[@value='Submit']").click()
    driver.find_element(By.XPATH, "//div[@class='panel-heading']"), 'NO ALERT'
    driver.find_element(By.XPATH, "//*[contains(text(), 'Invalid Email or password.')]")

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


def test_recover_password(driver):
    driver.get(SIGN_IN_PAGE)
    cssValue = driver.find_element(By.XPATH, "//a[@href='#']").value_of_css_property(
        "cursor"
    )
    assert cssValue == "pointer"
    driver.find_element(By.XPATH, "//a[@href='#']").click()
    element = driver.find_element(By.XPATH, "//input[@class='form-control string email optional']")
    text = element.get_attribute('placeholder')
    assert text == 'Enter email'
    driver.find_element(By.XPATH, "//input[@class='form-control string email optional']").send_keys(WRONG_LOGIN)
    cssValue = driver.find_element(By.XPATH, "//input[@value='Send']").value_of_css_property(
        "cursor"
    )
    assert cssValue == "pointer"
    WebDriverWait(driver, 10).until_not(EC.text_to_be_present_in_element_value(
        (By.XPATH, "//input[@value='Send']"), "Create user"))
    driver.find_element(By.XPATH, "//input[@value='Send']").click()
    assert "users/password" in driver.current_url
    driver.find_element(By.XPATH, "//div[@class='panel-heading']"), 'NO ERROR MESSAGE!'
    driver.find_element(By.XPATH, "// *[contains(text(), 'Email not found')]"), 'NO EMAIL NOT FOUND MESSAGE!'
    driver.find_element(By.XPATH, "//div[@class='sign-form']"), 'NO FORGOT YOUR PASSWORD FORM!!'
    driver.find_element(By.XPATH, "//*[contains(text(),'Forgot your password?')]")
    element = driver.find_element(By.ID, "user_email")
    text = element.get_attribute('placeholder')
    assert text == 'Enter email'
    element = driver.find_element(By.ID, "user_email")
    text = element.get_attribute('value')
    assert text == WRONG_LOGIN
    driver.find_element(By.XPATH, "//input[@value='Change password']"), 'NO CHANGE PASSWORD BUTTON!'
