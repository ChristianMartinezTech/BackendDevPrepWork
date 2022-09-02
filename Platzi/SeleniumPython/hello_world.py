#!/usr/bin/env python3
"""First contact with Selenium"""


import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class HelloWorld(unittest.TestCase):
    """Class HelloWorld"""
    
    @classmethod 
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_World(self):
        driver = self.driver
        driver.get('https://platzi.com/')

    def tearDown(self):
        return super().tearDown()


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reports', report_name='hello_world_report'))
