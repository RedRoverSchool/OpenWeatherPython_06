import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains




URL = 'https://openweathermap.org/'
cities = ['New York', 'Los Angeles', 'Paris']
load_div = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
displayed_city = (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2')
search_city_field = (By.CSS_SELECTOR, "input[placeholder='Search city']")
search_button = (By.CSS_SELECTOR, "button[class ='button-round dark']")


def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url


def test_check_page_title(driver):  # check title name
    driver.get('https://home.openweathermap.org/marketplace')
    assert driver.title == 'Marketplace: History Bulk, History Forecast Bulk, ' \
                           'Historical Weather Data by State for all ZIP codes, USA - OpenWeather'


def test_top_bar_nav(driver):
    driver.get('https://openweathermap.org/')
    time.sleep(5)
    top_bar_buttons = driver.find_elements(By.XPATH, "//div[@id='desktop-menu']/ul/li")
    print(top_bar_buttons)
    assert len(top_bar_buttons) == 12
    top_bar_button1_guide = driver.find_element(By.XPATH, "//div[@id='desktop-menu']/ul/li/a[@href='/guide']")
    print(f"Guide is displayed {top_bar_button1_guide.is_displayed()}")
    top_bar_button2_api = driver.find_element(By.XPATH, "//div[@id='desktop-menu']/ul/li/a[@href='/api']")
    print(f"API is displayed {top_bar_button2_api.is_displayed()}")
    top_bar_button3_dashboard = driver.find_element(By.XPATH,
                                                    "//div[@id='desktop-menu']/ul/li/a[@href='/weather-dashboard']")
    print(f"Dashboard is displayed {top_bar_button3_dashboard.is_displayed()}")
    top_bar_button4_marketplace = driver.find_element(By.XPATH,
                                                      "//div[@id='desktop-menu']/ul/li/a[@href='https://home.openweathermap.org/marketplace']")
    print(f"Marketplace is displayed {top_bar_button4_marketplace.is_displayed()}")
    top_bar_button5_pricing = driver.find_element(By.XPATH, "//div[@id='desktop-menu']/ul/li/a[@href='/price']")
    print(f"Pricing is displayed {top_bar_button5_pricing.is_displayed()}")
    top_bar_button6_map = driver.find_element(By.XPATH, "//div[@id='desktop-menu']/ul/li/a[@href='/weathermap']")
    print(f"Map is displayed {top_bar_button6_map.is_displayed()}")
    top_bar_button7_our_initiatives = driver.find_element(By.XPATH,
                                                          "//div[@id='desktop-menu']/ul/li/a[@href='/our-initiatives']")
    print(f"Our Initiatives is displayed {top_bar_button7_our_initiatives.is_displayed()}")
    top_bar_button8_partners = driver.find_element(By.XPATH, "//div[@id='desktop-menu']/ul/li/a[@href='/examples']")
    print(f"Partners is displayed {top_bar_button8_partners.is_displayed()}")
    top_bar_button9_blog = driver.find_element(By.XPATH,
                                               "//div[@id='desktop-menu']/ul/li/a[@href='https://openweather.co.uk/blog/category/weather']")
    print(f"Blog is displayed {top_bar_button9_blog.is_displayed()}")
    top_bar_button10_for_business = driver.find_element(By.XPATH,
                                                        "//div[@id='desktop-menu']/ul/li/a[@href='https://openweather.co.uk']")
    print(f"For Business is displayed {top_bar_button10_for_business.is_displayed()}")
    top_bar_button11_signin = driver.find_element(By.XPATH,
                                                  "//div[@id='desktop-menu']/ul/li/a[@href='https://openweathermap.org/home/sign_in']")
    print(f"Sign In is displayed {top_bar_button11_signin.is_displayed()}")
    top_bar_button12_support = driver.find_element(By.XPATH, "//div[@id='desktop-menu']/ul/li[@class='with-dropdown']")
    print(f"Support is displayed {top_bar_button12_support.is_displayed()}")
    top_bar_search = driver.find_element(By.CSS_SELECTOR, '#desktop-menu input[placeholder="Weather in your city"]')
    print(f"Search field on the top is displayed {top_bar_search.is_displayed()}")
    top_bar_logo = driver.find_element(By.XPATH, "//li[@class='logo']")
    print(f"Main logo on the top is displayed {top_bar_logo.is_displayed()}")



def test_dashboard_title(driver):
    driver.get('https://openweathermap.org/weather-dashboard')
    assert driver.title == 'Weather dashboard - OpenWeatherMap'

search_dropdown = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li')
search_dropdown_option = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')

urls = [
    'https://openweathermap.org/faq',
    'https://openweathermap.org/appid',
    'https://home.openweathermap.org/questions'
]

texts = [
    'FAQ',
    'How to start',
    'Ask a question'
]

def test_support_drop_down(driver):
    driver.get(URL)

    el_list = driver.find_element(By.ID, "support-dropdown-menu")
    items = el_list.find_elements(By.TAG_NAME, "li")
    assert len(items) == 3
    for i, el in enumerate(items):
        assert el.find_element(By.TAG_NAME, 'a').get_attribute('href') == urls[i]
        assert el.find_element(By.TAG_NAME, 'a').get_attribute("innerHTML") == texts[i]


def test_pricing_title(driver):
    driver.get('https://openweathermap.org/price')
    assert driver.title == 'Pricing - OpenWeatherMap'


def test_partners_title(driver):
    driver.get('https://openweathermap.org/examples')
    assert driver.title == 'Partners and solutions - OpenWeatherMap'


def test_guide_title(driver):
    driver.get('https://openweathermap.org/guide')
    assert driver.title == 'OpenWeatherMap API guide - OpenWeatherMap'


def test_open_initiatives_title(driver):
    driver.get('https://openweathermap.org/our-initiatives')
    assert driver.title == 'Our Initiatives - OpenWeatherMap'



@pytest.mark.parametrize('city', cities)
def test_fill_search_city_field(driver, city):
    driver.get('https://openweathermap.org/')
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    search_city_input = driver.find_element(*search_city_field)
    search_city_input.send_keys(city)
    driver.find_element(*search_button).click()
    wait.until(EC.element_to_be_clickable(search_dropdown_option)).click()
    expected_city = city
    wait.until(EC.text_to_be_present_in_element(displayed_city, city))
    actual_city = driver.find_element(*displayed_city).text
    assert expected_city in actual_city

def test_open_marketplace(driver):
    driver.get('https://openweathermap.org/')
    element = driver.find_element(By.CSS_SELECTOR, 'div#desktop-menu a[href*=marketplace]')
    actions = ActionChains(driver)
    actions.move_to_element(element)
    driver.execute_script("arguments[0].click();", element)
    WebDriverWait(driver, 15).until(
        EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.XPATH, '//div//h5//a[@href="/history_bulks/new"]').click()
    assert 'history_bulks/new' in driver.current_url



def test_blog_title(driver):
    driver.get('https://openweather.co.uk/blog/category/weather')
    assert driver.title == 'Blog - OpenWeatherMap'





