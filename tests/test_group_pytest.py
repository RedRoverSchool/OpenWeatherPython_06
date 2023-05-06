from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

MEDIUM_LINK = (By.XPATH, '//a[@href="https://medium.com/@openweathermap"]')


def test_tc_003_10_07_check_medium_icon_visible_and_clickable(driver, open_and_load_main_page, wait):
    driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.END)
    medium_link = wait.until(EC.element_to_be_clickable(MEDIUM_LINK))
    assert medium_link.is_displayed() and medium_link.is_enabled(), "The medium icon is not displayed or not clickable"
