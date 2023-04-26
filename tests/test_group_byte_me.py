import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://openweathermap.org/'


@pytest.fixture()
def open_page(driver):
    driver.get(URL)
    assert driver.current_url == URL, "--------Wrong URL-----------"


def test_go_to_sign_in_page(driver, open_page):
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div'))
    )
    sign_button = driver.find_element(By.CSS_SELECTOR, '.user-li>a')
    sign_button.click()
    assert "sign_in" in driver.current_url, "--------Wrong URL-----------"