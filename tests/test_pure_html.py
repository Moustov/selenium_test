from unittest import TestCase
from selenium import webdriver
from caipture_com_demo_samples import CaiptureComDemoSamples


class TestCaiptureComDemoSamples(TestCase):
    driver = None

    def setUp(self):
        if not self.driver:
            self.driver = webdriver.Firefox()
            self.page = CaiptureComDemoSamples(self.driver)
            self.page.open_page()

    def test_button_calc(self):
        self.page.click_cal_button("1")
        self.page.click_cal_button("+")
        self.page.click_cal_button("2")
        self.page.click_cal_button("=")
        assert self.page.get_calc_field_value() == "3"

    def test_input_field_calc(self):
        self.page.set_calc_field_value("99")
        self.page.click_cal_button("+")
        self.page.set_calc_field_value("1")
        self.page.click_cal_button("=")
        assert self.page.get_calc_field_value() == "100"

    def test_click_text(self):
        assert self.page.get_mouse_down_linked_text_status() == ""
        self.page.click_on_mouse_down()
        assert self.page.get_mouse_down_linked_text_status() == "OK"

    def test_file_submit(self):
        self.page.click_file_browse(r"C:\Users\chris\Agilitest-Editor\agilitest-app.xml")
        self.page.click_file_upload()
        assert "agilitest-app.xml" in self.driver.current_url

    def tearDown(self):
        self.driver.close()
