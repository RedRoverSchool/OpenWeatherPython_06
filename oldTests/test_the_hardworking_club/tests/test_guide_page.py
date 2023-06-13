from oldTests.test_the_hardworking_club.pages.guide_page import GuidePage

class TestGuide:


    def test_TC_004_03_01_all_links_are_visibility(self, driver):

        guide_page = GuidePage(driver)
        guide_page.check_the_all_links_are_visibility()

