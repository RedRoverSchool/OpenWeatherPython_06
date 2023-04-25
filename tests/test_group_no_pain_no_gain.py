from selenium.webdriver.common.by import By

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

