from pages.base_page import BasePage



class Footer(BasePage):

    def check_privacy_policy_link_is_clickable(self):
        privacy_policy_link = self.element_is_clickable(self.privacy_policy_link)
        assert privacy_policy_link.is_displayed() and privacy_policy_link.is_enabled(), "The privacy policy link is " \
                                                                                        "not clickable "