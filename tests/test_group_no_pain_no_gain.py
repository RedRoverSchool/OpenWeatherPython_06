from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

logo_locator = (By.CSS_SELECTOR, ".logo > a > img")
ASK_A_QUESTION_LINK = (By.XPATH, "(//*[contains(text(),'question')])[3]")


def test_TC_002_01_01_return_from_guide_page_to_main_page_by_clicking_on_logo(driver):
    driver.get('https://openweathermap.org/guide')
    driver.find_element(*logo_locator).click()
    assert driver.current_url == 'https://openweathermap.org/'

def test_TC_003_08_02_ask_a_question_link_is_visible(driver, open_and_load_main_page, wait):
    element = wait.until(EC.visibility_of_element_located(ASK_A_QUESTION_LINK))
    assert element.is_displayed(), "Ask a question link is not visible in the footer"
