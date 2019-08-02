import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class wp_delete_post(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.get("http://139.196.205.242:8000/wp-login.php")
        self.dr.maximize_window()

    def login(self, username, password):
        self.dr.find_element_by_css_selector("#user_login").send_keys(username)
        self.dr.find_element_by_css_selector("#user_pass").send_keys(password)
        self.dr.find_element_by_css_selector("#wp-submit").click()

    def test_delete_post(self):
        self.login(username='1940770824@qq.com', password='Summer@2019')
        self.dr.find_element_by_css_selector("li#menu-posts").click()

        ele_first_post = WebDriverWait(self.dr, 10).until(
            EC.visibility_of(self.dr.find_element_by_css_selector("tbody#the-list >tr:nth-of-type(1) strong >a")))

        ActionChains(self.dr).move_to_element(ele_first_post).perform()

        ele_delete = WebDriverWait(self.dr, 10).until(EC.visibility_of(
            self.dr.find_element_by_css_selector("tbody#the-list >tr:nth-of-type(1) div.row-actions span.trash >a")))

        ele_delete.click()

        ele_message = WebDriverWait(self.dr, 10).until(
            EC.visibility_of(self.dr.find_element_by_css_selector("#message")))

        self.assertTrue("已移动1篇文章到回收站。 " in ele_message.text)


if __name__ == "__main__":
    unittest.main()
