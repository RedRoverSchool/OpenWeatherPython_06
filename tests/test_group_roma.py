import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



def test_TC_003_07_01_visibility_of_the_company_module(driver, open_and_load_main_page, wait):
    footer_website = driver.find_element(By.ID, "footer-website")
    driver.execute_script("arguments[0].scrollIntoView();", footer_website)
    company_module = driver.find_element(By.XPATH, "//p[@class='section-heading' and text()='Company']")
    assert company_module.is_displayed()
    content = driver.find_element(By.CSS_SELECTOR, ".footer-section > div > p")
    assert content.is_displayed()
