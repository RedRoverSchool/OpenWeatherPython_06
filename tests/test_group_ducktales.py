from selenium.webdriver import Keys
import pytest
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import random
import string

URL_sing_in_page = "https://home.openweathermap.org/users/sign_in"
email_field = (By.ID, 'user_email')
user_email = "jtzcmspsmgvbep@bugfoo.com"
user_password = "Test1212"
password_field = (By.ID, 'user_password')
submit_button = (By.CSS_SELECTOR, '.btn-color[value="Submit"]')
tab_api_keys = (By.CSS_SELECTOR, '#myTab [href="/api_keys"')
URL_api_keys_page = 'https://home.openweathermap.org/api_keys'
SIGN_IN_ALERT = By.CLASS_NAME, 'panel-body'


def random_word():
    letters = string.ascii_lowercase
    random_word = ''.join(random.choice(letters) for _ in range(8))
    return random_word


@pytest.fixture()
def open_api_keys_page(driver):
    wait = WebDriverWait(driver, 15)
    driver.get(URL_sing_in_page)
    wait.until(EC.element_to_be_clickable(email_field)).send_keys(user_email)
    wait.until(EC.element_to_be_clickable(password_field)).send_keys(user_password)
    wait.until(EC.element_to_be_clickable(submit_button)).click()
    wait.until(EC.element_to_be_clickable(tab_api_keys)).click()


class TestSignInPage:
    def test_wrong_data_get_alert(self, driver):
        wait = WebDriverWait(driver, 15)
        driver.get(URL_sing_in_page)
        wait.until(EC.element_to_be_clickable(email_field)).send_keys(random_word())
        wait.until(EC.element_to_be_clickable(password_field)).send_keys(random_word())
        wait.until(EC.element_to_be_clickable(submit_button)).click()
        assert driver.find_element(*SIGN_IN_ALERT).is_displayed(), "не отображается 'Alert Invalid...' "


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


def test_authorization_page(driver):
    pass


def test_registration(driver):
    driver.get('https://openweathermap.org/home/sign_in')
    enter_email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user_email")))
    enter_email.send_keys('badlolpro@gmail.com')
    enter_password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user_password")))
    enter_password.send_keys('36Pv@tdm2H7/x-d')
    click_submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='Submit']")))
    click_submit_button.click()
    expected_message = 'Signed in successfully.'
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='panel-body']")))
    assert success_message.text == expected_message
