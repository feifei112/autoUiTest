"""
mp:自媒体登陆页面
"""
from selenium.webdriver.common.by import By
from base.mp_base.base_page import MpBasePage, BaseHandle


# 对象库层
class LoginPage(MpBasePage):

    def __init__(self):
        # 重写父类
        super().__init__()
        # 电话号码
        self.mobile = (By.CSS_SELECTOR, "[placeholder*='手机号']")
        # 验证码
        self.code = (By.CSS_SELECTOR, "[placeholder*='验证码']")
        # 登陆按钮
        self.login_btn = (By.CSS_SELECTOR, ".el-button--primary")

    def find_mobile(self):
        """
        :return:返回电话号码输入框元素对象
        """
        return self.find_elt(self.mobile)

    def find_code(self):
        return self.find_elt(self.code)

    def find_login_btn(self):
        return self.find_elt(self.login_btn)


# 操作层
class LoginHandle(BaseHandle):

    def __init__(self):
        self.login_page = LoginPage()

    # 输入手机号码
    def input_mobile(self, mobile):
        """
        :param mobile:手机号码
        :return:
        """
        self.input_text(self.login_page.find_mobile(), mobile)

    # 输入验证码
    def input_code(self, code):
        """
        :param code:验证码
        :return:
        """
        self.input_text(self.login_page.find_code(), code)

    # 点击登陆按钮
    def click_login_btn(self):
        self.login_page.find_login_btn().click()


# 业务层
class LoginProxy:
    """
    组织多个操作方法形成一个完整操作步骤:业务
    """
    def __init__(self):
        self.login_handle = LoginHandle()

    def test_mp_login(self, mobile, code):
        # 输入手机号码
        self.login_handle.input_mobile(mobile)
        # 输入验证码
        self.login_handle.input_code(code)
        # 点击登陆按钮
        self.login_handle.click_login_btn()
