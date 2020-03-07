"""
自媒体首页
"""
from selenium.webdriver.common.by import By
from base.mp_base.base_page import MpBasePage

class IndexPage(MpBasePage):

    def __init__(self):
        super().__init__()
        # 内容管理
        self.content_manager = (By.XPATH, "//*[text()='内容管理']")
        # 文章管理
        self.article_manager = (By.XPATH, "//*[contains(text(),'发布文章')]")

    def find_content_manager(self):
        return self.find_elt(self.content_manager)

    def find_article_manager(self):
        return self.find_elt(self.article_manager)


class IndexHandle:

    def __init__(self):
        self.index_page = IndexPage()

    # 点击内容管理
    def click_content_manager(self):
        self.index_page.find_content_manager().click()

    # 点击文章管理
    def click_article_manager(self):
        self.index_page.find_article_manager().click()


class IndexProxy:

    def __init__(self):
        self.index_handle = IndexHandle()

    # 去文章发布页面
    def to_publish_aritcle_page(self):
        # 点击内容管理
        self.index_handle.click_content_manager()
        # 点击文章管理
        self.index_handle.click_article_manager()
