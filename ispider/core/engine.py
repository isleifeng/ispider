"""
引擎
对外提供整个持续的入口
一次调用其他组件对外提供的接口, 实现整个框架的运作(驱动)
"""

from ispider.http import Request  # 导入Request对象

from .scheduler import Scheduler
from .downloader import Downloader
from .pipeline import Pipeline
from .spider import Spider


class Engine(object):
    """
    1. 利用init方法初始化其他组件对象, 在内部使用
    2. 实现start方法, 又外部调用, 启动引擎
    3. 实现_start_engine方法, 完成震哥框架的运行逻辑
    """

    def __init__(self):
        self.spider = Spider()  # 爬虫对象
        self.scheduler = Scheduler()  # 初始化调度器对象
        self.downloader = Downloader()  # 初始化下载器对象
        self.pipeline = Pipeline()  # 初始化管道对象

    def start(self):
        """启动整个引擎"""
        self._start_engine()

    def _start_engine(self):
        """一次调用其他组件提供的接口, 实现整个框架的驱动"""
        # 1. 爬虫模块发出初始化请求
        start_request = self.spider.start_requests()

        # 2. 把初始化请求添加给调度器
        self.scheduler.add_request(start_request)

        # 3. 从调度器获取请求对象, 交给下载器发起请求, 获取一个响应对象
        request = self.scheduler.get_request()

        # 4. 利用下载器发起请求
        response = self.downloader.get_response(request)

        # 5. 利用爬虫的解析响应的方法, 处理响应, 得到结果
        result = self.spider.parse(response)

        # 6. 判断结果对象
        # 6.1 如果是请求对象, 那么就再交给调度器
        if isinstance(result, Request):
            self.scheduler.add_request(result)
        else:  # 6.2 否则, 就交给管道处理
            self.pipeline.process_item(result)
