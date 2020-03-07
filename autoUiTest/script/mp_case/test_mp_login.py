"""
mp登陆测试用例
"""
import pytest

from page.mp_page.login_page import LoginProxy
from utils import DriverUtils, is_element_exist

@pytest.mark.run(order=2)
class TestMpLogin:

    # pytest 类级别的初始化fixture
    def setup_class(self):
        # 定义浏览器驱动实例属性来存放自媒体的浏览器驱动对象
        self.driver = DriverUtils.get_mp_drvier()
        self.login_proxy = LoginProxy()

    # pytest 类级别的销毁fixture
    def teardown_class(self):
        DriverUtils.quit_mp_driver()
        #  不使用下面的形式来关闭浏览器的原因：是因为运行多条测试用例的时候，浏览器开关对下面的
        #  浏览器关闭调用没有任何关联，还是会关闭浏览器
        # self.driver.quit() 和 DriverUtils.get_mp_drvier().quit()

    # 测试方法
    def test_mp_login(self):
        # 定义测试数据
        mobile = "15811859004"
        code = "246810"
        # 调用登陆的方法
        self.login_proxy.test_mp_login(mobile, code)
        # 执行断言
        is_element = is_element_exist(self.driver, "传智播客")
        assert is_element
