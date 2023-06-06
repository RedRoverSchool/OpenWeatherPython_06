from pages.partners_page import PartnersPage
from test_data.urls import PartnersPageUrls


class TestPartnersPage:

    def test_tc_011_15_01_verify_correctly_redirected_the_link_apache_camel(self, driver, wait):
        page = PartnersPage(driver)
        apache_camel = PartnersPageUrls.APACHE_CAMEL_URL
        page.verify_redirected_the_link_apache_camel_to_a_new_window(apache_camel)

    def test_tc_011_15_02_verify_visibility_and_clickability_of_the_link_apache_camel(self, driver, wait):
        page = PartnersPage(driver)
        apache_camel = PartnersPageUrls.APACHE_CAMEL_URL
        page.verify_visibility_and_clickability_the_link_apache_camel_to_a_new_window(apache_camel)
