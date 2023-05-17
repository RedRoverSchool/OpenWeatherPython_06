
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


WEATHER_IN_YOUR_CITY_FLD = (By.CSS_SELECTOR, "#desktop-menu input:nth-child(1)")
REQUESTED_CITY = 'London, GB'
DISPLAYED_CITY = (By.CSS_SELECTOR, "table b a:nth-child(1)")


def test_search_city_results_are_visible(driver, wait, open_and_load_main_page):
    weather_in_your_city_field = driver.find_element(*WEATHER_IN_YOUR_CITY_FLD)
    action_chains = ActionChains(driver)
    action_chains.move_to_element(weather_in_your_city_field)
    driver.execute_script("arguments[0].click();", weather_in_your_city_field)
    weather_in_your_city_field.send_keys(*REQUESTED_CITY)
    weather_in_your_city_field.submit()
    displayed_city = driver.find_element(*DISPLAYED_CITY).text
    assert displayed_city == REQUESTED_CITY
