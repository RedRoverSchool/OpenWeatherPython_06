import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def test_buttonVisible():
    browser.get("https://openweathermap.org/")
    Button = browser.find_element(By.XPATH, "//*[contains(text(), 'Manage cookies')]")
    assert Button.text == "Manage cookies", "wrong"
    print(Button.text, "button is visible")
    browser.quit()


