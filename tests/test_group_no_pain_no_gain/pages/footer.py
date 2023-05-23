from .main_page import MainPage
from tests.test_group_no_pain_no_gain.locators.footer_locators import FooterLocators as FL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

class Footer(MainPage):
    def element_visibility(self, locator):
        element = wait(self.driver, timeout=3).until(EC.visibility_of_element_located(locator))
        assert element.is_displayed(), 'element is not visible'

    def element_clickability(self, locator):
        element = wait(self.driver, timeout=3).until(EC.element_to_be_clickable(locator))
        assert element.is_enabled(), 'element is not clickable'

