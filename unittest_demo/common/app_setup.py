import sys
from os.path import abspath, dirname

file_path = dirname(dirname(abspath(__file__)))
sys.path.insert(0, file_path)

import unittest
from selenium import webdriver


class AppSetUp(unittest.TestCase):

    def setUp(self):
        print("before test")
        self.dr = webdriver.Chrome()
        self.dr.implicitly_wait(10)
        self.dr.get("http://139.196.205.242:8000/wp-login.php")
        self.dr.maximize_window()

    def tearDown(self):
        print("after test")
        self.dr.quit()
