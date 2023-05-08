from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

FOOTER_PANEL = (By.XPATH, '//*[@id="stick-footer-panel"]/div')
BTN_ALLOW_ALL = (By.CLASS_NAME, "stick-footer-panel__link")
FOOTER_COPYRIGHT = (By.XPATH, "//div[@class='horizontal-section my-5']/div[1]")
DASHBOARD_LINK = (By.XPATH, '//div[@id="desktop-menu"]//a[contains(@href, "/weather-dashboard")]')
BTN_DASHBOARD = (By.CSS_SELECTOR, "#desktop-menu [href$=-dashboard]")
TITLE_HOW_TO_START = (By.XPATH, "//div/h2[contains(text(),'How to Start')]")
LOGO = (By.CSS_SELECTOR, ".logo > a > img")


def test_TC_003_11_01_verify_the_copyright_information_is_present_on_the_page(driver, open_and_load_main_page, wait):
    wait.until(EC.element_to_be_clickable(FOOTER_PANEL))
    driver.find_element(*BTN_ALLOW_ALL).click()
    expected_footer_text = "© 2012 — 2023 OpenWeather"
    footer = driver.find_element(*FOOTER_COPYRIGHT)
    assert footer.is_displayed() and expected_footer_text in footer.text, \
        "The footer is not displayed or does not contain the expected text"


def test_TC_002_03_05_dashboard_is_visible_and_clickable(driver, open_and_load_main_page, wait):
    wait.until(EC.element_to_be_clickable(DASHBOARD_LINK))
    dashboard_tab = driver.find_element(*DASHBOARD_LINK)
    expected_dashboard_label = 'Dashboard'
    assert dashboard_tab.is_displayed() and dashboard_tab.is_enabled() and expected_dashboard_label in dashboard_tab.text


def test_TC_006_02_01_Verify_display_of_How_to_Start_section(driver, open_and_load_main_page, wait):
    driver.find_element(*BTN_DASHBOARD).click()
    section = driver.find_element(*TITLE_HOW_TO_START)
    assert section.is_displayed(), "Section not found"


def test_TC_002_03_06_dashboard_link_opens_correct_page(driver, open_and_load_main_page, wait):
    wait.until(EC.element_to_be_clickable(DASHBOARD_LINK))
    dashboard_tab = driver.find_element(*DASHBOARD_LINK)
    dashboard_tab.click()
    expected_url = 'https://openweathermap.org/weather-dashboard'
    assert driver.current_url == expected_url


def test_TC_002_01_04_Header_Logo_Verify_logo_redirects_from_dashboard_page_to_main_page(driver):
    driver.get('https://openweathermap.org/weather-dashboard/')
    driver.find_element(*LOGO).click()
    assert driver.current_url == 'https://openweathermap.org/'
