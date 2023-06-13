from pages.base_page import BasePage
from tests.group_files.group_qa_anna_prokhoda.locators.price_page_locators import PricePageLocators
from tests.group_files.group_qa_anna_prokhoda.links.links import main_page_url


class PricePage(BasePage):
    locators = PricePageLocators()


    def verify_clicking_on_the_logo_from_page_Pricing_redirects_to_main_page(self):
        self.driver.find_element(*self.locators.logo).click()
        assert self.driver.current_url == main_page_url
