import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://openweathermap.org/"
load_div = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
selector_dashboard = (By.XPATH, "//h1[contains(text(),'Weather dashboard')]")
selector_api = (By.XPATH, "//h1[contains(text(),'Weather API')]")
tab_desk_api = (By.CSS_SELECTOR, '#desktop-menu a[href="/api"]')
tab_desc_dashboard_bt = (By.XPATH, "//div[@id='desktop-menu']//a[@href='/weather-dashboard']")
selector_marketplace_tab = (By.XPATH, '//div[@id="desktop-menu"]//li[4]/a')

def test_open_page(driver):
    driver.get('https://openweathermap.org/')
    driver.maximize_window()
    assert 'openweathermap' in driver.current_url


def test_check_page_title(driver):
    # function checks page title
    driver.get('https://openweathermap.org')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


def test_checkout_menu_tab_api(driver):
    try:
        driver.get(URL)
        wait = WebDriverWait(driver, 15)
        wait.until_not(EC.presence_of_element_located(load_div))
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")

    try:
        tab_b_api = WebDriverWait(driver, 25).until(EC.element_to_be_clickable(tab_desk_api))
        tab_b_api.click()
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")
    try:
        exp_alert = 'Weather API'
        disp_alert = WebDriverWait(driver, 25).until(EC.presence_of_element_located(selector_api))
        disp_alert_text = disp_alert.text
        assert exp_alert == disp_alert_text
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")


def test_checkout_menu_tab_dashboard(driver):
    try:
        driver.get(URL)
        wait = WebDriverWait(driver, 15)
        wait.until_not(EC.presence_of_element_located(load_div))
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")

    try:
        tab_dashboard_bt = WebDriverWait(driver, 25).until(EC.element_to_be_clickable(tab_desc_dashboard_bt))
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

def test_home_button(driver):
    #  testing going back to home from Guide page
    try:
        driver.get('https://openweathermap.org')
        WebDriverWait(driver, 50).until_not(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
        tab_name_guide = WebDriverWait(driver, 45).until(EC.element_to_be_clickable(
            (By.XPATH, '//div[@id="desktop-menu"]//a[contains(@href, "guide")]')))
        tab_name_guide.click()
        tab_home_link = WebDriverWait(driver, 45).until(EC.element_to_be_clickable(
            (By.XPATH, '//div[@class="col-sm-5"]/ol/li/a')))
        tab_home_link.click()
        assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")

def test_guide_button(driver):
    #  testing Guide tab button
    try:
        driver.get('https://openweathermap.org')
        WebDriverWait(driver, 50).until_not(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
        tab_name_guide = WebDriverWait(driver, 45).until(EC.element_to_be_clickable(
            (By.XPATH, '//div[@id="desktop-menu"]//a[contains(@href, "guide")]')))
        tab_name_guide.click()
        assert driver.title == 'OpenWeatherMap API guide - OpenWeatherMap'
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")

def test_marketplace_page_link(driver):
    try:
        driver.get(URL)
        WebDriverWait(driver, 15).until_not(EC.presence_of_element_located(load_div))
        marketplace_tab = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
            (selector_marketplace_tab)))
        marketplace_tab.click()
        expected_url ='https://home.openweathermap.org/marketplace'
        assert expected_url
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")


