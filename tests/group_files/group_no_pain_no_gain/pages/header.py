from .main_page import MainPage


class Header(MainPage):
    def link_leads_to_page_with_correct_header(self, locator, result_header_locator):
        element = self.driver.find_element(*locator)
        element_text = element.text
        element.click()
        header_text = self.driver.find_element(*result_header_locator).text
        assert element_text in header_text, \
            f'{element_text} link leads to a page with an incorrect header'
