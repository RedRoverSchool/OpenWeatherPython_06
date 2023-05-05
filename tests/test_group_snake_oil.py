from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

HOME_PAGE_URL = "https://openweathermap.org/"
LOADING_VEIL = (By.CSS_SELECTOR, "div[aria-label='Loading']")
linkedIn_icon = (By.CSS_SELECTOR, "div[class='social'] a:nth-child(3)")


def test_tc_003_10_06_verify_linkedIn_link_is_visible(driver):
    driver.get(HOME_PAGE_URL)
    driver.maximize_window()
    wait = WebDriverWait(driver, 25)
    wait.until_not(EC.presence_of_element_located(LOADING_VEIL))
    element = wait.until(EC.visibility_of_element_located(linkedIn_icon))
    assert element.is_displayed()
