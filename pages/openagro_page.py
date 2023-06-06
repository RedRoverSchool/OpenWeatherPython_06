from pages.base_page import BasePage
from locators.locators import OpenAgroLocators


class OpenAgroPage(BasePage):

    def there_is_more_than_one_element_displayed_check(self, driver):
        elements = driver.find_elements(*OpenAgroLocators.REQUEST_DATA_LOCATORS)
        assert len(elements) >= 1

