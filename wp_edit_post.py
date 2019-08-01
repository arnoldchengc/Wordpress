import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class wp_edit_post(unittest.TestCase):

    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.get("http://139.196.205.242:8000/wp-login.php")
        self.dr.maximize_window()

    def login(self, username, password):
        self.dr.find_element_by_css_selector("#user_login").send_keys(username)
        self.dr.find_element_by_css_selector("#user_pass").send_keys(password)
        self.dr.find_element_by_css_selector("#wp-submit").click()

    def test_edit_post(self):
        self.login(username="1940770824@qq.com", password="Summer@2019")

        # 进入所有文章列表
        self.dr.find_element_by_css_selector("li#menu-posts").click()

        # 点击文章列表的第一篇文章
        ele_first_post = WebDriverWait(self.dr, 10).until(
            EC.visibility_of(self.dr.find_element_by_css_selector("tbody#the-list >tr:nth-of-type(1)>td>strong>a")))
        ele_first_post.click()

        # 更新标题
        ele_title = WebDriverWait(self.dr, 10).until(
            EC.visibility_of(self.dr.find_element_by_css_selector("#title")))
        update_title = update_content = time.strftime("%y%m%d%H%M%S") + "update"
        ele_title.send_keys(update_title)
    
        # 更新内容
        self.dr.switch_to.frame("content_ifr")
        self.dr.find_element_by_css_selector("body#tinymce").send_keys(update_content)
    
        # 切回默认的iframe
        self.dr.switch_to.default_content()
		
		#点击更新
        self.dr.find_element_by_css_selector("input#publish[value='更新']").click()
    
        # 断言
        message = self.dr.find_element_by_css_selector("div#message").text
        self.assertTrue("文章已更新。" in message)


if __name__ == "__main__":
    unittest.main()
