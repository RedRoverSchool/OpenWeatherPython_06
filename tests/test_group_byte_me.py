import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

# ############################ LOCATORS #################################
URL = 'https://openweathermap.org/'
URL_SignIN = 'https://home.openweathermap.org/users/sign_in'
SIGNIN_BTN = (By.CSS_SELECTOR, '.user-li a')
LOAD_DIV = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
EMAIL_FIELD = (By.ID, 'user_email')
PASSWORD_FIELD = (By.ID, 'user_password')
SUBMIT_BTN = (By.CSS_SELECTOR, '[value="Submit"]')
SIGNIN_ALERT = (By.CLASS_NAME, 'panel-heading')
FOOTER_ACCEPT_BTN = (By.CSS_SELECTOR, '.stick-footer-panel__btn-container button')
USERNAME_FIELD = (By.ID, 'user_username')
REP_PASSWORD_FIELD = (By.ID, 'user_password_confirmation')
IAM16_CHECKBOX = (By.ID, 'agreement_is_age_confirmed')
AGREMENT_CHECKBOX = (By.ID, 'agreement_is_accepted')
RECAPTCHA_CHECKBOX = (By.ID, 'recaptcha-anchor')
CREATE_ACC_LINK = (By.XPATH, 'id("new_user")/following-sibling::p')
CREATE_ACC_BTN = (By.CSS_SELECTOR, '.btn.btn-color.btn-submit')
assert_msg = '\n================\nAssertion Error\n================\n'
MARKETPLACE_BTN = (By.CSS_SELECTOR, '#desktop-menu > ul li:nth-child(4) a')


# ############################ FIXTURES #################################
@pytest.fixture()
def open_page(driver):
    driver.get(URL)
    assert driver.current_url == URL, assert_msg


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, 20)
    yield wait


def random_word():  # https://flexiple.com/python/generate-random-string-python/
    random_word = ''.join(random.choice(string.ascii_letters) for _ in range(8))
    return random_word


# ############################ TESTS #################################
# def test_go_to_sign_in_page(driver, open_page, wait):
#     # wait = WebDriverWait(driver, 30)
#     wait.until_not(EC.presence_of_element_located([*LOAD_DIV]))
#     footer = driver.find_element(*FOOTER_ACCEPT_BTN)
#     footer.click()
#     signin_btn = wait.until(EC.presence_of_element_located([*SIGNIN_BTN]))
#     driver.execute_script("return arguments[0].scrollIntoView(true);", signin_btn)
#     signin_btn.click()
#     wait.until(EC.url_to_be(URL_SignIN))
#     assert "sign_in" in driver.current_url, assert_msg


def test_should_go_to_sign_in_page(driver, open_page, wait):
    sign_btn = wait.until(EC.presence_of_element_located(SIGNIN_BTN))
    driver.execute_script("arguments[0].click();", sign_btn)
    assert "sign_in" in driver.current_url, f"\nWrong URL - {driver.current_url}"


@pytest.mark.parametrize(
    "email,password",
    [("", ""),
     ("", random_word()),
     (random_word(), ""),
     (f'{random_word()}@gmail.com', random_word()),
     ("eliser89@mail.ru", random_word()),
     (random_word(), random_word())],
)
def test_login_negativ(driver, email, password, wait):
    driver.get(URL_SignIN)
    wait.until(EC.presence_of_element_located([*EMAIL_FIELD]))
    driver.find_element(*EMAIL_FIELD).send_keys(email)
    driver.find_element(*PASSWORD_FIELD).send_keys(password)
    wait.until(EC.element_to_be_clickable([*SUBMIT_BTN]))
    driver.find_element(*SUBMIT_BTN).click()
    assert driver.find_element(*SIGNIN_ALERT).is_displayed(), assert_msg


def test_create_new_acc(driver, wait):
    driver.get(URL_SignIN)
    wait.until(EC.element_to_be_clickable([*CREATE_ACC_LINK])).click()
    username = wait.until(EC.element_to_be_clickable([*USERNAME_FIELD]))
    username.send_keys(random_word())
    email = wait.until(EC.element_to_be_clickable([*EMAIL_FIELD]))
    email.send_keys(f'{random_word()}@gmail.com')
    password = wait.until(EC.element_to_be_clickable([*PASSWORD_FIELD]))
    password.send_keys('qsc123WDV$')
    password_r = wait.until(EC.element_to_be_clickable([*REP_PASSWORD_FIELD]))
    password_r.send_keys('qsc123WDV$')
    wait.until(EC.element_to_be_clickable([*IAM16_CHECKBOX])).click()
    wait.until(EC.element_to_be_clickable([*AGREMENT_CHECKBOX])).click()
    wait.until(EC.element_to_be_clickable([*CREATE_ACC_BTN])).click()
    error = driver.find_element(By.CLASS_NAME, 'has-error')
    assert error.is_displayed()


def test_go_to_marketplace(driver, wait, open_page):
    wait.until_not(EC.presence_of_element_located([*LOAD_DIV]))
    driver.find_element(*MARKETPLACE_BTN).click()
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    assert 'marketplace' in driver.current_url
