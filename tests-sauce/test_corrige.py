# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
import unittest, time, re

class LoginLogout(unittest.TestCase):

    def login(self, username, password):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").clear()
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
    
    # Fonction pour le processus de déconnexion
    def logout(self, driver):
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        driver.find_element(By.ID, "logout_sidebar_link").click()
        driver.implicitly_wait(10)
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test(self):
        driver = self.driver

        # Partie 1 - Login
        self.login("standard_user", "secret_sauce")

        # Partie 2 - Ajout Panier
        driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
        driver.find_element(By.ID,"add-to-cart-sauce-labs-fleece-jacket").click()
        driver.find_element(By.ID,"add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.XPATH,"//div[@id='shopping_cart_container']/a").click()

        elements_du_panier = driver.find_elements(By.XPATH, "//div[@id='cart_contents_container']/div/div/div[@class='cart_item']")
        assert len(elements_du_panier) == 3, "Le nombre d'éléments dans le panier n'est pas égal à 3"

        # Partie 3 - Modification Panier
        driver.find_element(By.ID, "remove-sauce-labs-bike-light").click()

        # Partie 4 - Logout
        self.logout(driver)
       
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

