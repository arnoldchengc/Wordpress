from page_obj.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PostPage(BasePage):

    def all_post_icon(self):
        return self.dr.find_element_by_css_selector("#menu-posts > a > div.wp-menu-name")

    def first_post(self):
        return WebDriverWait(self.dr, 5).until(
            EC.visibility_of(self.dr.find_element_by_css_selector("tbody#the-list >tr:nth-of-type(1)>td>strong>a")))

    def click_all_post(self):
        self.all_post_icon().click()
