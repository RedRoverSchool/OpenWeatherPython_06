from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import pytest
from selenium.webdriver.common.keys import Keys

TO_IMPERIAL_BTN = By.XPATH, "//div[contains(text(),'Imperial: °F, mph')]"
TO_METRIC_BTN = By.XPATH, "//div[contains(text(),'Metric: °C, m/s')]"
INITIATIVES = By.CSS_SELECTOR, "ul[id='first-level-nav'] li:nth-child(7) a:nth-child(1)"
sections = ["Education", "Healthcare", "Open Source", "Weather stations"]
QUESTION_XPATH = "//*[@id='faq']/div[{i}]/p"
EDUCATION_SECTION_PAGE = "https://openweathermap.org/our-initiatives/student-initiative"
EDUCATION_LEARN_MORE = By.CSS_SELECTOR, ".ow-btn.round.btn-black"
LOADER_CONTAINER = By.CSS_SELECTOR, 'div.owm-loader-container > div'
SEARCH_CITY_INPUT = By.CSS_SELECTOR, "input[placeholder='Search city']"
BTN_SEARCH = By.CSS_SELECTOR, "button[class ='button-round dark']"
SEARCH_DROPDOWN_MENU = By.CLASS_NAME, 'search-dropdown-menu'
SEARCH_DROPDOWN_MENU_FIRST_CHILD = By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)'
SEARCH_DROPDOWN_MENU_FIRST_CHILD_TEXT = By.CSS_SELECTOR, '.grid-container.grid-4-5 h2'
MODULE_DOWNLOAD_OPENWEATHER_APP = By.XPATH, "//div[@class='my-5']/p"
FIRST_DAY_IN_8_DAY_FORECAST = By.CSS_SELECTOR, 'ul.day-list li:nth-child(1) span:nth-child(1)'
LIST_DAYS_IN_8_DAY_FORECAST = By.CSS_SELECTOR, 'div .day-list'
DAYS_IN_8_DAY_FORECAST = By.CSS_SELECTOR, 'div .day-list li'

WEEKDAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December')

SPACEKITS = [' ', '          ', '                    ']

APP_STORE_BRAND_LINK = By.CSS_SELECTOR, "img[src='/themes/openweathermap/assets/img/mobile_app/app-store-badge.svg']"

COOKIES_LINK_SELECTOR = By.XPATH, "//button[@type='button']"
API_LINK_SELECTOR = By.XPATH, "//div/ul/li/a[@href='/api']"
LIST_OF_WEATHER_CONDITION_CODES_LINK_SELECTOR = By.XPATH, "//a[@href='/api/one-call-3#list1']"
WEATHER_CONDITION_CODES_LINK_SELECTOR = By.XPATH, "//a[@href='/weather-conditions']"
ID_SELECTOR = By.XPATH, "//table[@class='table table-bordered'][not (position() < 2)]/tbody/tr/td[1]"
DESC_SELECTOR = By.XPATH, "//table[@class='table table-bordered'][not (position() < 2)]/tbody/tr/td[3]"
GOOGLE_PLAY_BRAND_LINK = By.CSS_SELECTOR, "img[alt='Get it on Google Play']"

API_KEY_NAME_URL = 'https://home.openweathermap.org/api_keys'
API_KEY_EDIT_SELECTOR = By.CSS_SELECTOR, "i[class='fa fa-edit']"
API_KEY_NAME_SELECTOR = By.XPATH, "//table/tbody/tr/td[2]"
API_KEY_ENTER_SELECTOR = By.CSS_SELECTOR, "input[name='edit_key_form[name]']"
SAVE_BUTTON_SELECTOR = By.CSS_SELECTOR, "button[class='button-round dark']"
TAB_API_KEYS = By.CSS_SELECTOR, '#myTab [href="/api_keys"]'
MODULE_API_KEY_CREATE = By.CSS_SELECTOR, '.col-md-4 h4'



@pytest.fixture()
def open_api_keys_page(driver, open_and_load_main_page, sign_in, wait):
    api_key_tab = driver.find_element(*TAB_API_KEYS)
    api_key_tab.click()

@pytest.fixture()
def api_key_delete_name(driver, open_api_keys_page, wait):
    wait.until(EC.element_to_be_clickable(API_KEY_EDIT_SELECTOR)).click()
    api_key_enter = wait.until(EC.element_to_be_clickable(API_KEY_ENTER_SELECTOR))
    api_key_enter.click()
    api_key_enter.send_keys(Keys.CONTROL, 'a')
    api_key_enter.send_keys(Keys.BACKSPACE)
    return api_key_enter

def get_api_key_name_before(driver, open_api_keys_page):
    return driver.find_element(*API_KEY_NAME_SELECTOR).text



def test_tc_001_01_01_verify_city_name_displayed_by_zip(driver, open_and_load_main_page, wait):
    search_city_field = driver.find_element(*SEARCH_CITY_INPUT)
    search_city_field.send_keys('66002')
    search_button = driver.find_element(*BTN_SEARCH)
    search_button.click()
    search_option = wait.until(EC.element_to_be_clickable(SEARCH_DROPDOWN_MENU_FIRST_CHILD))
    search_option.click()
    expected_city = 'Atchison, US'
    wait.until(EC.text_to_be_present_in_element(SEARCH_DROPDOWN_MENU_FIRST_CHILD_TEXT, 'Atchison'))
    displayed_city = driver.find_element(*SEARCH_DROPDOWN_MENU_FIRST_CHILD_TEXT).text
    assert displayed_city == expected_city


def test_tc_001_01_02_verify_dropdown_options_contain_valid_value(driver, open_and_load_main_page, wait):
    driver.find_element(*SEARCH_CITY_INPUT).send_keys('California')
    driver.find_element(*BTN_SEARCH).click()
    wait.until(EC.element_to_be_clickable(SEARCH_DROPDOWN_MENU))
    dropdown_list = driver.find_element(*SEARCH_DROPDOWN_MENU)
    for i in dropdown_list.find_elements(By.CSS_SELECTOR, 'li'):
        assert 'California' in i.text, 'Not all search suggestions in the drop-down list contain "California"'


# TC_001.02.04_01 | Main page> Search city widget > Verify the buttons for metric and imperial are visible and clickable
def test_tc_001_02_04_01_switch_toggle_buttons(driver, open_and_load_main_page, wait):
    # switch the temperature system to imperial
    imperial_button = driver.find_element(*TO_IMPERIAL_BTN)
    imperial_button.click()
    metric_button = driver.find_element(*TO_METRIC_BTN)
    metric_button.click()
    # Verify that toggle buttons are displayed and clickable
    assert all(button.is_displayed() and button.is_enabled() for button in [metric_button, imperial_button])


def test_tc_003_09_01_the_module_title_display(driver, open_and_load_main_page, wait):
    expected_module_title = "Download OpenWeather app"
    module_download_openweather_app = driver.find_element(*MODULE_DOWNLOAD_OPENWEATHER_APP)
    module_download_openweather_app.location_once_scrolled_into_view
    actual_module_title = module_download_openweather_app.text
    assert actual_module_title == expected_module_title


def test_TC_001_04_03_verify_in_day_list_first_element_day_by_week(driver, open_and_load_main_page):
    day_by_weak = driver.find_element(*FIRST_DAY_IN_8_DAY_FORECAST).text[:3]
    day_by_computer = datetime.now().weekday()
    today = WEEKDAYS[day_by_computer]
    assert day_by_weak == f'{today}'


def test_tc_001_04_05_main_page_search_city_widget_8_day_forecast_first_element_number_day(driver,
                                                                                           open_and_load_main_page):
    number_day = driver.find_element(*FIRST_DAY_IN_8_DAY_FORECAST).text[-2:]
    if number_day.startswith('0'):
        number_day = number_day[1:]
    number_day_by_computer = datetime.now().day
    assert number_day == f'{number_day_by_computer}'


def get_section_locator(section):
    return (By.XPATH, f"//span[contains(text(), '{section}')]")


@pytest.mark.parametrize("section", sections)
def test_010_01_01_01_verify_sections(driver, open_and_load_main_page, section):
    our_initiatives_link = driver.find_element(*INITIATIVES)
    our_initiatives_link.click()
    section_locator = get_section_locator(section)
    section_element = driver.find_element(*section_locator)
    assert section_element.is_displayed(), f"Section '{section}' not found on the page"


def test_TC_001_04_04_verify_in_day_list_first_element_month(driver, open_and_load_main_page):
    month = driver.find_element(*FIRST_DAY_IN_8_DAY_FORECAST).text[5:-3]
    month_by_computer = datetime.now().month
    current_month = MONTHS[month_by_computer - 1]
    assert month == f'{current_month}'


def test_tc_003_09_02_app_store_brand_link_display(driver, open_and_load_main_page):
    driver.find_element(*MODULE_DOWNLOAD_OPENWEATHER_APP).location_once_scrolled_into_view
    app_store_brand_link = driver.find_element(*APP_STORE_BRAND_LINK)
    assert app_store_brand_link.is_displayed(), "The brand-link for Download on the App Store is not displaying"


def test_tc_003_09_03_app_store_brand_link_clickable(driver, open_and_load_main_page):
    initial_page_number = len(driver.window_handles)
    driver.find_element(*MODULE_DOWNLOAD_OPENWEATHER_APP).location_once_scrolled_into_view
    app_store_brand_link = driver.find_element(*APP_STORE_BRAND_LINK)
    app_store_brand_link.click()
    actual_page_number = len(driver.window_handles)
    assert actual_page_number == initial_page_number + 1, \
        "The new web tab does not opened after click App Store brand-link's"


def test_tc_001_12_07_verify_that_codes_and_descriptions_are_visible_for_each_weather_condition_group(driver,
                                                                                                      open_and_load_main_page,
                                                                                                      wait):
    wait.until(EC.element_to_be_clickable(COOKIES_LINK_SELECTOR)).click()
    wait.until(EC.element_to_be_clickable(API_LINK_SELECTOR)).click()
    wait.until(EC.element_to_be_clickable(LIST_OF_WEATHER_CONDITION_CODES_LINK_SELECTOR)).click()
    wait.until(EC.element_to_be_clickable(WEATHER_CONDITION_CODES_LINK_SELECTOR)).click()
    ids_list = driver.find_elements(*ID_SELECTOR)
    descs_list = driver.find_elements(*DESC_SELECTOR)
    total_list = ids_list + descs_list
    for item in total_list:
        assert item.is_displayed()


def test_tc_017_03_10_verify_the_api_key_name_on_the_api_keys_tab_does_not_change_if_the_input_is_empty(driver,
                                                                                                        open_and_load_main_page,
                                                                                                        wait, sign_in):
    driver.get(API_KEY_NAME_URL)
    wait.until(EC.element_to_be_clickable(API_KEY_EDIT_SELECTOR)).click()
    api_key_name_before = driver.find_element(*API_KEY_NAME_SELECTOR).text
    api_key_enter = wait.until(EC.element_to_be_clickable(API_KEY_ENTER_SELECTOR))
    api_key_enter.click()
    api_key_enter.send_keys(Keys.CONTROL, 'a')
    api_key_enter.send_keys(Keys.BACKSPACE)
    driver.find_element(*SAVE_BUTTON_SELECTOR).click()
    api_key_name_after = driver.find_element(*API_KEY_NAME_SELECTOR).text
    assert api_key_name_after == api_key_name_before


# TC_010.01_02_02 | Our Initiatives > Verify the functionality of 'Our Initiatives' section
def test_010_01_02_02_functionality(driver, open_and_load_main_page, wait):
    initiatives_link = driver.find_element(*INITIATIVES)
    initiatives_link.click()
    education_learn_more = wait.until(EC.element_to_be_clickable(EDUCATION_LEARN_MORE))
    driver.execute_script("window.scrollBy(0, 500);")
    ActionChains(driver).move_to_element(education_learn_more).click(education_learn_more).perform()
    assert driver.current_url == EDUCATION_SECTION_PAGE


def test_tc_003_09_04_google_play_brand_link_clickable(driver, open_and_load_main_page):
    initial_page_number = len(driver.window_handles)
    driver.find_element(*MODULE_DOWNLOAD_OPENWEATHER_APP).location_once_scrolled_into_view
    google_play_brand_link = driver.find_element(*GOOGLE_PLAY_BRAND_LINK)
    google_play_brand_link.click()
    actual_page_number = len(driver.window_handles)
    assert actual_page_number == initial_page_number + 1, \
        "The new web tab does not opened after click Google Play brand-link's"


def test_tc_003_09_04_google_play_brand_link_display(driver, open_and_load_main_page):
    driver.find_element(*MODULE_DOWNLOAD_OPENWEATHER_APP).location_once_scrolled_into_view
    google_play_brand_link = driver.find_element(*GOOGLE_PLAY_BRAND_LINK)
    assert google_play_brand_link.is_displayed(), "Google Play brand-link is not displaying"


def test_tc_017_04_01_module_create_api_key_is_visible(driver, open_api_keys_page, wait):
    module_create_api_key = driver.find_element(*MODULE_API_KEY_CREATE)
    assert module_create_api_key.is_displayed(), "module with title “Create key“ does not visible"


def test_TC_001_04_06_verify_in_day_list_days_of_the_week(driver, open_and_load_main_page):
    driver.find_element(*LIST_DAYS_IN_8_DAY_FORECAST).location_once_scrolled_into_view
    days_by_page = []
    days = driver.find_elements(*DAYS_IN_8_DAY_FORECAST)
    for day in days:
        days_by_page.append(day.text[:3])
    number_day = datetime.now().weekday()
    days_by_computer = WEEKDAYS[number_day:] + WEEKDAYS[:number_day] + WEEKDAYS[(number_day):(number_day + 1):]
    assert days_by_page == days_by_computer


def test_010_02_08_accessibility_of_question_headings(driver, open_and_load_main_page):
    driver.get(EDUCATION_SECTION_PAGE)
    question_headings = []
    for i in range(1, 10):

        question_heading = driver.find_element(By.XPATH, QUESTION_XPATH.format(i=i))
        question_headings.append(question_heading)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    for heading in question_headings:
        assert heading.is_displayed(), "Error: FAQ header not displayed"


@pytest.mark.parametrize('spacekit', SPACEKITS)
def test_tc_017_03_11_verify_the_api_key_name_does_not_change_if_the_input_consists_of_spaces(driver, spacekit, api_key_delete_name, wait):
    api_key_delete_name.send_keys(spacekit)
    driver.find_element(*SAVE_BUTTON_SELECTOR).click()
    api_key_name_before = get_api_key_name_before(driver, open_api_keys_page)
    api_key_name_after = driver.find_element(*API_KEY_NAME_SELECTOR).text
    assert api_key_name_after == api_key_name_before
