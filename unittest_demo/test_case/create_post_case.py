import sys
from os.path import abspath, dirname

file_path = dirname(dirname(abspath(__file__)))
sys.path.insert(0, file_path)

import time
from common.app_setup import AppSetUp
from page_obj.login_page import LoginPage
from page_obj.post_page import PostPage


class CreatePostCase(AppSetUp):

    def test_create_post(self):
        username = '1940770824@qq.com'
        password = 'Summer@2019'
        login_page = LoginPage(self.dr)
        dashboard_page = login_page.login_success(username, password)
        post_detail_page = dashboard_page.click_create_new_post()
        title = content = time.strftime("%Y%m%d%H%M%S")
        post_detail_page.update_post_title(title)
        post_detail_page.update_post_content(content)
        post_detail_page.publish_post()
        post_page = PostPage(self.dr)
        post_page.click_all_post()
        self.assertTrue(title, post_page.first_post().text)
