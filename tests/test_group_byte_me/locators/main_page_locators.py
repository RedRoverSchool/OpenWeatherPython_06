from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


WEATHER_IN_YOUR_CITY_FLD = (By.CSS_SELECTOR, "#desktop-menu input:nth-child(1)")
REQUESTED_CITY = 'London, GB'
DISPLAYED_CITY = (By.CSS_SELECTOR, "table b a:nth-child(1)")