from page_obj.base_page import BasePage
from page_obj.post_detail_page import PostDetailPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class DashboardPage(BasePage):

    def greeting_link(self):
        return WebDriverWait(self.dr, 5).until(
            EC.visibility_of(self.dr.find_element_by_css_selector("#wp-admin-bar-my-account")))

    def click_create_new_post(self):
        create_icon = self.dr.find_element_by_css_selector("#wp-admin-bar-new-content")
        ActionChains(self.dr).move_to_element(create_icon).perform()
        create_post_icon = WebDriverWait(self.dr, 10).until(
            EC.visibility_of(self.dr.find_element_by_css_selector("#wp-admin-bar-new-post")))
        create_post_icon.click()
        return PostDetailPage(self.dr)
