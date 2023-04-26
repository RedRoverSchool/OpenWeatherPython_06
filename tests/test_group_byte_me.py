import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string


URL = 'https://openweathermap.org/'
URL_SignIN = 'https://home.openweathermap.org/users/sign_in'
SIGNIN_BTN = (By.CLASS_NAME, 'user-li')
LOAD_DIV = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
EMAIL_FIELD = (By.ID, 'user_email')
PASSWORD_FIELD = (By.ID, 'user_password')
SUBMIT_BTN = (By.CSS_SELECTOR, '[value="Submit"]')
SIGNIN_ALERT = (By.CLASS_NAME, 'panel-heading')
assert_msg = f'\n================\nAssertion Error\n================\n'


@pytest.fixture()
def open_page(driver):
    driver.get(URL)
    assert driver.current_url == URL, assert_msg


def random_word(): #https://flexiple.com/python/generate-random-string-python/
    random_word = ''.join(random.choice(string.ascii_letters) for _ in range(8))
    return random_word


def test_go_to_sign_in_page(driver, open_page):
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located([*LOAD_DIV]))
    try:
        driver.switch_to.alert.accept()
        wait.until(EC.element_to_be_clickable([*SIGNIN_BTN])).click()
    except:
        wait.until(EC.element_to_be_clickable([*SIGNIN_BTN])).click()
    assert "sign_in" in driver.current_url, assert_msg

@pytest.mark.parametrize(
    "email,password",
    [("", ""),
     ("", random_word()),
     (random_word(), "" ),
     (f'{random_word()}@gmail.com', random_word()),
     ("eliser89@mail.ru", random_word()),
     (random_word(), random_word())],
)
def test_login_negativ(driver, email, password):
    driver.get(URL_SignIN)
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located([*EMAIL_FIELD]))
    driver.find_element(*EMAIL_FIELD).send_keys(email)
    driver.find_element(*PASSWORD_FIELD).send_keys(password)
    wait.until(EC.element_to_be_clickable([*SUBMIT_BTN]))
    driver.find_element(*SUBMIT_BTN).click()
    assert driver.find_element(*SIGNIN_ALERT).is_displayed(), assert_msg
