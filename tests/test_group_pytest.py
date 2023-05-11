import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


BUTTON_UNDER_HOW_TO_START = (By.XPATH, '(//a[@class="btn_like btn-orange owm-block-mainpage__btn"])[2]')
DASHBOARD_HEADER_LINK = (By.XPATH, '//div[@id="desktop-menu"]//a[.="Dashboard"]')
WEATHER_DASHBOARD_HOME_LINK = (By.XPATH, '//a[.="Home"]')
HOW_TO_START_SIGN_UP_LINK = (By.XPATH, '//b[.="Sign up"]')
HOW_TO_START_OPENWEATHER_USERNAME_AND_PASSWORD_LINK = (By.XPATH, '//a[.="OpenWeather username and password"]')
HOW_TO_START_GO_TO_THE_DASHBOARD_LINK = (By.XPATH, '//b[.="Go to the Dashboard"]')
HOW_TO_START_EVENTS_SECTION_LINK = (By.XPATH, '//a[contains(text(), "Events")]')
HOW_TO_START_GO_TO_THE_NEW_TRIGGER_SECTION_LINK = (By.XPATH, '//b[contains(text(), "New trigger")]')
HOW_TO_START_HERE_LINK = (By.XPATH, '//a[.="here"]')
HOW_TO_START_DETAILED_USER_MANUAL_LINK = (By.XPATH, '//b[.="detailed user manual"]')
HEADER_API_LINK = (By.XPATH, '//div[@id="desktop-menu"]//a[.="API"]')
HOME_LINK = (By.XPATH, '//ol//a[.="Home"]')
LIST_OF_WEATHER_CONDITION_CODES_LINK = (By.XPATH, '//a[.="List of weather condition codes"]')
WEATHER_CONDITION_CODES_LINK = (By.XPATH, '//a[.="weather condition codes"]')
GROUP_6XX_SNOW_LINK = (By.XPATH, '//h3[.="Group 6xx: Snow"]')
GROUP_5XX_RAIN_ROWS_LINK = (By.XPATH, '//h3[.="Group 5xx: Rain"]/../following-sibling::tbody/tr')
COOKIES_ALLOW_ALL_BUTTON_LINK = (By.XPATH, '//button[.="Allow all"]')
HEADER_PRICING_LINK = (By.XPATH, '//div[@id="desktop-menu"]//a[.="Pricing"]')
PRICING_SUBSCRIBE_TO_ONE_CALL_BY_CALL_BUTTON = (By.XPATH, '//a[.="Subscribe to One Call by Call"]')
PRICING_PAGE_SECTIONS_LOCATOR = ()
sections = ['onecall', 'current', 'alerts', 'history', 'historyspecial', 'offers']
URL_WEATHER_CONDITION = 'https://openweathermap.org/weather-conditions'
WEATHER_ICONS = (By.XPATH, '//a[.="Weather icons"]')
ICONS_FOR_DAYTIME = (By.XPATH, '//td[contains(text(), "d.png")]')


@pytest.fixture()
def open_weather_condition_page(driver, wait):
    driver.get(URL_WEATHER_CONDITION)
    wait.until(EC.element_to_be_clickable(WEATHER_ICONS))


def test_tc_006_02_02_verify_how_to_start_block_7_links_are_visible(driver, open_and_load_main_page, wait):
    driver.find_element(*DASHBOARD_HEADER_LINK).click()
    wait.until(EC.element_to_be_clickable(WEATHER_DASHBOARD_HOME_LINK))
    how_to_start_block = driver.find_element(*BUTTON_UNDER_HOW_TO_START)
    actions = ActionChains(driver)
    actions.move_to_element(how_to_start_block).perform()
    list_of_links = [driver.find_element(*HOW_TO_START_SIGN_UP_LINK),
                     driver.find_element(*HOW_TO_START_OPENWEATHER_USERNAME_AND_PASSWORD_LINK),
                     driver.find_element(*HOW_TO_START_GO_TO_THE_DASHBOARD_LINK),
                     driver.find_element(*HOW_TO_START_EVENTS_SECTION_LINK),
                     driver.find_element(*HOW_TO_START_GO_TO_THE_NEW_TRIGGER_SECTION_LINK),
                     driver.find_element(*HOW_TO_START_HERE_LINK),
                     driver.find_element(*HOW_TO_START_DETAILED_USER_MANUAL_LINK)]
    for item in list_of_links:
        assert item.is_displayed(), f"{item.text} link not visible"


def test_tc_001_12_02_verify_that_rain_group_of_codes_is_visible(driver, open_and_load_main_page, wait):
    driver.find_element(*COOKIES_ALLOW_ALL_BUTTON_LINK).click()
    driver.find_element(*HEADER_API_LINK).click()
    wait.until(EC.element_to_be_clickable(HOME_LINK))
    actions = ActionChains(driver)
    actions.move_to_element(driver.find_element(*LIST_OF_WEATHER_CONDITION_CODES_LINK)).perform()
    driver.find_element(*LIST_OF_WEATHER_CONDITION_CODES_LINK).click()
    wait.until(EC.element_to_be_clickable(WEATHER_CONDITION_CODES_LINK))
    driver.find_element(*WEATHER_CONDITION_CODES_LINK).click()
    wait.until(EC.element_to_be_clickable(HOME_LINK))
    actions1 = ActionChains(driver)
    actions1.move_to_element(driver.find_element(*GROUP_6XX_SNOW_LINK)).perform()
    list_of_elements = driver.find_elements(*GROUP_5XX_RAIN_ROWS_LINK)
    for number, item in enumerate(list_of_elements):
        assert item.is_displayed(), f"{number} row not visible"

        
def test_tc_001_12_03_verify_that_rain_group_of_codes_contains_more_than_1_item(driver, open_and_load_main_page, wait):
    driver.find_element(*COOKIES_ALLOW_ALL_BUTTON_LINK).click()
    driver.find_element(*HEADER_API_LINK).click()
    wait.until(EC.element_to_be_clickable(HOME_LINK))
    actions = ActionChains(driver)
    actions.move_to_element(driver.find_element(*LIST_OF_WEATHER_CONDITION_CODES_LINK)).perform()
    driver.find_element(*LIST_OF_WEATHER_CONDITION_CODES_LINK).click()
    wait.until(EC.element_to_be_clickable(WEATHER_CONDITION_CODES_LINK))
    driver.find_element(*WEATHER_CONDITION_CODES_LINK).click()
    wait.until(EC.element_to_be_clickable(HOME_LINK))
    actions1 = ActionChains(driver)
    actions1.move_to_element(driver.find_element(*GROUP_6XX_SNOW_LINK)).perform()
    list_of_elements = driver.find_elements(*GROUP_5XX_RAIN_ROWS_LINK)
    assert len(list_of_elements) > 2, "rain_group_of_codes_contains 1 or less item"


def get_section_locator_for_tc_008_01_04(section):
    return (By.XPATH, f'//section[@id="{section}"]')


def get_section_title_locator_for_tc_008_01_04(section):
    return (By.CSS_SELECTOR, f'#{section} h2')


@pytest.mark.parametrize('section', sections)
def test_tc_008_01_04_check_6_sections_are_visible(driver, open_and_load_main_page, wait, section):
    driver.find_element(*HEADER_PRICING_LINK).click()
    wait.until(EC.element_to_be_clickable(PRICING_SUBSCRIBE_TO_ONE_CALL_BY_CALL_BUTTON))
    section_locator = get_section_locator_for_tc_008_01_04(section)
    actual_section = driver.find_element(*section_locator)
    actual_section.location_once_scrolled_into_view
    section_title_locator = get_section_title_locator_for_tc_008_01_04(section)
    assert actual_section.is_displayed(), \
        f"Section {driver.find_element(*section_title_locator).text} is not visible"


def test_tc_001_10_02_verify_count_of_icons_for_daytime(driver, open_weather_condition_page):
    minimum_icons_for_daytime = 8
    driver.find_element(*WEATHER_ICONS).click()
    actual_icons_daytime = driver.find_elements(*ICONS_FOR_DAYTIME)
    quantity = len(actual_icons_daytime)
    assert quantity >= minimum_icons_for_daytime, f"Count of daytime icons less then 8 and equal {quantity}"
