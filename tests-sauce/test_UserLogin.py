# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class StandardLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_standard_login(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.save_screenshot("./data/Login.png")
        driver.find_element(By.ID,"user-name").click()
        driver.find_element(By.ID,"user-name").clear()
        driver.find_element(By.ID,"user-name").send_keys("standard_login")
        driver.find_element(By.ID,"password").click()
        driver.find_element(By.ID,"password").clear()
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        driver.save_screenshot("./data/Login-pwd.png")
        driver.find_element(By.ID,"login-button").click()
        driver.find_element(By.ID,"password").click()
        driver.find_element(By.ID,"login-button").click()
        driver.find_element(By.XPATH,"(.//*[normalize-space(text()) and normalize-space(.)='Swag Labs'])[2]/following::*[name()='svg'][2]").click()
        driver.find_element(By.XPATH,"(.//*[normalize-space(text()) and normalize-space(.)='Swag Labs'])[2]/following::*[name()='svg'][2]").click()
        driver.find_element(By.ID,"login-button").click()
        driver.find_element(By.ID,"user-name").click()
        driver.find_element(By.XPATH,"//div[@id='login_button_container']/div/form").click()
        driver.find_element(By.ID,"password").click()
        driver.find_element(By.ID,"user-name").click()
        driver.find_element(By.ID,"user-name").clear()
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        driver.find_element(By.ID,"password").click()
        driver.find_element(By.ID,"login-button").click()
        driver.save_screenshot("./data/Login_done.png")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
