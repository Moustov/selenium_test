from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CodeSandbox:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.elements_root = {}
        self.elements_search = {}

    def open_page(self):
        self.driver.get("https://codesandbox.io/s/angularjs-17x-sandbox-5kdd3")

    def click_on_button_search(self):
        self.elements_root["button_search"] = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/button[2]')
        self.elements_root["button_search"].click()

    def click_on_button_explorer(self):
        self.elements_root["button_search"] = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/button[1]')
        self.elements_root["button_search"].click()

    def is_search_frame_activated(self) -> bool:
        try:
            self.elements_search["button_search_option"] = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div[2]')
        except NoSuchElementException as nsee:
            return False
        return self.elements_search["button_search_option"].is_displayed()

    def wait_for_button_search_option(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div[2]')))