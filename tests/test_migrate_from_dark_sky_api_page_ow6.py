from pages.migrate_from_dark_sky_api_page import MigrateFromDarkSkyApiPage
from test_data.urls import MigratePageUrls


class TestMigrateFromDarkSkyApiPage:
    def test_001_18_01_verify_subscribe_link_redirection(self, driver, wait):
        page = MigrateFromDarkSkyApiPage(driver)
        migrate_page = MigratePageUrls.URL_SIGN_UP
        page.verify_subscribe_for_free_link_redirection(migrate_page)
