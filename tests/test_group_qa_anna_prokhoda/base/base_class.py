'''
Basic methods that could be used among the project
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:

    def __init__(self, driver):
        self.driver = driver

    """
    Method: find element
    """

    def find_element(self, locator):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, locator)))

    """
    Method: find group of elements (array of elements)
    """

    def find_elements_array(self, locator):
        return self.driver.find_elements(by=By.XPATH, value=locator)

    """
    Method: input values, send_keys
    """

    def input_value(self, element, value):
        self.find_element(element).send_keys(value)
        print(f'Input: {value}')

    """
    Method: click element (e.g. button)
    """

    def click_element(self, element):
        self.find_element(element).click()
        print('Button clicked')

    """
    Method: get current url
    """

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current URL: {get_url}")
        return get_url

    """
    Method: assert current URL
    """

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result, \
            f'Wrong result:' \
            f'\nCurrent URL: "{self.get_current_url()}"' \
            f'\nURL expected: "{result}"'
        print(f"Current URL result: '{result}' --- PASSED")

    """
    Method: assert page text
    """

    def assert_text(self, text, result):
        value_text = text.text
        assert value_text == result, \
            f'Wrong result:' \
            f'\nThe message displayed: "{value_text}"' \
            f'\nThe message expected: "{result}"'
        print(f"Text result: '{result}' --- PASSED")

    """
    Method: check if element is enabled for selecting (True / False): 
    fields, radio buttons, etc.
    """

    def check_element_enabled(self, element):
        result = element.is_enabled()
        print(f'Is element enabled: {result})')
        return result

    """
    Method: check value of the elements attribute (
    e.g. checked="checked" for radio buttons; disabled="disabled" for fields)
    """

    def check_attributes(self, element, attribute, value):
        try:
            result = element.get_attribute(attribute)
            assert result == value, \
                                f'Wrong {attribute} value, the actual one is {result}, the required is {value}'
            return result
        except Exception:
            print("No such attribute")




