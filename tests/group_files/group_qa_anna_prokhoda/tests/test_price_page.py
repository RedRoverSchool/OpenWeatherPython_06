from tests.group_files.group_qa_anna_prokhoda.pages.price_page import PricePage
from tests.group_files.group_qa_anna_prokhoda.links.links import price_page_url


class TestLogoFromPagePricingRedirectsToMainPage:

    def test_TC_002_01_07_verify_clicking_on_the_logo_from_page_Pricing_redirects_to_main_page(self, driver):
        price_page = PricePage(driver, price_page_url)
        price_page.open_page()
        price_page.verify_clicking_on_the_logo_from_page_Pricing_redirects_to_main_page()
