

"""
请求工具封装
"""
import requests


class RequsesUntil:

    def __init__(self):
        pass

    def request(self, method, url, headers=None, param=None, content_type=None):
        """
        封装
        :return:
        """
        try:
            if method == "get":
                result = requests.get(url=url, param=param, headers=headers).json()
                return result
            elif method == "post":
                if content_type == "application/json":
                    result = requests.post(url=url, headers=headers, json=param).json()
                    return result
                else:
                    result = requests.post(url=url, headers=headers, json=param).json()
                    return result
            else:
                print("no such method！")

        except Exception as e:
            print("HTTP请求报错:{0}".format(e))


if __name__ == '__main__':
    RequsesUntil()


