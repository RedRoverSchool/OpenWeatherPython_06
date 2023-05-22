from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


URL_SOLAR_API = "https://openweathermap.org/api/solar-energy-prediction"
CITIES = ['New York', 'Los Angeles', 'Paris']
SEARCH_CITY_FIELD_LOCATOR = (By.CSS_SELECTOR, "input[placeholder='Search city']")
SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button[class ='button-round dark']")
SEARCH_1ST_OPTION_LOCATOR = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:first-child span:first-child')
C_TEMP_LOCATOR = (By.CSS_SELECTOR, '.switch-container .option:nth-child(2)')
LINE_IN_8_DAYS_FORECAST_LOCATOR = (By.XPATH, "//div[@class='day-list-values']/div/span[contains(text(), '°C')]")
product_concept_title_locator = (By.CSS_SELECTOR, "#concept h2")
subscription_module_button = (By.CSS_SELECTOR, ".inner-footer-container div:first-of-type "
                                               ".footer-section:nth-child(2) p.section-heading")
QUALITY_INFO_PAGE = "https://openweathermap.org/accuracy-and-quality"
NWP_MODEL = (By.CSS_SELECTOR, ".col-sm-12 > ul:first-of-type")
CONTINUE_TO_PAYMENT_BUTTON = (By.CSS_SELECTOR, 'input[value ="Continue to payment"]')
CANT_BE_BLANK = (By.CSS_SELECTOR, '.help-block')
EXPECTED_NUMBER_OF_FIELDS = 7
URL_SUBSCRIPTION_BASE = 'https://home.openweathermap.org/subscriptions/unauth_subscribe/onecall_30/base'
MAIN_LOGO = (By.CSS_SELECTOR, 'img[src="/themes/openweathermap/assets/img/logo_white_cropped.png"]')
OUR_INITIATIVES_PAGE = 'https://openweathermap.org/our-initiatives'
MAIN_PAGE = 'https://openweathermap.org/'
HOW_TO_GET_ACCESS_LINK_LOCATOR = (By.XPATH, '//a[@href="#how"]')
HOW_TO_GET_ACCESS_TITLE_LOCATOR = (By.CSS_SELECTOR, "#how h2")
GUIDE_PAGE = "https://openweathermap.org/guide"
HISTORICAL_COLLECTION_MODULE = (By.CSS_SELECTOR, ".col-sm-12 ol ul:nth-of-type(2)")
LINK_HISTORICAL_ARCHIVE = (By.PARTIAL_LINK_TEXT, "archive")
CLICK_ALLOW_IN_STICK_FOOTER = (By.CLASS_NAME, 'stick-footer-panel__link')
URL_HISTORY_BULK = "https://openweathermap.org/history-bulk"



@pytest.mark.parametrize('city', CITIES)
def test_TC_001_04_01_visibility_of_8_lines_in_8_day_forecast_block(driver, open_and_load_main_page, city):
    """Checking if all 8 lines are visible in 8-day forecast block"""
    search_city_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SEARCH_CITY_FIELD_LOCATOR))
    search_city_field.send_keys(city)
    search_button = driver.find_element(*SEARCH_BUTTON_LOCATOR)
    search_button.click()
    search_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SEARCH_1ST_OPTION_LOCATOR))
    search_option.click()
    c_temp = driver.find_element(*C_TEMP_LOCATOR)
    c_temp.click()
    lines = driver.find_elements(*LINE_IN_8_DAYS_FORECAST_LOCATOR)
    for line in lines:
        assert line.is_displayed()


def test_TC_005_10_02_visibility_of_Product_concept_article_title(driver):
    driver.get(URL_SOLAR_API)
    product_concept_title = driver.find_element(*product_concept_title_locator)
    assert product_concept_title.is_displayed()



def test_TC_003_05_01_subscription_module_title_displayed(driver, open_and_load_main_page):
    subscription_title = driver.find_element(*subscription_module_button)
    driver.execute_script("arguments[0].click();", subscription_title)
    assert subscription_title.is_displayed()



def test_001_017_01_visibility_of_nwp_block(driver):
    driver.get(QUALITY_INFO_PAGE)
    nwp = driver.find_element(*NWP_MODEL)
    assert nwp.is_displayed()


def test_TC_018_01_02_Verify_error_messages_for_empty_required_fields(driver):
    driver.get(URL_SUBSCRIPTION_BASE)
    driver.find_element(*CONTINUE_TO_PAYMENT_BUTTON).click()
    error_messages = driver.find_elements(*CANT_BE_BLANK)
    checks = 0
    for i in error_messages:
        assert i.is_displayed()
        checks += 1
    assert checks == EXPECTED_NUMBER_OF_FIELDS

def test_002_01_11_verify_main_logo(driver):
    driver.get(OUR_INITIATIVES_PAGE)
    m_logo = driver.find_element(*MAIN_LOGO)
    m_logo.click()
    response = requests.get(MAIN_PAGE)
    assert response.status_code == 200


def test_TC_005_10_03_correct_redirection_for_how_to_get_access_link(driver):
    """Checking for correct redirection when clicking on How to get access link from the side menu"""
    driver.get(URL_SOLAR_API)
    how_to_get_access_link = driver.find_element(*HOW_TO_GET_ACCESS_LINK_LOCATOR)
    how_to_get_access_link.click()
    how_to_get_access_title = driver.find_element(*HOW_TO_GET_ACCESS_TITLE_LOCATOR)
    assert how_to_get_access_title.is_displayed()



def test_TC_004_08_01_historical_collection_block_visibility(driver):
    driver.get(GUIDE_PAGE)
    historical_collection = driver.find_element(*HISTORICAL_COLLECTION_MODULE)
    driver.execute_script("arguments[0].scrollIntoView(true);", historical_collection)
    assert historical_collection.is_displayed(), "The Historical Weather collection is not displaying"


def test_TC_004_08_02_link_to_history_archive_is_clickable(driver):
    driver.get(GUIDE_PAGE)
    archive_link = driver.find_element(*LINK_HISTORICAL_ARCHIVE)
    actions = ActionChains(driver)
    actions.move_to_element(archive_link).perform()
    assert archive_link.is_enabled(), "The link is not clickable"



def test_TC_004_08_03_historical_collection_link_redirects_correctly(driver):
    driver.get(GUIDE_PAGE)
    driver.find_element(*CLICK_ALLOW_IN_STICK_FOOTER).click()
    driver.find_element(*LINK_HISTORICAL_ARCHIVE).click()
    assert driver.current_url == URL_HISTORY_BULK
