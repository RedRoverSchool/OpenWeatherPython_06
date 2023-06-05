from tests.test_group_future_auto_qa.pages.guide_page import GuidePage


class TestGuidePage:
    def test_tc_004_09_01_weather_maps_collection_block_visibility(self, driver):
        page = GuidePage(driver)
        page.check_weather_maps_collection_block_visibility()

    def test_tc_004_09_02_global_precipitation_maps_link_clickability(self, driver):
        page = GuidePage(driver)
        page.check_global_precipitation_maps_link_clickability()
