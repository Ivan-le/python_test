import unittest

from until.Request_Until import RequsesUntil

host= "http://tst.gdmcmc.cn"
request = RequsesUntil()
headers = {"token": "2cddb83c309d21476cc1750b53cdcc9b", "JSESSIONID": "1598ACC71CDD988B3722E949F762FE4E"}
content_type="application/json"

class PageTestCase(unittest.TestCase):


    def testObtainPageCase(self):
        """
        页面请求
        :return:
        """
        # request = RequsesUntil()
        data = {"pageNum": 1,"pageSize":"","username": ""}
        # headers = {"token": "99cacfe165e457bf36183fb1be736370", "JSESSIONID": "4828DF92B9C7AF56018FAB817A99556C"}
        url = host + "/iovs/auth/sys/user/page"

        response = request.request("post", url, headers, data, content_type)
        # print(len(response["page"]["list"]))
        # print(response["page"])
        self.assertEqual(response['code'], 0, "请求错误")
        # self.assertTrue(response['page'] > 0, "12323")

    def testTrafficCase(self):
        """
        违章查询
        :return:
        """
        data = ["1"]
        url = host + "/iovs/violation/getViolationInfoList"

        response = request.request("post", url, headers, data, content_type)
        # print(response)
        self.assertEqual(response['code'], 0, "error")


if __name__ == '__main__':
    unittest.main(verbosity=2)

