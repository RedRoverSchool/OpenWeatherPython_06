from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

HEADER_API_LINK = (By.XPATH, '//div[@id="desktop-menu"]//a[.="API"]')
HOME_LINK = (By.XPATH, '//ol//a[.="Home"]')
LIST_OF_WEATHER_CONDITION_CODES_LINK = (By.XPATH, '//a[.="List of weather condition codes"]')
WEATHER_CONDITION_CODES_LINK = (By.XPATH, '//a[.="weather condition codes"]')
GROUP_6XX_SNOW_LINK = (By.XPATH, '//h3[.="Group 6xx: Snow"]')
GROUP_5XX_RAIN_ROWS_LINK = (By.XPATH, '//h3[.="Group 5xx: Rain"]/../following-sibling::tbody/tr')
COOKIES_ALLOW_ALL_BUTTON_LINK = (By.XPATH, '//button[.="Allow all"]')


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
