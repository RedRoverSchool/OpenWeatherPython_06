import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

HEAD_SEARCH_FIELD = (By.NAME, "q")
HEAD_SEARCH_PLACEHOLDER = (By.CSS_SELECTOR, 'input[name="q"]::placeholder')


def test_TC_002_02_07_verify_placeholder_is_displayed_in_search_field(driver, open_and_load_main_page, wait):
    search_field = wait.until(EC.presence_of_element_located(HEAD_SEARCH_FIELD))
    search_placeholder_text = search_field.get_attribute("placeholder")
    assert search_placeholder_text == "Weather in your city", \
        "Password field placeholder text is incorrect or missing"
