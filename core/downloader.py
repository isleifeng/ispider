"""
下载器模块
根据请求对象(Request), 发起HTTP, HTTPS网络请求, 拿到HTTP, HTTPS响应 构建响应对象(Response)并返回
"""

import requests
from http.response import Response


class Downloader(object):
    """
    1. 利用requests, urllib2模块发请求, 这里使用requests模块
    2. 实现get_response方法, 接收request请求对象作为参数, 发起请求, 获取响应
    """

    def get_response(self, request):
        """发起请求获取响应的方法"""

        # 1. 根据请求对象, 发起请求, 获取响应
        # 判断请求方法:
        if request.method.upper() == 'GET':
            resp = requests.get(url=request.url, headers=request.headers, params=request.params)
        elif request.method.upper() == 'POST':
            resp = requests.post(url=request.url, headers=request.headers, params=request.params, data=request.data)

        else:
            # 如果方法不是get祸post, 抛出一个异常
            raise Exception('不支持的请求方法')

        # 2. 构建响应对象, 并返回
        return Response(resp.url, resp.status_code, resp.headers, resp.content)
