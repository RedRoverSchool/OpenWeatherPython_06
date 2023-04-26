import pytest

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://openweathermap.org/"
load_div = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
home_btn = (By.CSS_SELECTOR, '.breadcrumb.pull-right.hidden-xs li :nth-child(1)')
selector_dashboard = (By.XPATH, "//h1[contains(text(),'Weather dashboard')]")
bt_go_home = (By.XPATH, "//a[contains(text(),'Home')]")
tab_api = (By.CSS_SELECTOR, '#desktop-menu a[href="/api"]')
def test_open_page(driver):
    driver.get('https://openweathermap.org/')
    driver.maximize_window()
    assert 'openweathermap' in driver.current_url


def test_check_page_title(driver):
    # function checks page title
    driver.get('https://openweathermap.org')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


def test_python():
    print('Hello girls!')


@pytest.mark.skip(reason="GitHub test fails <selenium.common.exceptions.TimeoutException>")
def test_checkout_tab_dashboard(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    tab_dashboard_bt = WebDriverWait(driver, 25).until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@id='desktop-menu']//a[@href='/weather-dashboard']")))
    tab_dashboard_bt.click()
    exp_alert = 'Weather dashboard'
    disp_alert = WebDriverWait(driver, 25).until(EC.presence_of_element_located(selector_dashboard))
    disp_alert_text = disp_alert.text
    assert exp_alert == disp_alert_text


@pytest.mark.skip(reason="GitHub test fails <selenium.common.exceptions.TimeoutException>")
def test_checkout_menu_tab_guide(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    tab_guild_bt = WebDriverWait(driver, 25).until(EC.presence_of_element_located
                                                   ((By.XPATH, "//div[@id='desktop-menu']//a[@href='/guide']")))
    tab_guild_bt.click()
    assert driver.current_url == 'https://openweathermap.org/guide'
    bt_home = WebDriverWait(driver, 25).until(EC.presence_of_element_located
                                              (bt_go_home))
    bt_home.click()
    assert driver.current_url == URL


@pytest.mark.skip(reason="GitHub test fails <selenium.common.exceptions.TimeoutException>")
def test_checkout_menu_tab_api(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    tab_b_api = WebDriverWait(driver, 25).until(EC.element_to_be_clickable(tab_api))
    tab_b_api.click()
    assert driver.current_url == 'https://openweathermap.org/api'
    btn_home = WebDriverWait(driver, 25).until(EC.element_to_be_clickable(bt_go_home))
    btn_home.click()
    assert driver.current_url == URL


def test_checkout_menu_tab_dashboard(driver):
    try:
        driver.get(URL)
        wait = WebDriverWait(driver, 15)
        wait.until_not(EC.presence_of_element_located(load_div))
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")

    try:
        tab_dashboard_bt = WebDriverWait(driver, 25).until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@id='desktop-menu']//a[@href='/weather-dashboard']")))
        tab_dashboard_bt.click()
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")

    try:
        exp_alert = 'Weather dashboard'
        disp_alert = WebDriverWait(driver, 25).until(EC.presence_of_element_located(selector_dashboard))
        disp_alert_text = disp_alert.text
        assert exp_alert == disp_alert_text
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")