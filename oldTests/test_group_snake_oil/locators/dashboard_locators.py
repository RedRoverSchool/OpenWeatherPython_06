from selenium.webdriver.common.by import By


class DashboardPageLocators:
    # 'How to Start' section

    # text-links locators
    SIGN_UP_LINK = (By.XPATH, ".//a[b='Sign up']")
    USERNAME_AND_PASSWORD_LINK = (By.XPATH, "//a[text()='OpenWeather username and password']")
    GO_TO_DASHBOARD_LINK = (By.XPATH, ".//a[b='Go to the Dashboard']")
    EVENTS_SECTION_LINK = (By.XPATH, "//a[contains(text(), 'section')]")
    NEW_TRIGGER_SECTION_LINK = (By.XPATH, ".//a[b='Go to the \"New trigger\" section']")
    HERE_LINK = (By.XPATH, "//a[text()='here']")
    DETAILED_USER_MANUAL_LINK = (By.XPATH, ".//a[b='detailed user manual']")
    TRY_THE_DASHBOARD_BUTTON = (By.XPATH, "(//a[text()='Try the Dashboard'])[2]")

    # 7 links + 1 button
    ALL_TEXT_LINK_LOCATORS = [SIGN_UP_LINK, USERNAME_AND_PASSWORD_LINK, GO_TO_DASHBOARD_LINK, EVENTS_SECTION_LINK,
                              NEW_TRIGGER_SECTION_LINK,
                              HERE_LINK, DETAILED_USER_MANUAL_LINK, TRY_THE_DASHBOARD_BUTTON]
