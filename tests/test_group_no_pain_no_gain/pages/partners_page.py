from .main_page import MainPage
from tests.test_group_no_pain_no_gain.locators.partners_page_locators import PartnersPageLocators as PPL
from tests.test_group_no_pain_no_gain import links

class Partners(MainPage):
    def check_partners_page_title(self):
        self.driver.get(links.PARTNERS_AND_SOLUTIONS)
        title = self.driver.title
        assert 'Partners and solutions' in title
