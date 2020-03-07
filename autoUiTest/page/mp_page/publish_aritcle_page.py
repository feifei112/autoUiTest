"""
发布文章的页面
"""
import os
import time

from selenium.webdriver.common.by import By
from base.mp_base.base_page import MpBasePage, BaseHandle

# 发布文章页面对象库层
from utils import DriverUtils, select_option


class PublishAlPage(MpBasePage):

    def __init__(self):
        super().__init__()
        # 文章标题
        self.aritcle_title = (By.CSS_SELECTOR, "[placeholder='文章名称']")
        # 文章富文本iframe
        self.aritcle_iframe = (By.ID, "publishTinymce_ifr")
        # 文章内容
        self.aritcle_content = (By.ID, "tinymce")
        # 文章封面
        self.aritcle_cover = (By.XPATH, "//*[text()='自动']")
        # 文章频道
        self.aritcle_channel = (By.CSS_SELECTOR, "[placeholder='请选择']")
        # 文章频道的选项
        self.aritcle_channel_option = (By.XPATH, "//*[text()='区块链']")
        # 发表按钮
        self.publish_btn = (By.XPATH, "//*[text()='发表']")

    def find_aritcle_title(self):  # 找文章标题
        return self.find_elt(self.aritcle_title)

    def find_aritcle_iframe(self):  # 找到iframe
        return self.find_elt(self.aritcle_iframe)

    def find_aritcle_content(self):  # 找到文章内容的输入框元素对象
        return self.find_elt(self.aritcle_content)
        # return self.find_elt(self.aritcle_title)

    def find_aritcle_cover(self):  # 找封面元素
        return self.find_elt(self.aritcle_cover)

    def find_aritcle_channel(self):  # 找频道元素
        return self.find_elt(self.aritcle_channel)

    def find_aritcle_channel_option(self):  # 找具体某个频道
        return self.find_elt(self.find_aritcle_channel_option())

    def find_publish_btn(self):  # 找到发布按钮
        return self.find_elt(self.publish_btn)


# 发布文章操作层
class PublishAlHandle(BaseHandle):

    def __init__(self):
        self.publish_al_page = PublishAlPage()
        self.driver = DriverUtils.get_mp_drvier()

    # 输入文章标题
    def input_article_title(self, title):
        self.input_text(self.publish_al_page.find_aritcle_title(), title)

    # 输入文章信息
    def input_article_content(self, aritcle_content):
        # 切换iframe
        self.driver.switch_to.frame(self.publish_al_page.find_aritcle_iframe())
        time.sleep(2)
        # 输入文章信息
        self.input_text(self.publish_al_page.find_aritcle_content(), aritcle_content)
        # 返回默认页面
        self.driver.switch_to.default_content()
        time.sleep(2)

    # 选择封面
    def check_cover(self):
        self.publish_al_page.find_aritcle_cover().click()

    # 选择频道
    def check_channel_option(self, channel_option, select_text):
        """
        :param channel_option:选项的文本信息
        :param select_text:下来框的placehodler的属性值
        :return:
        """
        select_option(driver=self.driver,
                      select_text=select_text, channel_option=channel_option)

    # 提交文章
    def click_publish_btn(self):
        self.publish_al_page.find_publish_btn().click()


# 发布文章业务层
class PublishAlProxy:
    def __init__(self):
        self.pulish_al_handle = PublishAlHandle()

    # 发布文章的业务方法
    def test_publish_aritcle(self,title,aritcle_content,option,select_text):
        """
        :param title:发布文章的标题
        :param aritcle_content: 发布文章的类容
        :param option: 频道的具体某个选项
        :param select_text: 选择框的元素对象的文本信息
        :return:
        """
        # 输入文章标题
        self.pulish_al_handle.input_article_title(title)
        # 输入文章的类容
        self.pulish_al_handle.input_article_content(aritcle_content)
        # 选择封面
        self.pulish_al_handle.check_cover()
        # 选择频道
        self.pulish_al_handle.check_channel_option(channel_option=option,select_text=select_text)
        # 提交文章
        self.pulish_al_handle.click_publish_btn()