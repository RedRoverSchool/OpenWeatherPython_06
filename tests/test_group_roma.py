from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

footer_website_locator = (By.ID, "footer-website")
company_title_locator = (By.XPATH, "//p[@class='section-heading' and text()='Company']")
company_content_locator = (By.CSS_SELECTOR, ".footer-section > div > p")
gitHub_icon_image = (By.XPATH, "//div[@class='social']//a[6]/img")
logo = (By.CSS_SELECTOR, "#first-level-nav a")


def test_TC_003_07_01_visibility_of_the_company_module(driver, open_and_load_main_page, wait):
    footer_website = driver.find_element(*footer_website_locator)
    driver.execute_script("arguments[0].scrollIntoView();", footer_website)
    company_title = driver.find_element(*company_title_locator)
    assert company_title.is_displayed()
    content = driver.find_element(*company_content_locator)
    assert content.is_displayed()


def test_TC_003_10_03_visibility_of_GitHub_icon(driver, open_and_load_main_page, wait):
    footer_website = driver.find_element(*footer_website_locator)
    driver.execute_script("arguments[0].scrollIntoView();", footer_website)
    github_icon = driver.find_element(*gitHub_icon_image)
    assert github_icon.is_displayed()


def test_TC_002_01_02_verify_returning_from_API_page_to_main_page_by_clicking_on_logo(driver, wait):
    driver.get('https://openweathermap.org/api')
    driver.find_element(*logo).click()
    assert 'https://openweathermap.org/' in driver.current_url
