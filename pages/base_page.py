from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys


class BasePage:
    sign_in_link = (By.CSS_SELECTOR, '.user-li a')
    guide_link = (By.CSS_SELECTOR, "#desktop-menu a[href*='guide']")
    dashboard_link = (By.CSS_SELECTOR, "#desktop-menu [href$=-dashboard]")
    pricing_link = (By.XPATH, '//div[@id="desktop-menu"]//a[text()="Pricing"]')
    allow_all_cookies_button = (By.XPATH, "//button[contains(text(), 'Allow all')]")
    privacy_policy_link = (By.CSS_SELECTOR, 'div.section-content ul li:nth-child(2) a[href*="privacy-policy"]')

    support_link = (By.XPATH, "//*[@id='support-dropdown']")
    faq_option = (By.XPATH, "//*[@id='support-dropdown-menu']//a[@href='/faq']")
    maps_link = (By.CSS_SELECTOR, '#desktop-menu ul li:nth-child(6) a')
    how_to_start_option = (By.XPATH, "//*[@id='support-dropdown-menu']//a[@href='/appid']")

    def __init__(self, driver, link=None):
        self.driver = driver
        self.link = link

    def open_page(self):
        self.driver.get(self.link)

    def click_header_link(self, link_name):
        match link_name:
            case 'sign':
                self.driver.find_element(*self.sign_in_link).click()
            case 'guide':
                self.driver.find_element(*self.guide_link).click()
            case 'dashboard':
                self.driver.find_element(*self.dashboard_link).click()
            case 'pricing':
                self.driver.find_element(*self.pricing_link).click()
            case 'faq':
                self.driver.find_element(*self.support_link).click()
                self.driver.find_element(*self.faq_option).click()
            case 'maps':
                self.driver.find_element(*self.maps_link).click()

            case 'faq':
                self.driver.find_element(*self.support_link).click()
                self.driver.find_element(*self.faq_option).click()
            case 'how to start':
                self.driver.find_element(*self.support_link).click()
                self.driver.find_element(*self.how_to_start_option).click()

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
        wait(self.driver, timeout).until(EC.element_to_be_clickable(self.allow_all_cookies_button)).click()

    def title_check(self, text=None):
        assert self.driver.title == text, "Title is NOT correct"
