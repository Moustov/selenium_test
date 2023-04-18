from pathlib import Path
from unittest import TestCase
from selenium import webdriver
from pom.caipture_com_demo_samples import CaiptureComDemoSamples


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
        self.page.click_file_browse(__file__)
        self.page.click_file_upload()
        assert Path(__file__).name in self.driver.current_url

    def test_color_selection(self):
        self.page.click_on_color_button()
        self.page.define_color("FF", "BB", "99")
        self.page.click_on_submit_color()
        print(self.driver.current_url)
        assert "23ffbb99" in self.driver.current_url

    def test_mouse_enter_area(self):
        res = self.page.get_mouse_enter_area_status()
        assert res != "OK"
        self.page.mouse_enter_area()
        res = self.page.get_mouse_enter_area_status()
        assert res == "OK"

    def test_mouse_move_area(self):
        init_value = self.page.get_mouse_move_count()
        self.page.mouse_move_area(1, 1)
        self.page.mouse_move_area(1, 1)
        res = self.page.get_mouse_move_count()
        assert init_value != res

    def tearDown(self):
        self.driver.close()
