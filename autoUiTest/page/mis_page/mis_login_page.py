"""
后台管理系统的登陆页面
"""
from selenium.webdriver.common.by import By

from base.mis_base.base_page import MisBasePage, BaseHandle
from utils import DriverUtils

# MIS登陆页面对象库层
class MLoginPage(MisBasePage):

    def __init__(self):
        super().__init__()
        # 用户名
        self.username = (By.NAME, "username")
        # 密码
        self.password = (By.NAME, "password")
        # 登陆按钮
        self.submit_btn = (By.ID, "inp1")

    def find_username(self):
        return self.find_elt(self.username)

    def find_password(self):
        return self.find_elt(self.password)

    def find_submit_btn(self):
        return self.find_elt(self.submit_btn)


# Mis登陆页面操作层
class MLoginHandle(BaseHandle):

    def __init__(self):
        self.m_login_page = MLoginPage()

    # 输入用户名
    def input_username(self,username):
        self.input_text(self.m_login_page.find_username(),username)

    # 输入密码
    def input_password(self,pwd):
        self.input_text(self.m_login_page.find_password(),pwd)

    # 点击登陆按钮
    def click_submit_btn(self):
        # 定义js脚本字符串
        js_str = 'document.getElementById("inp1").removeAttribute("disabled")'
        # 执行js脚本
        DriverUtils.get_mis_drvier().execute_script(js_str)
        # 点击登陆按钮
        self.m_login_page.find_submit_btn().click()


# Mis登陆业务层
class MisLoginProxy:
    def __init__(self):
        self.m_login_handle = MLoginHandle()

    # 登陆方法
    def test_mis_login(self,username,pwd):
        # 输入用户名
        self.m_login_handle.input_username(username)
        # 输入密码
        self.m_login_handle.input_password(pwd)
        # 点击登陆
        self.m_login_handle.click_submit_btn()
