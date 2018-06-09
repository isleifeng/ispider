"""管道组件, 负责处理数据对象"""


class Pipeline(object):
    def process_item(self, item):
        """处理item对象"""
        print(item)
        return item
