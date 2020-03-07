from utils import DriverUtils


# 对象库层的基类
class MisBasePage:

    # 初始化方法
    def __init__(self):
        self.driver = DriverUtils.get_mis_drvier()

    # 自媒体公用元素定位方法
    def find_elt(self, loction):
        return self.driver.find_element(*loction)


# 操作层的基类
class BaseHandle:

    # 公用模拟输入的方法
    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)
