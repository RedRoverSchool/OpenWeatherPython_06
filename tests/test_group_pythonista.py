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
footer_panel = (By.XPATH, '//*[@id="stick-footer-panel"]/div')
btn_allow_all = (By.XPATH, '//*[@id="stick-footer-panel"]/div/div/div/div/div/button')
btn_about_us = (By.CSS_SELECTOR, 'a[href*="/about-us"]')
text_openweather = (By.XPATH, '//div/h1/span["orange -text"]')


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
        expected_url = 'https://home.openweathermap.org/marketplace'
        assert expected_url
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")


def test_check_about(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    wait.until(EC.element_to_be_clickable(footer_panel))
    driver.find_element(*btn_allow_all).click()
    driver.find_element(*btn_about_us).click()
    title_about_us = driver.find_element(*text_openweather).text
    assert title_about_us == 'OpenWeather'

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

FOOTER_PANEL = (By.XPATH, '//*[@id="stick-footer-panel"]/div')
BTN_ALLOW_ALL = (By.CLASS_NAME, "stick-footer-panel__link")
FOOTER_COPYRIGHT = (By.XPATH, "//div[@class='horizontal-section my-5']/div[1]")
DASHBOARD_LINK = (By.XPATH, '//div[@id="desktop-menu"]//a[contains(@href, "/weather-dashboard")]')
BTN_DASHBOARD = (By.CSS_SELECTOR, "#desktop-menu [href$=-dashboard]")
TITLE_HOW_TO_START = (By.XPATH, "//div/h2[contains(text(),'How to Start')]")
PROFESSIONAL_COLLESTION_TITLE = (By.XPATH, "//section[@id='pro']/h2")
CURRENT_FORECAST_COLLECTION_LINK = (By.XPATH, "//section[@id='pro']//p/a[contains(@href, '#current')]")
LOGO = (By.CSS_SELECTOR, ".logo > a > img")
BTN_TRY_THE_DASHBOARD_2 = (By.XPATH, "//div[6]//a[text()='Try the Dashboard']")
BTN_COOKIES = (By.CLASS_NAME, "stick-footer-panel__link")
ALERT_PANEL_SINGIN = (By.CSS_SELECTOR, '.col-md-6 .panel-heading')
HISTORICAL_WEATHER_DATA_COLLECTION_LINK = (By.XPATH, "//section[@id='pro']//p/a[contains(@href, '#history')]")
WEATHER_MAPS_COLLECTION_LINK = (By.XPATH, "//section[@id='pro']//p/a[contains(@href, '#maps')]")

URL_API = 'https://openweathermap.org/api'

def test_TC_003_11_01_verify_the_copyright_information_is_present_on_the_page(driver, open_and_load_main_page, wait):
    wait.until(EC.element_to_be_clickable(FOOTER_PANEL))
    driver.find_element(*BTN_ALLOW_ALL).click()
    expected_footer_text = "© 2012 — 2023 OpenWeather"
    footer = driver.find_element(*FOOTER_COPYRIGHT)
    assert footer.is_displayed() and expected_footer_text in footer.text, \
        "The footer is not displayed or does not contain the expected text"


def test_TC_002_03_05_dashboard_is_visible_and_clickable(driver, open_and_load_main_page, wait):
    wait.until(EC.element_to_be_clickable(DASHBOARD_LINK))
    dashboard_tab = driver.find_element(*DASHBOARD_LINK)
    expected_dashboard_label = 'Dashboard'
    assert dashboard_tab.is_displayed() and dashboard_tab.is_enabled() and expected_dashboard_label in dashboard_tab.text


def test_TC_006_02_01_verify_display_of_how_to_start_section(driver, open_and_load_main_page, wait):
    driver.find_element(*BTN_DASHBOARD).click()
    section = driver.find_element(*TITLE_HOW_TO_START)
    assert section.is_displayed(), "Section not found"


def test_TC_002_03_06_dashboard_link_opens_correct_page(driver, open_and_load_main_page, wait):
    wait.until(EC.element_to_be_clickable(DASHBOARD_LINK))
    dashboard_tab = driver.find_element(*DASHBOARD_LINK)
    dashboard_tab.click()
    expected_url = 'https://openweathermap.org/weather-dashboard'
    assert driver.current_url == expected_url


def test_TC_005_04_02_Professional_collection_section_is_presented(driver, wait):
    driver.get(URL_API)
    wait.until(EC.presence_of_element_located(PROFESSIONAL_COLLESTION_TITLE))
    proffecional_collection_title = driver.find_element(*PROFESSIONAL_COLLESTION_TITLE)
    expected_title = 'Professional collections'
    assert expected_title in proffecional_collection_title.text


def test_TC_002_01_04_header_logo_verify_logo_redirects_from_dashboard_page_to_main_page(driver):
    driver.get('https://openweathermap.org/weather-dashboard/')
    driver.find_element(*LOGO).click()
    assert driver.current_url == 'https://openweathermap.org/'


def test_TC_006_02_03_weather_dashboard_verify_the_transition_to_another_page(driver, open_and_load_main_page, wait):
    driver.find_element(*BTN_DASHBOARD).click()
    cookie_close = driver.find_element(*BTN_COOKIES)
    driver.execute_script("arguments[0].click();", cookie_close)
    driver.find_element(*BTN_TRY_THE_DASHBOARD_2).click()
    driver.switch_to.window(driver.window_handles[1])
    alert_mms = driver.find_element(*ALERT_PANEL_SINGIN)
    assert alert_mms.is_displayed(), 'WELCOME EVENTS'

def test_TC_005_04_03_professional_collection_historical_weather_is_visible_and_clickable(driver, wait):
    driver.get(URL_API)
    wait.until(EC.presence_of_element_located(HISTORICAL_WEATHER_DATA_COLLECTION_LINK))
    historical_link = driver.find_element(*HISTORICAL_WEATHER_DATA_COLLECTION_LINK)
    expected_historical_label = 'Historical weather data collection'
    assert historical_link.is_displayed() and historical_link.is_enabled() and expected_historical_label in historical_link.text

def test_TC_005_04_04_professional_collection_weather_maps_link_is_visible_and_clickable(driver, wait):
    driver.get(URL_API)
    wait.until(EC.presence_of_element_located(WEATHER_MAPS_COLLECTION_LINK))
    expected_weather_maps_label = 'Weather Maps collection'
    weather_maps_link = driver.find_element(*WEATHER_MAPS_COLLECTION_LINK)
    assert weather_maps_link.is_enabled() and weather_maps_link.is_displayed() and expected_weather_maps_label in weather_maps_link.text

def test_TC_005_04_05_professional_collection_current_and_forecast_is_visible_and_clickable(driver, wait):
    driver.get(URL_API)
    wait.until(EC.presence_of_element_located(CURRENT_FORECAST_COLLECTION_LINK))
    current_forecast_link = driver.find_element(*CURRENT_FORECAST_COLLECTION_LINK)
    exp_current_forecast = 'Current & Forecasts collection'
    assert current_forecast_link.is_enabled() and current_forecast_link.is_displayed() and exp_current_forecast in current_forecast_link.text