"""
发布文章的页面
"""
from base.mp_base.base_page import MpBasePage, BaseHandle


# 发布文章页面对象库层
class Page(MpBasePage):

    def __init__(self):
        super().__init__()

    pass


# 发布文章操作层
class Handle(BaseHandle):

    def __init__(self):
        self.publish_al_page = Page()


# 发布文章业务层
class Proxy:
    def __init__(self):
        self.pulish_al_handle = Handle()
