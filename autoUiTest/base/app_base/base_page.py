from utils import DriverUtils


# 对象库层的基类
class AppBasePage:

    # 初始化方法
    def __init__(self):
        # 由于分为三个系统，在初始化获取浏览器驱动对象的时候注意不要调用错其它系统的浏览器驱动对象
        self.driver = DriverUtils.get_app_drvier()

    # 自媒体公用元素定位方法
    def find_elt(self, loction):
        """
        :param loction: 参数类型为元组，元组包含两个数据，一个是元素的定位方式，一个是元素定位方式所对应的值
        :return: 元素对象
        """
        return self.driver.find_element(*loction)


# 操作层的基类，这个类名三个是一样的，命名不会有问题，但是注意后续在继承导包的时候，不要导错包
class BaseHandle:

    # 公用模拟输入的方法
    def input_text(self, element, text):
        """
        :param element: 传递的是元素对象
        :param text: 输入的文本信息
        :return:
        """
        element.clear()
        element.send_keys(text)
