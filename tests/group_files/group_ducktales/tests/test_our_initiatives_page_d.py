import pytest
from tests.group_files.group_ducktales.pages.our_initiatives_page import OurInitiativesPage


class TestOurInitiativesPage:

    @pytest.mark.parametrize("section", sections)
    def test_010_01_01_01_verify_sections(self, driver, open_and_load_main_page, section):
        page = OurInitiativesPage(driver, OUR_INITIATIVES_PAGE)
        page.open_page()
        page.click_initiatives_link()
        page.get_section_element(section)

    def test_010_01_02_02_functionality(self, driver, open_and_load_main_page):
        page = OurInitiativesPage(driver, EDUCATION_SECTION_PAGE)
        page.open_page()
        page.click_initiatives_link()
        page.click_education_learn_more()
        page.check_education_page_opened()

    def test_010_02_08_accessibility_of_question_headings(self, driver, open_and_load_main_page):
        page = OurInitiativesPage(driver, EDUCATION_SECTION_PAGE)
        page.open_page()
        page.click_initiatives_link()
        page.click_education_learn_more()
        question_headings = page.get_question_headings()
        page.verify_question_headings_displayed(question_headings)

    def test_010_02_09_clickability_of_question_headings(self, driver, open_and_load_main_page):
        page = OurInitiativesPage(driver, EDUCATION_SECTION_PAGE)
        page.open_page()
        page.click_initiatives_link()
        page.click_education_learn_more()
        question_headings = page.get_question_headings()
        page.click_question_headings(question_headings)
        page.verify_question_headings_clickable(question_headings)

