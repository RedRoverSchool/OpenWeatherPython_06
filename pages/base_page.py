from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from locators.locators import BasePageLocators


class BasePage:
    locators = BasePageLocators()

    def __init__(self, driver, link=None):
        self.driver = driver
        self.link = link

    def open_page(self):
        self.driver.get(self.link)

    def click_header_link(self, link_name):
        match link_name:
            case 'sign':
                self.driver.find_element(*self.locators.SIGN_IN_LINK).click()
            case 'guide':
                self.driver.find_element(*self.locators.GUIDE_LINK).click()
            case 'dashboard':
                self.driver.find_element(*self.locators.DASHBOARD_LINK).click()
            case 'pricing':
                self.driver.find_element(*self.locators.PRICING_LINK).click()
            case 'faq':
                self.driver.find_element(*self.locators.SUPPORT_LINK).click()
                self.driver.find_element(*self.locators.FAQ_OPTION).click()
            case 'maps':
                self.driver.find_element(*self.locators.MAPS_LINK).click()
            case 'our initiatives':
                self.driver.find_element(*self.locators.OUR_INITIATIVES_LINK).click()
            case 'partners':
                self.driver.find_element(*self.locators.PARTNERS_LINK).click()
            case 'how to start':
                self.driver.find_element(*self.locators.SUPPORT_LINK).click()
                self.driver.find_element(*self.locators.HOW_TO_START_OPTION).click()
            case 'ask a question':
                self.driver.find_element(*self.locators.SUPPORT_LINK).click()
                self.driver.find_element(*self.locators.ASK_A_QUESTION_OPTION).click()
                window_after = self.driver.window_handles[1]
                self.driver.switch_to.window(window_after)
            case 'api':
                self.driver.find_element(*self.locators.API_LINK).click()


    def check_header_link(self, link_name):
        self.click_header_link(link_name)
        assert link_name in self.driver.current_url

    def element_is_displayed(self, locator, wait):
        try:
            wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def element_is_visible(self, locator, timeout=5):
        """
        Ожидает проверку, что элемент присутствует в DOM-дереве, виден и отображается на странице.
        Видимость означает, что элемент не только отображается,
        но также имеет высоту и ширину больше 0.
        Локатор - используется для поиска элемента. Возвращает WebElement.
        Timeout - время в течение которого он будет ожидать. По умолчанию стоит 5 секунд,
        при необходимости можно будет изменить.
        """
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        """
        Ожидает проверку, что элементы присутствуют в DOM-дереве, видны и отображаются на странице.
        Видимость означает, что элементы не только отображаются,
        но также имеет высоту и ширину больше 0.
        Локатор - используется для поиска элементов. Возвращает WebElements.
        Timeout - время в течение которого он будет ожидать. По умолчанию стоит 5 секунд,
        при необходимости можно будет изменить.
        """
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        """
        Ожидает проверку, что элемент присутствует в DOM-дереве, но не обязательно,
        что виден и отображается на странице.
        Локатор - используется для поиска элемента. Возвращает WebElement.
        Timeout - время в течение которого он будет ожидать. По умолчанию стоит 5 секунд,
        при необходимости можно будет изменить.
        """
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        """
        Ожидает проверку, что элементы присутствуют в DOM-дереве, но не обязательно,
        что видны и отображаются на странице.
        Локатор - используется для поиска элемента. Возвращает WebElement.
        Timeout - время в течение которого он будет ожидать. По умолчанию стоит 5 секунд,
        при необходимости можно будет изменить.
        """
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        """
        Ожидает проверку, является ли элемент невидимым или нет. Элемент присутствует в DOM-дереве.
        Локатор - используется для поиска элемента. Возвращает WebElement.
        Timeout - время в течение которого он будет ожидать. По умолчанию стоит 5 секунд,
        при необходимости можно будет изменить.
        """
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        """
        Ожидает проверку, что жлемент виден, отображается на странице,
        а также элемент включен. Элемент присутствует в DOM-дереве.
        Локатор - используется для поиска элемента.
        Timeout - время в течение которого он будет ожидать. По умолчанию стоит 5 секунд,
        при необходимости можно будет изменить.
        """
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        """
        Проскроливет страницу к выбранному элементы, так, чтобы элемент стал видимым пользователю.
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_move_to_element(self, element):
        """
        Двигает курсор мышки на середину выбранного элемента
        Имитирует hover.
        Можно использовать для проверки интерактивности элемента при наведении
        курсора мышки на элемент.
        """
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def press_enter_button(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER).perform()

    def allow_all_cookies(self, timeout=10):
        wait(self.driver, timeout).until(EC.element_to_be_clickable(self.locators.ALLOW_ALL_COOKIES_BUTTON)).click()

    def title_check(self, text=None):
        assert self.driver.title == text, "Title is NOT correct"

    def find_element_and_click(self, locator):
        self.driver.find_element(*locator).click()

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_for_redirection(self, expected_url):
        assert self.driver.current_url == expected_url

    def find_element(self, locator):
        return self.driver.find_element(*locator)

