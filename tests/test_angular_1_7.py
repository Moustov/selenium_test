from unittest import TestCase
from selenium import webdriver
from pom.codesandbox import CodeSandbox


class Testcodesandbox(TestCase):
    driver = None

    def setUp(self):
        if not self.driver:
            self.driver = webdriver.Firefox()
            self.page = CodeSandbox(self.driver)
            self.page.open_page()

    def test_button_search(self):
        assert not self.page.is_search_frame_activated()
        self.page.click_on_button_search()
        self.page.wait_for_button_search_option()
        assert self.page.is_search_frame_activated()

    def tearDown(self):
        self.driver.close()
