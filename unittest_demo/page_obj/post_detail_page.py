from page_obj.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PostDetailPage(BasePage):

    def post_title_textbox(self):
        return WebDriverWait(self.dr, 5).until(
            EC.visibility_of(self.dr.find_element_by_css_selector("#title")))

    def post_content_textarea(self):
        self.dr.switch_to.frame("content_ifr")
        return self.dr.find_element_by_css_selector("body#tinymce")

    def publish_btn(self):
        return self.dr.find_element_by_css_selector("#publish")

    def update_post_title(self, title):
        self.post_title_textbox().send_keys(title)

    def update_post_content(self, content):
        self.post_content_textarea().send_keys(content)

    def publish_post(self):
        self.dr.switch_to.default_content()
        self.publish_btn().click()
