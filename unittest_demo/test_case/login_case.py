import sys
from os.path import abspath, dirname

file_path = dirname(dirname(abspath(__file__)))
sys.path.insert(0, file_path)

import unittest
from selenium import webdriver
from page_obj.login_page import LoginPage
from page_obj.dashboard_page import DashboardPage


class LoginCase(unittest.TestCase):

    def setUp(self):
        print("before test")
        self.dr = webdriver.Chrome()
        self.dr.get("http://139.196.205.242:8000/wp-login.php")
        self.dr.maximize_window()

    def tearDown(self):
        print("after test")
        self.dr.quit()

    def test_login_success(self):
        username = '1940770824@qq.com'
        password = 'Summer@2019'
        login_page = LoginPage(self.dr)
        dashboard_page = login_page.login_success(username, password)
        self.assertTrue("mini2019" in dashboard_page.greeting_link().text)


if __name__ == '__main__':
    unittest.main()
