import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

FOOTER_PANEL = (By.XPATH, '//*[@id="stick-footer-panel"]/div')
BTN_ALLOW_ALL = (By.CLASS_NAME, "stick-footer-panel__link")
FOOTER_COPYRIGHT = (By.XPATH, "//div[@class='horizontal-section my-5']/div[1]")


def test_TC_003_11_01_verify_the_copyright_information_is_present_on_the_page(driver, open_and_load_main_page, wait):
    wait.until(EC.element_to_be_clickable(FOOTER_PANEL))
    driver.find_element(*BTN_ALLOW_ALL).click()
    expected_footer_text = "© 2012 — 2023 OpenWeather"
    footer = driver.find_element(*FOOTER_COPYRIGHT)
    assert footer.is_displayed() and expected_footer_text in footer.text,\
        "The footer is not displayed or does not contain the expected text"


