"""
后台管理系统登陆测试用例
"""
from page.mis_page.mis_login_page import MisLoginProxy
from utils import DriverUtils, is_element_exist


# 定义测试类
class TestMisLogin:

    # 1.打开浏览器，并且最大化，设置隐式等待，打开后台管理系统测试地址
    def setup_class(self):
        self.driver = DriverUtils.get_mis_drvier()
        self.mis_login_proxy = MisLoginProxy()

    # 5.关闭浏览器，释放资源
    def teardown_class(self):
        DriverUtils.quit_mis_driver()

    # 2.定义测试方法:执行手工测试用例的步骤，在行测试步骤时候输入的数据是手工测试用例中数据一列
    def test_mis_login(self):
        # 定义测试数据
        username = "testid"
        password = "testpwd123"
        # 调用登陆页面业务层登陆方法
        self.mis_login_proxy.test_mis_login(username, password)
        # 3.拿到测试步骤执行完成的后的一个结果，这个结果可以用来判断测试用例是否执行成功
        is_exist = is_element_exist(self.driver, "管理员")
        # 4.断言：拿实际结果和期望结果做对比
        assert is_exist
