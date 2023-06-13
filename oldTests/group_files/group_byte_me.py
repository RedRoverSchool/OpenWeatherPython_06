from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


WEATHER_IN_YOUR_CITY_FLD = (By.CSS_SELECTOR, "#desktop-menu input:nth-child(1)")
REQUESTED_CITY = 'London, GB'
DISPLAYED_CITY = (By.XPATH, "//*[@Class='table']//tr[1]//b/a")
SEARCH_CITY_FIELD_locator = (By.CSS_SELECTOR, "input[placeholder='Search city']")
SEARCH_BUTTON_Locator = (By.CSS_SELECTOR, "button[class='button-round dark']")
SEARCH_OPTION_Locator = (By.CSS_SELECTOR, "ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)")
DISPLAYED_CITY_1_Locator = (By.CSS_SELECTOR, ".grid-container.grid-4-5 h2")


def test_tc_002_02_01_01_search_city_results_are_visible(driver, wait, open_and_load_main_page):
    weather_in_your_city_field = driver.find_element(*WEATHER_IN_YOUR_CITY_FLD)
    action_chains = ActionChains(driver)
    action_chains.move_to_element(weather_in_your_city_field)
    driver.execute_script("arguments[0].click();", weather_in_your_city_field)
    weather_in_your_city_field.send_keys(*REQUESTED_CITY)
    weather_in_your_city_field.submit()
    displayed_text = wait.until(EC.visibility_of_element_located(DISPLAYED_CITY))
    assert displayed_text.text == REQUESTED_CITY

def test_tc_001_01_01_02_searching_requested_city_name_displayed_in_widget(driver, wait, open_and_load_main_page):
    search_city_field = driver.find_element(*SEARCH_CITY_FIELD_locator)
    search_city_field.send_keys('Kyiv, UA')
    search_button = driver.find_element(*SEARCH_BUTTON_Locator)
    search_button.click()
    driver.implicitly_wait(10)
    search_option = wait.until(EC.element_to_be_clickable(SEARCH_OPTION_Locator))
    search_option.click()
    expected_city = 'Kyiv, UA'
    driver.find_element(*DISPLAYED_CITY_1_Locator)
    wait.until(EC.text_to_be_present_in_element(DISPLAYED_CITY_1_Locator, 'Kyiv, UA'))
    displayed_city_1 = driver.find_element(*DISPLAYED_CITY_1_Locator)
    assert displayed_city_1.text == expected_city
