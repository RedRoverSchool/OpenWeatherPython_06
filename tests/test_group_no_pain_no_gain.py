from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

logo_locator = (By.CSS_SELECTOR, ".logo > a > img")
ASK_A_QUESTION_LINK = (By.XPATH, "(//*[contains(text(),'question')])[3]")
allow_all_cookies_locator = (By.XPATH, '//*[contains(text(), "Allow all")]')
PARTNERS_LINK = (By.CSS_SELECTOR, '#desktop-menu a[href="/examples"]')
PARTNERS_PAGE_TITLE = (By.XPATH, '//h1')

def test_TC_002_01_01_return_from_guide_page_to_main_page_by_clicking_on_logo(driver):
    driver.get('https://openweathermap.org/guide')
    driver.find_element(*logo_locator).click()
    assert driver.current_url == 'https://openweathermap.org/'

def test_TC_003_08_02_ask_a_question_link_is_visible(driver, open_and_load_main_page, wait):
    element = wait.until(EC.visibility_of_element_located(ASK_A_QUESTION_LINK))
    assert element.is_displayed(), "Ask a question link is not visible in the footer"

def test_TC_003_13_03_verify_visibility_and_clickability_of_allow_all_button(driver, open_and_load_main_page, wait):
    element = driver.find_element(*allow_all_cookies_locator)
    wait.until(EC.element_to_be_clickable(allow_all_cookies_locator))
    assert element.is_displayed() and element.is_enabled()

def test_TC_002_03_21_verify_that_the_partners_link_leads_to_the_correct_page(driver, open_and_load_main_page):
    driver.find_element(*PARTNERS_LINK).click()
    partners_title_text = driver.find_element(*PARTNERS_PAGE_TITLE).text
    assert partners_title_text == "Partners and solutions"
