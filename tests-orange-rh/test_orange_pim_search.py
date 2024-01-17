# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Test_orange_pim_search(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_orange_search(self):

        driver = self.driver

        # Connexion
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        
        time.sleep(5)
        driver.save_screenshot("./data/login.png")
        time.sleep(5)
        
        driver.find_element(By.NAME,"username").click()
        driver.find_element(By.NAME,"username").clear()
        driver.find_element(By.NAME,"username").send_keys("Admin")
        driver.find_element(By.NAME,"password").clear()
        driver.find_element(By.NAME,"password").send_keys("admin123")
        
        time.sleep(5)
        driver.save_screenshot("./data/login_admin.png")
        time.sleep(5)
        
        driver.find_element(By.XPATH,"//button[@type='submit']").click()

        # Navigation sur la page viewEmployeeList
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        
        time.sleep(5)
        driver.save_screenshot("./data/page_accueil_admin.png")
        time.sleep(5)
        
        driver.find_element(By.LINK_TEXT,"PIM").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
        
        time.sleep(5)
        driver.save_screenshot("./data/employee.png")
        time.sleep(5)

        #search employee
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/div/div/input").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/div/div/input").clear()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/div/div/input").send_keys("lambert")
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        
        # attente du chargement de la liste filtrée
        time.sleep(10)
        
        driver.save_screenshot("./data/employee_lambert.png")
        time.sleep(5)
    
        elements=driver.find_elements(By.CLASS_NAME, "oxd-table-card")
        print("Longueur: ",len(elements))
    
        self.assertEqual(len(elements), 1, "Recherche sans menu pas OK")
        
        
        #search avec menu déroulant
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/div/div/input").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/div/div/input").clear()
        #driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/div/div/input").send_keys("lambert")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div[6]/div/div[2]/div/div/div[2]/i").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div[6]/div/div[2]/div/div/div").click()
        
        time.sleep(10)
        
        driver.save_screenshot("./data/employee_lambert-chief.png")
        
        #filtre        
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        
        # attente du chargement de la liste filtrée
        time.sleep(10)
    
        elements=driver.find_elements(By.CLASS_NAME, "oxd-table-card")
        print("Longueur filtre: ",len(elements))
    
        self.assertEqual(len(elements), 1, "Recherche par menu pas OK")
        
        #logout
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/header/div/div[2]/ul/li/span/p").click()
        driver.find_element(By.LINK_TEXT,"Logout").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        
        time.sleep(5)
        driver.save_screenshot("./data/logout_admin.png")
        time.sleep(5)
        
        element=driver.find_elements(By.NAME,"username")
        #print("Find:",len(element))
        
        self.assertEqual(len(element), 1, "Logout pas OK") 
        
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
