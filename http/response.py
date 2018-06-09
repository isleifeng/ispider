"""对HTTP基本的响应属性进行简单封装, 实现一个Response对象"""


class Response(object):
    """Response对象"""

    def __init__(self, url, status_code, headers, body):
        self.url = url  # 响应url
        self.status_code = status_code  # 响应状态码
        self.headers = headers  # 响应头
        self.body = body
