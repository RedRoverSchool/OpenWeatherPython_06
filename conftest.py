import os
import shutil
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_data.credentials import credentials

URL = 'https://openweathermap.org/'

load_div = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
email_input = (By.CSS_SELECTOR, '#user_email')
password_input = (By.CSS_SELECTOR, '#user_password')
submit_button = (By.CSS_SELECTOR, "input[value='Submit']")
sign_in_link = (By.CSS_SELECTOR, '.user-li a')
@pytest.fixture(scope='function')
def driver():
    print('\nstart browser...')
    chrome_options = Options()
    if 'CI' in os.environ:
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.set_window_size(1382, 754)
    else:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
    yield driver
    print('\nquit browser...')
    driver.quit()

@pytest.fixture()
def open_and_load_main_page(driver, wait):
    driver.get(URL)
    wait.until_not(EC.presence_of_element_located(load_div))


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, 15)
    yield wait

@pytest.fixture()
def sign_in(driver):
    driver.find_element(*sign_in_link).click()
    driver.find_element(*email_input).send_keys(credentials["email"])
    driver.find_element(*password_input).send_keys(credentials["password"])
    driver.find_element(*submit_button).click()


def pytest_runtest_makereport(item, call):
    if call.when == 'call':
        # test_name = item.name
        if call.excinfo is not None:
            # status = 'failed'
            # logger.error(f'{status} - {test_name}. Reason: {str(call.excinfo)}')
            try:
                driver = item.funcargs['driver']
                driver.save_screenshot('allure-results/screenshot.png')
                allure.attach.file('allure-results/screenshot.png', name='Screenshot',
                                   attachment_type=allure.attachment_type.PNG)
                allure.attach(driver.page_source, name="HTML source", attachment_type=allure.attachment_type.HTML)
            except Exception as e:
                print(f"Failed to take screenshot: {e}")

def pytest_sessionstart(session):
    allure_report_dir = "allure-results"
    if os.path.exists(allure_report_dir):
        for file_name in os.listdir(allure_report_dir):
            file_path = os.path.join(allure_report_dir, file_name)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
