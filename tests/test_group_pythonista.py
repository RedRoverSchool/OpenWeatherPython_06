from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

URL_API = 'https://openweathermap.org/api'
URL_WEATHER_MODEL = 'https://openweathermap.org/technology'
URL_WEATHER_STATIONS = 'https://openweathermap.org/stations'

URL_FORCAST30 = 'https://openweathermap.org/api/forecast30'
TITLE_FORCAST30 = (By.CSS_SELECTOR, '.col-sm-7 .breadcrumb-title')
LINK_HOW_TO_MAKE = (By.CSS_SELECTOR, "a[href$='geo-year']")
TITLE_HOW_TO_MAKE = (By.XPATH, '//*[@id="geo-year"]/h3')

URL_ROAD_RISK = 'https://openweathermap.org/api/road-risk'
SECTION_R_CONCEPTS = (By.XPATH, "//*[@id='concept']")

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
API_LINK = (By.XPATH, '//div[@id="desktop-menu"]//a[contains(@href, "api")]')


def test_TC_003_11_01_verify_the_copyright_information_is_present_on_the_page(driver, open_and_load_main_page, wait):
    cookie_close = driver.find_element(*BTN_COOKIES)
    driver.execute_script("arguments[0].click();", cookie_close)
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


def test_TC_005_04_02_professional_collection_section_is_presented(driver, wait):
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


def test_TC_005_06_1_visibility_climatic_forecast_30_days_page_title(driver):
    driver.get(URL_FORCAST30)
    title_page = driver.find_element(*TITLE_FORCAST30).text
    assert title_page == 'Climate forecast for 30 days', 'The title of the page does not match the expected value'


def test_TC_005_06_02_redirect_to_the_how_to_make_an_API_call_section_of_the_page(driver):
    driver.get(URL_FORCAST30)
    driver.find_element(*LINK_HOW_TO_MAKE).click()
    new_page_title = driver.find_element(*TITLE_HOW_TO_MAKE)
    assert new_page_title.is_displayed(), 'The title of the page does not match the expected value'


def test_TC_003_11_02_verify_the_copyright_information_is_present_on_the_site_page(driver):
    driver.get(URL_API)
    expected_footer_text = "© 2012 — 2023 OpenWeather"
    footer = driver.find_element(*FOOTER_COPYRIGHT)
    assert footer.is_displayed() and expected_footer_text in footer.text, \
        "The footer is not displayed or does not contain the expected text"


def test_TC_005_08_03_road_risk_api_visibility_of_road_risk_api_concept_section(driver):
    driver.get(URL_ROAD_RISK)
    section_road_risk = driver.find_element(*SECTION_R_CONCEPTS)
    assert section_road_risk.is_displayed(), 'Section - NOT FOUND'


def test_TC_002_01_08_header_logo_verify_logo_redirects_from_weather_model_page_to_main_page(driver):
    driver.get(URL_WEATHER_MODEL)
    driver.find_element(*LOGO).click()
    assert driver.current_url == 'https://openweathermap.org/'


def test_TC_002_01_10_header_logo_verify_logo_redirects_from_weather_stations_page_to_main_page(driver):
    driver.get(URL_WEATHER_STATIONS)
    driver.find_element(*LOGO).click()
    assert driver.current_url == 'https://openweathermap.org/'


def test_TC_002_03_16_api_link_redirects_to_api_page(driver, open_and_load_main_page, wait):
    wait.until(EC.element_to_be_clickable(API_LINK))
    driver.find_element(*API_LINK).click()
    assert driver.current_url == URL_API
    