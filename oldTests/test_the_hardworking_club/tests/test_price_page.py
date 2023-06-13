from oldTests.test_the_hardworking_club.pages.price_page import PricePage


class TestPricePage:

    def test_TC_008_01_01_subscribe_button_redirects(self, driver):
        price_page = PricePage(driver)
        price_page.check_subscribe_button_redirect()
