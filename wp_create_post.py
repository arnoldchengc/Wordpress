import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class wp_create_post(unittest.TestCase):

    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.get("http://139.196.205.242:8000/wp-login.php")
        self.dr.maximize_window()

    def login(self, username, password):
        self.dr.find_element_by_css_selector("#user_login").send_keys(username)
        self.dr.find_element_by_css_selector("#user_pass").send_keys(password)
        self.dr.find_element_by_css_selector("#wp-submit").click()

    def test_create_post(self):
        self.login(username='1940770824@qq.com', password='Summer@2019')

        # 定位新建文章的元素
        create_new_post = self.dr.find_element_by_css_selector("#wp-admin-bar-new-content")
        ActionChains(self.dr).move_to_element(create_new_post).perform()

        # 等待悬浮的元素出现
        WebDriverWait(self.dr, 10).until(
            EC.visibility_of(self.dr.find_element_by_css_selector("#wp-admin-bar-new-post")))

        # 点击创建新文章
        self.dr.find_element_by_css_selector("#wp-admin-bar-new-post").click()

        # 填写文章标题和内容
        title = content = time.strftime("%Y%m%d%H%M%S")
        self.dr.find_element_by_css_selector("#title").send_keys(title)
        js = "document.getElementById('content_ifr').contentWindow.document.body.innerHTML = '{}'"
        res = js.format(content)
        self.dr.execute_script(res)

        # 发布文章
        self.dr.find_element_by_css_selector("#publish").click()

        # 断言1: 验证新创建的文章是否出现在所有文章列表  
        self.dr.find_element_by_css_selector("li.wp-first-item.current > a").click()
        new_post_all = self.dr.find_element_by_css_selector(
            "tbody#the-list >tr:nth-of-type(1) strong>a").text
        self.assertTrue(new_post_all == title)
        time.sleep(10)

        # 断言2: 验证新创建的文章是否出现在首页
        self.dr.find_element_by_css_selector("#wp-admin-bar-site-name >a").click()
        new_post_home = self.dr.find_element_by_css_selector(".entry-title").text
        self.assertTrue(new_post_home == title)


if __name__ == '__main__':
    unittest.main()
