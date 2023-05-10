from selenium.webdriver.common.by import By

logo_locator = (By.CSS_SELECTOR, ".logo > a > img")


def test_TC_002_01_01_return_from_guide_page_to_main_page_by_clicking_on_logo(driver):
    driver.get('https://openweathermap.org/guide')
    driver.find_element(*logo_locator).click()
    assert driver.current_url == 'https://openweathermap.org/'


def test_TC_003_08_07_verify_Blog_link_is_visible(driver, open_and_load_main_page):
    element = driver.find_element(By.XPATH, "//*[@id='footer-website']/div/div[2]/div[3]/div/ul/li[2]/a")
    assert element.is_displayed(), "Blog"

