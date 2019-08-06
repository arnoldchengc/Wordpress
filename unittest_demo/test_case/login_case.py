import sys
from os.path import abspath, dirname

file_path = dirname(dirname(abspath(__file__)))
sys.path.insert(0, file_path)

from page_obj.login_page import LoginPage
from page_obj.dashboard_page import DashboardPage
from common.app_setup import AppSetUp

class LoginCase(AppSetUp):

    def test_login_success(self):
        username = '1940770824@qq.com'
        password = 'Summer@2019'
        login_page = LoginPage(self.dr)
        dashboard_page = login_page.login_success(username, password)
        self.assertTrue("mini2019" in dashboard_page.greeting_link().text)
