import time

from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def test_open_page():
    driver.get('https://openweathermap.org/')


def test_title():
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


def test_description():
    description_element = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.XPATH, '//span[text()="Weather forecasts, nowcasts and history in a fast and elegant way"]')))
    assert description_element.text == "Weather forecasts, nowcasts and history in a fast and elegant way"


def test_sign_in_page():
    driver.get('https://home.openweathermap.org/users/sign_in')


def test_login():
    search_email_field = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.XPATH, "(//input)[9]")))
    search_email_field.send_keys("tester1627283@gmail.com")
    search_password_field = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.XPATH, "(//input)[10]")))
    search_password_field.send_keys("tester123")
    submit_button = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.XPATH, "(//input)[13]")))
    submit_button.click()