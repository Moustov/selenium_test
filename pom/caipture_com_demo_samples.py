from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class CaiptureComDemoSamples:
    """
    https://selenium-python.readthedocs.io/api.html
    """

    def __init__(self, driver: webdriver):
        self.css_selector_for_color_picker = "body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > form:nth-child(2) > input:nth-child(1)"
        self.alert = None
        self.driver = driver
        self.calc_button_xpaths = {"CE": "/html/body/table/tbody/tr[1]/td[1]/form/table/tbody/tr[2]/td[1]/input",
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
        self.mouse_events_xpaths = {"Mouse Down Area": "/html/body/table/tbody/tr[1]/td[2]/table[2]/tbody/tr[4]/td[1]/span",
                                    "Mouse Down Linked Text": '//*[@id="mousedownbutton"]'}
        self.elements = {}

    def open_page(self):
        self.driver.get("https://www.caipture.com/demo/samples.html")

    def click_cal_button(self, name: str):
        self.elements[name] = self.driver.find_element(By.XPATH,self.calc_button_xpaths[name])
        self.elements[name].click()

    def get_calc_field_value(self) -> str:
        self.elements["field_value"] = self.driver.find_element(By.XPATH, self.calc_button_xpaths["field_value"])
        return self.elements["field_value"].get_attribute('value')

    def set_calc_field_value(self, value: str):
        self.elements["field_value"] = self.driver.find_element(By.XPATH, self.calc_button_xpaths["field_value"])
        return self.elements["field_value"].send_keys(value)

    def click_on_mouse_down(self):
        self.elements["Mouse Down Area"] = self.driver.find_element(By.XPATH,self.mouse_events_xpaths["Mouse Down Area"])
        self.elements["Mouse Down Area"].click()

    def click_on_color_button(self):
        self.elements["Color selector"] = self.driver.find_element(By.CSS_SELECTOR, self.css_selector_for_color_picker)
        self.elements["Color selector"].click()

    def define_color(self, red: str, green: str, blue: str):
        self.driver.execute_script(f"document.querySelector('{self.css_selector_for_color_picker}').value='#{red}{green}{blue}'")

    def get_mouse_down_linked_text_status(self):
        self.elements["Mouse Down Linked Text"] = self.driver.find_element(By.ID,"mousedownbutton")
        return self.elements["Mouse Down Linked Text"].get_attribute('innerHTML')

    def click_file_browse(self, file_path: str):
        self.elements["file browse"] = self.driver.find_element(By.NAME,'file')
        self.elements["file browse"].send_keys(file_path)

    def click_file_upload(self):
        self.elements["submit file"] = self.driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td[3]/form/input[2]')
        self.elements["submit file"].click()

    def click_on_submit_color(self):
        self.elements["submit color"] = self.driver.find_element(By.CSS_SELECTOR,
                                                                'body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > form:nth-child(2) > input:nth-child(3)')
        self.elements["submit color"].click()

    def mouse_enter_area(self):
        element = self.driver.find_element(By.CSS_SELECTOR, 'body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(1) > span:nth-child(1)')
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def get_mouse_enter_area_status(self) -> str:
        element = self.driver.find_element(By.CSS_SELECTOR, '#onmouseenter')
        return element.get_attribute('innerHTML')

    def mouse_move_area(self, x: int, y: int):
        element = self.driver.find_element(By.CSS_SELECTOR, 'body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(7) > td:nth-child(1) > span:nth-child(1)')
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()
        action.move_by_offset(x, y).perform()

    def get_mouse_move_count(self) -> str:
        element = self.driver.find_element(By.CSS_SELECTOR, '#onmousemove')
        return element.get_attribute('value')

