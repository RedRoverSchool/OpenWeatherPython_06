import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://openweathermap.org/'


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
