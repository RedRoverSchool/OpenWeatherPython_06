from tests.test_group_100000.pages.main_page import FooterBlock


class TestHowToStartLink:
    def test_TC_003_05_03_verify_how_to_start_link_is_clickable(self, driver):
        page = FooterBlock(driver, link='https://openweathermap.org/')
        page.open_page()
        page.verify_how_to_start_link_is_clickable()



