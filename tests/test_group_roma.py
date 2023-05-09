from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import pytest


footer_website_locator = (By.CLASS_NAME, "inner-footer-container")
company_title_locator = (By.XPATH, "//p[@class='section-heading' and text()='Company']")
company_content_locator = (By.CSS_SELECTOR, ".footer-section > div > p")
gitHub_icon_image = (By.XPATH, "//div[@class='social']//a[6]/img")
logo = (By.CSS_SELECTOR, "#first-level-nav a")
URL = 'https://openweathermap.org/'
#The page 'Maps' (/weathermap) doesn't include because it hasn't website footer
PAGES = ['', 'guide', 'api', 'weather-dashboard', 'price', 'our-initiatives', 'examples', 'home/sign_in', 'faq', 'appid']


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


@pytest.mark.parametrize('page', PAGES)
def test_TC_003_01_01_verify_footer_is_visible_from_all_pages_specified_in_data(driver, wait, page):
    driver.get(f'{URL}{page}')
    footer_website = driver.find_element(*footer_website_locator)
    driver.execute_script('arguments[0].scrollIntoView();', footer_website)
    # print(footer_website.is_displayed(), driver.current_url, driver.title)
    assert footer_website.is_displayed() and driver.title not in 'Page not found (404) - OpenWeatherMap', \
        f'\nFooter is not present on the page - {driver.current_url}'
