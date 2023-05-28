from tests.test_group_snake_oil.pages.pricing_for_business_page import PricingForBusinessPage


class TestPricingForBusinessPage:

    def test_tc_012_02_01_table_data_content_check(self, driver):
        page = PricingForBusinessPage(driver, "https://openweather.co.uk/pricing-corp")
        page.open_page()
        page.get_table_content()
