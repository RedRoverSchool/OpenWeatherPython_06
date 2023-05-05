from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

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
