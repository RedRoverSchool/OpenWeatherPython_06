from pages.student_initiatives_page import StudentInitiativePage


class TestStudentInitiativePage:

    def test_tc_010_02_06_verify_website_link_redirects_to_main_page(self, driver, wait):
        student_initiative_page = StudentInitiativePage(driver, link='https://openweathermap.org/our-initiatives/student-initiative')
        student_initiative_page.open_page()
        student_initiative_page.verify_website_link_redirects_to_main_page(wait=wait)

    def test_tc_010_02_07_verify_correct_redirection_to_popup_window(self, driver, wait):
        student_initiative_page = StudentInitiativePage(driver, link='https://openweathermap.org/our-initiatives/student-initiative')
        student_initiative_page.open_page()
        student_initiative_page.verify_correct_redirection_to_popup_window(wait=wait)
