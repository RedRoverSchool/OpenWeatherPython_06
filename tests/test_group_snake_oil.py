from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

HOME_PAGE_URL = "https://openweathermap.org/"
LOADING_VEIL = (By.CSS_SELECTOR, "div[aria-label='Loading']")
linkedIn_icon = (By.CSS_SELECTOR, "div[class='social'] a:nth-child(3)")


def test_tc_003_10_06_verify_linkedIn_link_is_visible(driver, open_and_load_main_page, wait):
    driver.maximize_window()
    element = wait.until(EC.visibility_of_element_located(linkedIn_icon))
    assert element.is_displayed(), "LinkedIn interactive icon is not visible on a page"
