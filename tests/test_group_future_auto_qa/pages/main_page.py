from selenium.webdriver import ActionChains
import requests
import os
from pages.base_page import BasePage
from tests.test_group_future_auto_qa.locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    locators = MainPageLocators()

    def get_header_search_field_attribute(self, attribute):
        search_placeholder = self.driver.find_element(*self.locators.HEADER_SEARCH_FIELD)
        return search_placeholder.get_attribute(attribute)

    def fill_city_search_field(self, city):
        input_city = self.driver.find_element(*self.locators.HEADER_SEARCH_FIELD)
        input_city.send_keys(city)

    def click_header_search_field(self):
        self.driver.find_element(*self.locators.HEADER_SEARCH_FIELD).click()

    def click_support_nav_menu(self):
        return self.driver.find_element(*self.locators.SUPPORT_MENU).click()

    def click_faq_submenu(self, wait):
        submenu = wait.until(EC.visibility_of_element_located(self.locators.SUPPORT_FAQ_SUBMENU)).click()
        actions = ActionChains(self.driver)
        actions.click(submenu).perform()
        return submenu

    def faq_submenu_should_be_visible(self, wait):
        element = wait.until(EC.visibility_of_element_located(self.locators.SUPPORT_FAQ_SUBMENU))
        assert element.is_displayed() and element.is_enabled(), f'"{element}" link is not visible or clickable'

    def assert_current_url(self, expected_url):
        current_url = self.driver.current_url
        assert current_url == expected_url, f"URL does not match. Actual: {current_url}"

    def correct_header_is_displayed(self, text):
        element_text = self.driver.find_element(*self.locators.HEADER).text
        assert element_text == text, f'"{text}" is not present.'

    def click_footer_product_collections_widgets(self, expected_link):
        self.allow_all_cookies()
        widgets_link = self.element_is_clickable(self.locators.FOOTER_WIDGETS)
        link_href = widgets_link.get_attribute('href')
        assert link_href == expected_link, "Incorrect link"

    def how_to_start_submenu_should_be_visible(self, wait):
        element = wait.until(EC.visibility_of_element_located(self.locators.SUPPORT_HOW_TO_START_SUBMENU))
        assert element.is_displayed() and element.is_enabled(), f'"{element}" link is not visible or clickable'

    def click_how_to_start_submenu(self, wait):
        submenu = wait.until(EC.visibility_of_element_located(self.locators.SUPPORT_HOW_TO_START_SUBMENU)).click()
        actions = ActionChains(self.driver)
        actions.click(submenu).perform()
        return submenu


class MainPageFooter(BasePage):
    locators = MainPageLocators()

    def pdf_downloader(self, locator):
        pdf_url = self.element_is_clickable(locator).get_attribute("href")
        response = requests.get(pdf_url)
        pdf_filename = pdf_url[pdf_url.rfind("/") + 1:]
        path_to_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', f'test_data/{pdf_filename}'))
        with open(path_to_file, 'wb') as f:
            f.write(response.content)
            check_file = os.path.exists(path_to_file)
            f.close()
            os.remove(path_to_file)
        return pdf_filename,  path_to_file, check_file

    def verify_pdf_downloading_after_click_on_terms_and_conditions_of_sale_link(self):
        self.allow_all_cookies()
        pdf_filename,  path_to_file, check_file = self.pdf_downloader(self.locators.FOOTER_TERMS_AND_CONDITIONS_OF_SALE)
        assert check_file is True, f"PDF file '{pdf_filename}' was not downloaded to {path_to_file}"

    def verify_pdf_downloading_after_click_on_website_terms_and_conditions_link(self):
        self.allow_all_cookies()
        pdf_filename,  path_to_file, check_file = self.pdf_downloader(self.locators.FOOTER_WEBSITE_TERMS_AND_CONDITIONS)
        assert check_file is True, f"PDF file '{pdf_filename}' was not downloaded to {path_to_file}"

    def verify_terms_and_conditions_module_title_visibility(self):
        terms_and_conditions_module_title = \
            self.driver.find_element(*self.locators.FOOTER_TERMS_AND_CONDITIONS_TITLE)
        assert terms_and_conditions_module_title.is_displayed(), \
            "The Terms & Conditions module title is not visible"

    def check_blog_link_functionality(self, expected_link):
        self.allow_all_cookies()
        blog_link = self.element_is_clickable(self.locators.FOOTER_BLOG_LINK)
        link_href = blog_link.get_attribute('href')
        assert link_href == expected_link, "Incorrect link"

    def click_footer_product_collections_all_widgets(self, expected_link, link_number):
        self.allow_all_cookies()
        widgets_link = self.element_is_clickable(self.locators.product_collection[link_number])
        print(f'widgets_link = {widgets_link}')
        link_href = widgets_link.get_attribute('href')
        print(f'link_href = {link_href}')
        print(f'expected_link = {expected_link}')
        assert link_href in expected_link, "Incorrect link"
