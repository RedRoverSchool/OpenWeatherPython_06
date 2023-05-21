'''
Basic methods that could be used among the project
'''
from selenium.common import WebDriverException
from selenium.webdriver.support.ui import Select
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
            EC.visibility_of_element_located(locator))

    """
    Method: find group of elements (array of elements)
    """

    def find_elements_array(self, locator):
        return self.driver.find_elements(locator)

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

    def check_element_selected(self, element):
        result = self.find_element(element).is_selected()
        print(f'Is element selected: {result}')
        return result

    """
    Method: check if the element is clickable or not
    """

    def check_clickable(self, element):
        try:
            self.find_element(element).click()
        except WebDriverException:
            print('Element is not clickable')

    """
    Method: select value from drop-down list
    For the web-elements: 
    <select>
        <option>
        <option>
    </select>
    """

    def select_option_from_list(self, locator, option):
        select = Select(self.find_element(locator))
        select.select_by_index(option)
        print(f'Item from drop-down selected')

    """
    Method: check element has property
    ("checked", "disabled", etc.)
    """

    def check_property(self, element, value):
        result = self.find_element(element).get_property(value)
        print(f'Is element has property {value}: {result}')
        return result

    """
    Method: verify preselected option:
    For the web-elements: 
    <select>
        <option>
        <option>
    </select> 
    """

    def check_preselected_option(self, element):
        select = Select(self.find_element(element))
        selected_option = select.first_selected_option
        return selected_option






