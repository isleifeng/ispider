"""
调度器:
1. 缓存请求对象(Request), 并为下载器提供请求对象, 实现请求的调度
2. 对请求对象进行去重判断: 实现去重方法_filter_request,该方法对内提供
"""
# 利用six木块实现py2和py3兼容
from six.moves.queue import Queue


class Scheduler(object):
    """
    1. 利用队列FIFO储存请求
    2. 实现add_request方法添加请求, 接收请求对象作为参数
    3. 实现get_request方法对外提供从队列取出的请求对象
    """

    def __init__(self):
        self.queue = Queue()

    def add_request(self):
        """获取一个请求对象并返回"""
        request = self.queue.get()
        return request

    def _filter_request(self):
        """请求去重"""
        pass
