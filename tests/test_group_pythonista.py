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
