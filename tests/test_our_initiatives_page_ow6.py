import locators.locators
from pages.our_initiatives_page import OurInitiativesPage
from test_data.our_initiatives_page_data import sections
from test_data.urls import OurInitiativesPageUrls
import pytest


class TestOurInitiativesPage:

    @pytest.mark.parametrize("section", sections)
    def test_010_01_01_01_verify_sections(self, driver, open_and_load_main_page, section):
        page = OurInitiativesPage(driver, OurInitiativesPageUrls.OUR_INITIATIVES_PAGE)
        page.open_page()
        page.click_initiatives_link()
        page.get_section_element(section)

    def test_010_01_02_02_functionality(self, driver, open_and_load_main_page):
        page = OurInitiativesPage(driver, OurInitiativesPageUrls.EDUCATION_SECTION_PAGE)
        page.open_page()
        page.click_initiatives_link()
        page.click_education_learn_more()
        page.check_education_page_opened()

    def test_010_02_08_accessibility_of_question_headings(self, driver, open_and_load_main_page):
        page = OurInitiativesPage(driver, OurInitiativesPageUrls.EDUCATION_SECTION_PAGE)
        page.open_page()
        page.click_initiatives_link()
        page.click_education_learn_more()
        question_headings = page.get_question_headings()
        page.verify_question_headings_displayed(question_headings)

    def test_010_02_09_clickability_of_question_headings(self, driver, open_and_load_main_page):
        page = OurInitiativesPage(driver, OurInitiativesPageUrls.EDUCATION_SECTION_PAGE)
        page.open_page()
        page.click_initiatives_link()
        page.click_education_learn_more()
        question_headings = page.get_question_headings()
        page.click_question_headings(question_headings)
        page.verify_question_headings_clickable(question_headings)

    def test_010_01_01_1_text_on_button_learn_more(self, driver, open_and_load_main_page):
        our_initiatives = OurInitiativesPage(driver, OurInitiativesPageUrls.OUR_INITIATIVES_PAGE)
        our_initiatives.open_page()
        our_initiatives.click_initiatives_link()
        our_initiatives.check_text_on_button_learn_more()

    def test_tc_010_01_04_check_url_our_initiatives(self, driver, open_and_load_main_page):
        our_initiatives = OurInitiativesPage(driver, OurInitiativesPageUrls.OUR_INITIATIVES_PAGE)
        our_initiatives.open_page()
        our_initiatives.click_initiatives_link()
        our_initiatives.verify_correct_url_out_initiative()

    def test_010_02_02_check_title_student_initiatives(self, driver, open_and_load_main_page):
        our_initiatives = OurInitiativesPage(driver, OurInitiativesPageUrls.OUR_INITIATIVES_PAGE)
        our_initiatives.open_page()
        our_initiatives.click_initiatives_link()
        our_initiatives.verify_learn_more_link_redirects_to_valid_page()
