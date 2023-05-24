from pages.base_page import BasePage
from tests.test_group_bugs_in_each_step.locators.sign_in_page_locators import *
import requests
import time
import os


class SignInPage(BasePage):
    locators = SignInPageLocators()

    def sample_function(self):
        return self

    def check_registration_question_is_visible(self):
        registration_question = self.element_is_visible(self.locators.REGISTRATION_QUESTION)
        return registration_question.is_displayed()

