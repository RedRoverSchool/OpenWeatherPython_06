import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


search_sky_in_words = (By.XPATH, "//div[@class='day-list-values']/span[contains(@class,'sub')]")
how_to_start_footer_loc = (By.CSS_SELECTOR, "div.section-content ul>li>a[href='/appid']")
URL_HISTORICAL_WEATHER = 'https://home.openweathermap.org/zip_code_data/new'
SELECT_STATE_FIELD = (By.CSS_SELECTOR, '#__BVID__10 .form-control.dropdown-selector')
STATE_TEXAS = (By.XPATH, "//span[text()='Texas']")
weather_symbol = (By.CSS_SELECTOR, "ul  > li:nth-child(3) > span.symbol")


def test_TC_001_04_02_Verify_state_of_sky_in_words_for_each_day_is_displayed(driver, open_and_load_main_page, wait):
    elements = driver.find_elements(*search_sky_in_words)
    for i in elements:
        assert i.is_displayed()
    driver.quit()


def test_TC_007_01_01_Select_state_from_dropdown_list(driver, wait):
    driver.get(URL_HISTORICAL_WEATHER)
    wait.until(EC.element_to_be_clickable([*SELECT_STATE_FIELD])).click()
    wait.until(EC.presence_of_element_located([*STATE_TEXAS])).click()
    expected_state = "Texas"
    selected_state = driver.find_element(*STATE_TEXAS).text
    assert expected_state == selected_state, '\n======== WRONG STATE! ========\n'


def test_TC_001_05_03_Verify_humidity_percentage_in_detailed_weather_data_for_current_location(driver, open_and_load_main_page, wait):
    humidity_symbol = driver.find_element(*weather_symbol)
    assert humidity_symbol.is_displayed()


def test_TC_003_05_03_verify_how_to_start_link_is_clickable(driver, open_and_load_main_page, wait):
    how_to_start = wait.until(EC.element_to_be_clickable(how_to_start_footer_loc))
    assert how_to_start.is_enabled(), "The 'How to start' link does not clickable"
