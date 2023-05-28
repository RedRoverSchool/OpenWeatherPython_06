import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
# from conftest import driver
# Main page locators
HEAD_SEARCH_FIELD = (By.NAME, "q")
HEAD_SEARCH_PLACEHOLDER = (By.CSS_SELECTOR, 'input[name="q"]::placeholder')
WIDGETS = (By.XPATH, "//a[contains(text(), 'Widgets')]")
COOKIES =(By.XPATH, "//button[contains(text(), 'Allow all')]")
QUESTION_ANSWER = (By.XPATH, "./following-sibling::div[@class='question-content']")


def test_TC_002_02_07_verify_placeholder_is_displayed_in_search_field(driver, open_and_load_main_page, wait):
    search_field = wait.until(EC.presence_of_element_located(HEAD_SEARCH_FIELD))
    search_placeholder_text = search_field.get_attribute("placeholder")
    assert search_placeholder_text == "Weather in your city", \
        "Password field placeholder text is incorrect or missing"


def test_TC_002_02_09_verify_placeholder_disappers_if_symbol_is_typed_in_search_field(driver, open_and_load_main_page, wait):
    search_field = wait.until(EC.presence_of_element_located(HEAD_SEARCH_FIELD))
    placeholder_text = search_field.get_attribute("placeholder")
    search_field.click()
    search_field.send_keys('a')
    assert placeholder_text not in search_field.get_attribute("value"), \
        "The placeholder text is still visible in the search field after typing a symbol"


def test_TC_003_12_12_widgets_link_functionality(driver, open_and_load_main_page, wait):
    wait.until(EC.element_to_be_clickable(COOKIES)).click()
    widgets = wait.until(EC.presence_of_element_located(WIDGETS))
    widget = widgets.get_attribute('href')
    widgets.click()
    driver.implicitly_wait(5)
    current_url = driver.current_url
    assert widget in current_url


def test_TC_005_10_01_visibility_of_weather_api_page_title(driver):
    driver.get('https://openweathermap.org/api')
    assert driver.title == 'Weather API - OpenWeatherMap', "The title of the page is incorrect"


def test_hidden_text_is_displayed_by_clicking_on_accordion_buttons(driver, wait):
    driver.get("https://openweathermap.org/faq")
    parent_elements = driver.find_elements(By.CSS_SELECTOR, ".question-heading")
    previous_content = None
    for parent_element in parent_elements:
        driver.execute_script("arguments[0].click();", parent_element)
        question_content = parent_element.find_element(*QUESTION_ANSWER)
        answer_text = question_content.find_element(By.CSS_SELECTOR, "p")
        assert answer_text.is_displayed(), "The answer text is not shown"
        if previous_content is not None:
            assert not previous_content.is_displayed(), "The previous answer content is not hidden"

        previous_content = question_content



