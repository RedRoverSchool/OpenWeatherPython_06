from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

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

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url1 = 'https://home.openweathermap.org/users/sign_in'

user_name1 = 'murzin199593@gmail.com'
password1 = '1234567890'
def test_authorization():
    browser.get(url1)
    user_name = browser.find_element(By.XPATH, "//input[@id='user_email']")
    user_name.send_keys(user_name1)
    password = browser.find_element(By.XPATH, "//input[@id='user_password']")
    password.send_keys(password1)
    submit_btn = browser.find_element(By.XPATH, "//input[@name='commit']")
    submit_btn.click()
    notice = browser.find_element(By.XPATH, "//*[@class='panel-body']")
    value_notice = notice.text
    assert value_notice == 'Signed in successfully.'

