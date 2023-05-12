from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# from selenium.webdriver.common.by import By
# URL = 'https://openweathermap.org/'
#
# search_dropdown = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li')
# search_dropdown_option = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')
#
# urls = [
#     'https://openweathermap.org/faq',
#     'https://openweathermap.org/appid',
#     'https://home.openweathermap.org/questions'
# ]
#
# texts = [
#     'FAQ',
#     'How to start',
#     'Ask a question'
# ]
#
# def test_support_drop_down(driver):
#     driver.get(URL)
#
#     el_list = driver.find_element(By.ID, "support-dropdown-menu")
#     items = el_list.find_elements(By.TAG_NAME, "li")
#     assert len(items) == 3
#
#     for i, el in enumerate(items):
#         assert el.find_element(By.TAG_NAME, 'a').get_attribute('href') == urls[i]
#         assert el.find_element(By.TAG_NAME, 'a').get_attribute("innerHTML") == texts[i]

subscribe_button = (By.XPATH, '//a[contains(text(), "Subscribe to One Call by Call")]')
cookie_button = (By.CSS_SELECTOR, 'button.stick-footer-panel__link')

def test_TC_008_01_01_subscribe_button_redirects(driver):
    driver.get('https://openweathermap.org/price')
    cookie_button_click = driver.find_element(*cookie_button)
    cookie_button_click.click()
    # wait.until(EC.presence_of_element_located(*subscribe_button))
    subscribe_button_click = driver.find_element(*subscribe_button)
    subscribe_button_click.click()
    assert 'home.openweathermap.org/subscriptions' in driver.current_url and 'onecall_30/base' in driver.current_url