from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    LINK_PRICING = (By.XPATH, '//div[@id="desktop-menu"]//a[text()="Pricing"]')

    def __init__(self, driver, link=None):
        self.driver = driver
        self.link = link

    def click_header_link(self, link_name):
        action_chains = ActionChains(self.driver)
        match link_name:
            case 'pricing':
                button_pricing = self.driver.find_element(*self.LINK_PRICING)
                action_chains.move_to_element(button_pricing)
                self.driver.execute_script("arguments[0].click();", button_pricing)

