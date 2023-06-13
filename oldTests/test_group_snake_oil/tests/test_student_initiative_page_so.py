from oldTests.test_group_snake_oil.links.all_links import StudentInitiativePageLinks
from oldTests.test_group_snake_oil.pages.student_initiative_page import StudentInitiativePage


class TestStudentInitiativePage:
    links = StudentInitiativePageLinks

    def test_tc_010_02_03_verify_the_learn_more_link_redirection_for_the_developer_plan(self, driver):
        student_initiative_page = StudentInitiativePage(driver, self.links.STUDENT_INITIATIVE_PAGE_URL)
        student_initiative_page.open_page()
        student_initiative_page.allow_all_cookies()
        current_url = student_initiative_page.click_the_learn_more_link_for_the_developer_plan()
        student_initiative_page.verify_page_redirection_for_plan(current_url,
                                                                 self.links.PRICING_PAGE_URL_FOR_DEVELOPER_PLAN)

    def test_tc_010_02_04_verify_the_learn_more_link_redirection_for_the_medium_plan(self, driver):
        student_initiative_page = StudentInitiativePage(driver, self.links.STUDENT_INITIATIVE_PAGE_URL)
        student_initiative_page.open_page()
        student_initiative_page.allow_all_cookies()
        current_url = student_initiative_page.click_the_learn_more_link_for_the_medium_plan()
        student_initiative_page.verify_page_redirection_for_plan(current_url,
                                                                 self.links.PRICING_PAGE_URL_FOR_MEDIUM_PLAN)
