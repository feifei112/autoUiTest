"""
发布文章的测试类
"""
import time

import pytest

from page.mp_page.index_page import IndexProxy
from page.mp_page.publish_aritcle_page import PublishAlProxy
from utils import DriverUtils, is_element_exist


@pytest.mark.run(order=3)
class TestPublishAritcle:

    def setup_class(self):
        # 1.打开浏览器并且打开对应的测试网址
        self.driver = DriverUtils.get_mp_drvier()
        # 实例化对象是为：提供测试步骤方法的调用
        self.pl_proxy = PublishAlProxy()
        self.index_proxy = IndexProxy()

    def teardown_class(self):
        # 5.关闭浏览器释放资源
        DriverUtils.quit_mp_driver()

    # 如果单个测试类中存在多个测试方法得话就需要使用方法界别得fixture，每个方法都会执行回到首页得动作
    # 例如：对于发布文章验证多种发布不成功情况：少标题，无文章详情等多个测试方法
    # def setup(self):
    #     self.driver.get("http://ttmp.research.itcast.cn/")

    def test_pb_aritcle(self):
        # 2.测试数据
        title = "web自动化技术-{}".format(time.strftime("%Y%m%d%H%M%S"))
        content = "web自动化技术-{}".format(time.strftime("%Y%m%d%H%M%S"))
        channel_option = "数据库"
        select_name = "请选择"
        # 3.执行测试步骤
        # 进入发布文章的页面
        self.index_proxy.to_publish_aritcle_page()
        # 发布文章
        self.pl_proxy.test_publish_aritcle(title=title, aritcle_content=content, option=channel_option,
                                           select_text=select_name)
        # 4.拿到测试实际结果并进行断言,如找到对应的元素则返回元素对象，其是一个字符串，断言时非空字符串都为真则通过
        # 如未找到元素则返回的是False,断言则会失败
        is_exist = is_element_exist(self.driver, "新增文章成功")
        assert is_exist
