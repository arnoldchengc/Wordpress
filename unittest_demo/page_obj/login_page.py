from page_obj.base_page import BasePage
from page_obj.dashboard_page import DashboardPage


class LoginPage(BasePage):

    def username_textbox_filed(self):
        return self.dr.find_element_by_css_selector("#user_login")

    def password_textbox_filed(self):
        return self.dr.find_element_by_css_selector("#user_pass")

    def login_btn(self):
        return self.dr.find_element_by_css_selector("#wp-submit")

    def login_success(self, username, password):
        self.username_textbox_filed().send_keys(username)
        self.password_textbox_filed().send_keys(password)
        self.login_btn().click()
        return DashboardPage(self.dr)
