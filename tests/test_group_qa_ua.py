import time

from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

URL = 'https://openweathermap.org/'
cities = ['New York', 'Los Angeles', 'Paris']
load_div = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
search_dropdown = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li')
search_dropdown_option = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')
search_city_field = (By.CSS_SELECTOR, "input[placeholder='Search city']")
search_button = (By.CSS_SELECTOR, "button[class ='button-round dark']")
displayed_city = (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2')
sign_in_link = (By.CSS_SELECTOR, '.user-li a')
pricing_link = (By.CSS_SELECTOR, '#desktop-menu a[href="/price"]')
price_page_title = (By.CSS_SELECTOR, "h1[class='breadcrumb-title']")
accept_cookies = (By.CSS_SELECTOR, 'button.stick-footer-panel__link')


@pytest.fixture()
def open_and_load_page(driver, wait):
    driver.get(URL)
    wait.until_not(EC.presence_of_element_located(load_div))


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, 25)
    yield wait


def test_should_go_to_sign_in_page(driver, open_and_load_page, wait):
    sign_link = wait.until(EC.presence_of_element_located(sign_in_link))
    driver.execute_script("arguments[0].click();", sign_link)
    assert "sign_in" in driver.current_url, f"\nWrong URL - {driver.current_url}"


def test_open_page(driver):
    driver.get('https://openweathermap.org/')
    driver.maximize_window()
    assert 'openweathermap' in driver.current_url
    print(driver.current_url)


def test_check_page_title(driver):
    driver.get('https://openweathermap.org/')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


def test_fill_search_city_field(driver):
    driver.get('https://openweathermap.org/')
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    search_city_field.send_keys('New York')
    search_button = driver.find_element(By.CSS_SELECTOR, "button[class ='button-round dark']")
    search_button.click()
    search_option = WebDriverWait(driver, 15).until((EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)'))))
    search_option.click()
    expected_city = 'New York City, US'
    WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2'), 'New York'))
    displayed_city = driver.find_element(By.CSS_SELECTOR, '.grid-container.grid-4-5 h2').text
    # displayed_city_text = displayed_city.text
    # print(displayed_city_text)
    assert displayed_city == expected_city
    

def test_box_presence(driver):
    driver.get("https://home.openweathermap.org/marketplace")
    driver.maximize_window()
    # marketplace_button = driver.find_element(By.CSS_SELECTOR, "ul:nth-child(1) li:nth-child(4)")
    # marketplace_button.click()
    boxes = driver.find_elements(By.CSS_SELECTOR,".product:nth-child(1), .product:nth-child(2), .product")
    print(f'len boxes = {len(boxes)}')
    assert len(boxes) == 3
    

def test_search_field_placeholder(driver):
    driver.get('https://openweathermap.org/')
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    expected_placeholder = 'Search city'
    actual_placeholder = search_city_field.get_attribute('placeholder')
    assert actual_placeholder == expected_placeholder, f'Search field placeholder is {actual_placeholder}, expected {expected_placeholder}'


def test_check_log_in(driver, open_and_load_page, wait):
    driver.find_element(*accept_cookies).click()
    expected_text = 'Sign in'
    element = driver.find_element(*sign_in_link)
    sign_in_text = driver.execute_script("return arguments[0].textContent", element)
    assert sign_in_text == expected_text


def test_find_metric_buttons(driver):
    driver.get(URL)
    search_metric_button = driver.find_element(By.CSS_SELECTOR, 'div.switch-container > div:nth-child(2)')
    search_imperial_button = driver.find_element(By.CSS_SELECTOR, 'div.switch-container > div:nth-child(3)')
    expected_metric_button = 'Metric: °C, m/s'
    expected_imperial_button = 'Imperial: °F, mph'
    assert search_metric_button.text == expected_metric_button
    assert search_imperial_button.text == expected_imperial_button


def test_footer_social_links(driver):
    driver.get(URL)
    actions = ActionChains(driver)

    social_links = driver.find_elements(by=By.XPATH, value="//div[@class='social']/a")
    actions.move_to_element(social_links[0])
    actions.perform()

    allow_button = driver.find_element(by=By.XPATH, value="//button[@class='stick-footer-panel__link']")
    allow_button.click()

    links_array = [
        'https://www.facebook.com/groups/270748973021342',
        'https://twitter.com/OpenWeatherMap',
        'https://www.linkedin.com/uas/login?session_redirect=%2Fcompany%2F9816754',
        'https://openweathermap.medium.com/',
        'https://t.me/openweathermap',
        'https://github.com/search?q=openweathermap&ref=cmdform'
    ]

    for i in range(len(social_links)):
        social_links[i].click()
        time.sleep(3)

        handles = driver.window_handles
        driver.switch_to.window(handles[i+1])

        assert driver.current_url == links_array[i], \
            f'Social link url does not correspond with the needed one: current: {driver.current_url}, required: {links_array[i]}'

        print(
            f'current url = {driver.current_url}'
        )

        driver.switch_to.window(handles[0])







