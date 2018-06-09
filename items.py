"""对数据进行简单封装, 实现item对象"""


class Item(object):
    def __init__(self, data):
        # data 表示传入的数据
        self._data = data  # 设置为私有属性

    @property
    def data(self):
        """对外提供data进行访问"""
        return self._data
