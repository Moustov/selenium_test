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
        new_value = self.page.get_mouse_move_count()
        assert init_value != new_value

    def test_input_radio(self):
        init_value = self.page.get_input_radio_genre()
        assert init_value == "MALE"
        self.page.set_female_input_radio()
        new_value = self.page.get_input_radio_genre()
        assert new_value == "FEMALE"

    def test_datetime_local(self):
        init_value = self.page.get_datetime_local()
        assert init_value == ""
        self.page.set_datetime_local('2023-04-19T10:24:00')
        new_value = self.page.get_datetime_local()
        assert new_value == '2023-04-19T10:24'
        self.page.submit_datetime_local()
        assert "2023-04-19T10%3A24" in self.driver.current_url

    def test_range(self):
        init_value = self.page.get_range_value()
        assert init_value == 50
        self.page.set_range_value(5)
        new_value = self.page.get_range_value()
        assert new_value == 54
        self.page.set_range_value(-15)
        new_value = self.page.get_range_value()
        assert new_value == 39


    def tearDown(self):
        self.driver.close()

