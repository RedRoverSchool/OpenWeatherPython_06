from tests.test_group_no_pain_no_gain.pages.footer import Footer
from tests.test_group_no_pain_no_gain import links
from tests.test_group_no_pain_no_gain.locators.footer_locators import FooterLocators as FL

class TestFooter:
    def test_TC_003_08_02_ask_a_question_link_is_visible(self, driver, open_and_load_main_page, wait):
        page = Footer(driver)
        page.element_visibility(FL.ASK_A_QUESTION_LINK)

