from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CaiptureComDemoSamples:
    """
    https://selenium-python.readthedocs.io/api.html
    """

    def __init__(self, driver: webdriver):
        self.alert = None
        self.driver = driver
        self.css_selector_for_color_picker = "body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > " \
                                             "td:nth-child(2) > form:nth-child(2) > input:nth-child(1)"
        self.xpath_calc_buttons = {"CE": "/html/body/table/tbody/tr[1]/td[1]/form/table/tbody/tr[2]/td[1]/input",
                                   "<-": "/html/body/table/tbody/tr[1]/td[1]/form/table/tbody/tr[2]/td[2]/input",
                                   "%": "/html/body/table/tbody/tr[1]/td[1]/form/table/tbody/tr[2]/td[3]/input",
                                   "+": "/html/body/table/tbody/tr[1]/td[1]/form/table/tbody/tr[2]/td[4]/input",
                                   "0": "/html/body/table/tbody/tr[1]/td[1]/form/table/tbody/tr[6]/td[1]/input",
                                   "1": "/html/body/table/tbody/tr[1]/td[1]/form/table/tbody/tr[5]/td[1]/input",
                                   "2": "/html/body/table/tbody/tr[1]/td[1]/form/table/tbody/tr[5]/td[2]/input",
                                   "3": "",
                                   "4": "",
                                   "5": "",
                                   "6": "",
                                   "7": "",
                                   "8": "",
                                   "9": "",
                                   "+-": "",
                                   ",": "",
                                   "-": "",
                                   "*": "",
                                   "/": "",
                                   "=": "/html/body/table/tbody/tr[1]/td[1]/form/table/tbody/tr[6]/td[4]/input",
                                   "field_value": '//*[@id="calc_resultat"]'}
        self.xpath_mouse_events = {"Mouse Down Area": "/html/body/table/tbody/tr[1]/td[2]/table[2]/tbody/tr[4]"
                                                      "/td[1]/span",
                                    "Mouse Down Linked Text": '//*[@id="mousedownbutton"]'}
        self.css_selector_mouse_move_area = 'body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > ' \
                                            'td:nth-child(2) > table:nth-child(3) > tbody:nth-child(1) > ' \
                                            'tr:nth-child(7) > td:nth-child(1) > span:nth-child(1)'
        self.xpath_submit_file = '/html/body/table/tbody/tr[3]/td[3]/form/input[2]'
        self.id_mouse_down_linked_text_status = "mousedownbutton"
        self.css_selector_submit_color = 'body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > ' \
                                         'td:nth-child(2) > form:nth-child(2) > input:nth-child(3)'
        self.css_selector_mouse_enter_area = 'body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > ' \
                                             'td:nth-child(2) > table:nth-child(3) > tbody:nth-child(1) > ' \
                                             'tr:nth-child(5) > td:nth-child(1) > span:nth-child(1)'
        self.css_selector_mouse_enter_area_status = '#onmouseenter'
        self.css_selector_mouse_move_area_count = '#onmousemove'
        self.css_selector_input_radio_male = "body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > " \
                                             "td:nth-child(1) > form:nth-child(2) > input:nth-child(1)"
        self.css_selector_input_radio_female = "body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > " \
                                               "td:nth-child(1) > form:nth-child(2) > input:nth-child(3)"
        self.css_selector_input_radio_genre_other = "body > table:nth-child(1) > tbody:nth-child(1) > " \
                                                    "tr:nth-child(2) > td:nth-child(1) > form:nth-child(2) > " \
                                                    "input:nth-child(5)"
        self.css_selector_datetime_local = "body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > " \
                                           "td:nth-child(1) > form:nth-child(2) > input:nth-child(1)"
        self.css_selector_submit_radio_female = "body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > " \
                                                "td:nth-child(1) > form:nth-child(2) > input:nth-child(3)"
        self.css_selector_submit_datetime_local = 'body > table:nth-child(1) > tbody:nth-child(1) > ' \
                                                  'tr:nth-child(3) > td:nth-child(1) > form:nth-child(2) > ' \
                                                  'input:nth-child(3)'
        self.css_selector_range = "body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(5) > " \
                                  "td:nth-child(2) > form:nth-child(2) > input:nth-child(1)"

        self.elements = {}

    def open_page(self):
        self.driver.get("https://www.caipture.com/demo/samples.html")

    def click_cal_button(self, name: str):
        self.elements[name] = self.driver.find_element(By.XPATH, self.xpath_calc_buttons[name])
        self.elements[name].click()

    def get_calc_field_value(self) -> str:
        self.elements["field_value"] = self.driver.find_element(By.XPATH, self.xpath_calc_buttons["field_value"])
        return self.elements["field_value"].get_attribute('value')

    def set_calc_field_value(self, value: str):
        self.elements["field_value"] = self.driver.find_element(By.XPATH, self.xpath_calc_buttons["field_value"])
        return self.elements["field_value"].send_keys(value)

    def click_on_mouse_down(self):
        self.elements["Mouse Down Area"] = self.driver.find_element(By.XPATH, self.xpath_mouse_events["Mouse Down Area"])
        self.elements["Mouse Down Area"].click()

    def click_on_color_button(self):
        self.elements["Color selector"] = self.driver.find_element(By.CSS_SELECTOR, self.css_selector_for_color_picker)
        self.elements["Color selector"].click()

    def define_color(self, red: str, green: str, blue: str):
        self.driver.execute_script(f"document.querySelector('{self.css_selector_for_color_picker}').value='#{red}{green}{blue}'")

    def get_mouse_down_linked_text_status(self):
        self.elements["Mouse Down Linked Text"] = self.driver.find_element(By.ID, self.id_mouse_down_linked_text_status)
        return self.elements["Mouse Down Linked Text"].get_attribute('innerHTML')

    def click_file_browse(self, file_path: str):
        self.elements["file browse"] = self.driver.find_element(By.NAME,'file')
        self.elements["file browse"].send_keys(file_path)

    def click_file_upload(self):
        self.elements["submit file"] = self.driver.find_element(By.XPATH, self.xpath_submit_file)
        self.elements["submit file"].click()

    def click_on_submit_color(self):
        self.elements["submit color"] = self.driver.find_element(By.CSS_SELECTOR, self.css_selector_submit_color)
        self.elements["submit color"].click()

    def mouse_enter_area(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.css_selector_mouse_enter_area)
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def get_mouse_enter_area_status(self) -> str:
        element = self.driver.find_element(By.CSS_SELECTOR, self.css_selector_mouse_enter_area_status)
        return element.get_attribute('innerHTML')

    def mouse_move_area(self, x: int, y: int):
        element = self.driver.find_element(By.CSS_SELECTOR, self.css_selector_mouse_move_area)
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()
        action.move_by_offset(x, y).perform()

    def get_mouse_move_count(self) -> str:
        element = self.driver.find_element(By.CSS_SELECTOR, self.css_selector_mouse_move_area_count)
        return element.get_attribute('value')

    def get_input_radio_genre(self) -> str:
        element = self.driver.find_element(By.CSS_SELECTOR,self.css_selector_input_radio_male)
        is_male = element.is_selected()
        if is_male:
            return "MALE"
        element = self.driver.find_element(By.CSS_SELECTOR, self.css_selector_input_radio_female)
        is_female = element.is_selected()
        if is_female:
            return "FEMALE"
        element = self.driver.find_element(By.CSS_SELECTOR, self.css_selector_input_radio_genre_other)
        is_other = element.is_selected()
        if is_other:
            return "OTHER"
        return "NO DEFAULT VALUE"

    def set_female_input_radio(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.css_selector_input_radio_female)
        element.click()

    def set_datetime_local(self, datetime: str):
        wait = WebDriverWait(self.driver, 5)
        date = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.css_selector_datetime_local)))
        # self.driver.execute_script(f"arguments[0].setAttribute('value', {datetime})")
        self.driver.execute_script(f"arguments[0].value = '{datetime}';", date)

    def get_datetime_local(self) -> str:
        """
        todo get_datetime_local
        :return:
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.css_selector_datetime_local)
        res = element.get_attribute('value')
        return res

    def submit_datetime_local(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.css_selector_submit_datetime_local)
        element.click()

    def get_range_value(self) -> int:
        element = self.driver.find_element(By.CSS_SELECTOR, self.css_selector_range)
        res = element.get_attribute('value')
        return int(res)

    def set_range_value(self, new_value: int):
        # alternative : https://stackoverflow.com/questions/12122824/slider-movement-possible-in-selenium
        element = self.driver.find_element(By.CSS_SELECTOR, self.css_selector_range)
        move = ActionChains(self.driver)
        move.click_and_hold(element).move_by_offset(new_value, 0).release().perform()

