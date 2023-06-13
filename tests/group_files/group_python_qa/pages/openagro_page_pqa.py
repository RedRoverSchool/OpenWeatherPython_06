from pages.base_page import BasePage
from tests.group_files.group_python_qa.locators.locators import OpenAgroLocators


class OpeAgroPage(BasePage):

    locator = OpenAgroLocators()

    def there_is_more_than_one_element_displayed_check(self, driver):
        elements = driver.find_elements(*self.locator.REQUEST_DATA_LOCATOR)
        assert len(elements) >= 1
