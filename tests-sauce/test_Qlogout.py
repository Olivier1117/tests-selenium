# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Logout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID,"user-name").click()
        self.driver.find_element(By.ID,"user-name").clear()
        self.driver.find_element(By.ID,"user-name").send_keys("standard_login")
        self.driver.find_element(By.ID,"password").click()
        self.driver.find_element(By.ID,"password").clear()
        self.driver.find_element(By.ID,"password").send_keys("secret_sauce")
        self.driver.find_element(By.ID,"login-button").click()
        self.driver.find_element(By.ID,"password").click()
        self.driver.find_element(By.ID,"login-button").click()
        self.driver.find_element(By.XPATH,"(.//*[normalize-space(text()) and normalize-space(.)='Swag Labs'])[2]/following::*[name()='svg'][2]").click()
        self.driver.find_element(By.XPATH,"(.//*[normalize-space(text()) and normalize-space(.)='Swag Labs'])[2]/following::*[name()='svg'][2]").click()
        self.driver.find_element(By.ID,"login-button").click()
        self.driver.find_element(By.ID,"user-name").click()
        self.driver.find_element(By.XPATH,"//div[@id='login_button_container']/div/form").click()
        self.driver.find_element(By.ID,"password").click()
        self.driver.find_element(By.ID,"user-name").click()
        self.driver.find_element(By.ID,"user-name").clear()
        self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
        self.driver.find_element(By.ID,"password").click()
        self.driver.find_element(By.ID,"login-button").click()
    
    def test_logout(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/inventory.html")
        driver.save_screenshot("./data/Logout.png")
        driver.find_element(By.ID,"react-burger-menu-btn").click()
        driver.save_screenshot("./data/Logout-menu.png")
        driver.find_element(By.ID,"logout_sidebar_link").click()
        driver.save_screenshot("./data/Logout_done.png")
    
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
