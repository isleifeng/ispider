"""爬虫组件封装"""

from ispider.items import Item  # 导入Item对象
from ispider.http.request import Request  # 导入Request对象


class Spider(object):
    """
    1. 构建请求信息(初始的), 也就是生成请求对象(Request)
    2. 解析响应对象, 返回数据对象(Item)活着新的请求对象(Request)
    """
    start_url = 'https://www.yeyu.me'  # 初始化请求地址

    def start_requests(self):
        """构建初始请求对象并返回"""
        return Request(self.start_url)

    def parse(self, response):
        """
        解析请求
        返回新的请求对象, 或数据对象
        :param response: 请求对象
        :return: 新的请求对象, 或数据对象
        """
        return Item(response.body)  # 返回item对象
