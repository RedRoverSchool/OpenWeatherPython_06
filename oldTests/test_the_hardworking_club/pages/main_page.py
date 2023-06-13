from pages.base_page import BasePage
from oldTests.test_the_hardworking_club.locators.locators_all import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    locators = MainPageLocators()
    URL_MAIN_PAGE = "https://openweathermap.org/"
    PRIVACY_POLICY_URL = "https://openweather.co.uk/privacy-policy"

    def verify_privacy_policy_is_opened_after_click(self, driver, wait):
        self.driver.get(MainPage.URL_MAIN_PAGE)
        privacy_policy_button = wait.until(EC.element_to_be_clickable(self.locators.XPATH_PRIVACY_POLICY_BUTTON))
        self.driver.execute_script("arguments[0].click();", privacy_policy_button)
        self.driver.switch_to.window(driver.window_handles[1])
        assert self.driver.current_url == MainPage.PRIVACY_POLICY_URL