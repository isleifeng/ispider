"""封装请求对象"""


class Request(object):

    def __init__(self, url, method='GET', headers=None, params=None, data=None):
        self.url = url  # 请求地址
        self.method = method  # 请求方法
        self.headers = headers  # 请求头
        self.params = params  # 请求参数
        self.data = data  # 请求体
