import sys
from os.path import abspath, dirname

file_path = dirname(dirname(abspath(__file__)))
sys.path.insert(0, file_path)

import unittest
import time
from selenium import webdriver
from page_obj.login_page import LoginPage
from page_obj.post_page import PostPage


class CreatePostCase(unittest.TestCase):

    def setUp(self):
        print("before test")
        self.dr = webdriver.Chrome()
        self.dr.get("http://139.196.205.242:8000/wp-login.php")
        self.dr.maximize_window()

    def tearDown(self):
        print("after test")
        self.dr.quit()

    def test_create_post(self):
        username = '1940770824@qq.com'
        password = 'Summer@2019'
        login_page = LoginPage(self.dr)
        dashboard_page = login_page.login_success(username, password)
        post_detail_page = dashboard_page.click_create_new_post()
        title = content = time.strftime("%y%m%d%H%M%S")
        post_detail_page.update_post_title(title)
        post_detail_page.update_post_content(content)
        post_detail_page.publish_post()
        post_page = PostPage(self.dr)
        post_page.click_all_post()
        self.assertTrue(title, post_page.first_post().text)


if __name__ == "__main__":
    unittest.main()
