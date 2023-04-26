import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://openweathermap.org/'
SIGNIN_BTN = (By.CLASS_NAME, 'user-li')


@pytest.fixture()
def open_page(driver):
    driver.get(URL)
    assert driver.current_url == URL, "--------Wrong URL-----------"


def test_go_to_sign_in_page(driver, open_page):
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div'))
    )
    wait.until(EC.element_to_be_clickable([*SIGNIN_BTN])).click()
    assert "sign_in" in driver.current_url, "--------Wrong URL-----------"
