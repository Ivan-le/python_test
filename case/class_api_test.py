import datetime

from until.db_until import MysqlDb


class XdclassTestCase():



    def loadAllCaseByAPP(self,app):

        """
        加载全部测试用例
        :param app:
        :return:
        """
        my_db = MysqlDb()
        sql = "select * from `case` where app='{0}'".format(app)

        result = my_db.query(sql)
        return result






    def findCaseById(self,case_id):
        """
        根据id找测试用例
        :param case_id:
        :return:
        """
        my_db = MysqlDb()
        sql = "select * from `case` where id='{0}'".format(case_id)

        result = my_db.query(sql,state="one")
        return result





    def loadConfigByAppAndKey(self,app,key):
        """
        根据app和key加载配置
        :param app:
        :param key:
        :return:
        """
        my_db = MysqlDb()
        sql = "select * from `config` where app='{0} AND key={0}'".format(app, key)

        result = my_db.query(sql,state="one")
        return result



    def updateResultByCaseId(self,response,is_pass,msg,case_id):
        """
        根据测试用例id,更新响应内容和测试内容
        :param response:
        :param is_pass:
        :param msg:
        :param case_id:
        :return:
        """
        my_db = MysqlDb()
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if is_pass:
            sql = "update `case` set response='{0}', pass='{1}',msg='{2},update_time='{3}' where id='{4}'".format("",is_pass,msg,now_time,case_id)
        else:
            sql = "update `case` set response=\"{0}\", pass='{1}',msg='{2},update_time='{3}' where id='{4}'".format(str(response),is_pass,msg,now_time,case_id)

        rows = my_db.execute(sql)
        print(sql)

        return  rows



    def runAllCase(self,app):
        """
        执行全部用例入口
        :param app:
        :return:
        """

        #获取接口域名
        api_host_obj = self.loadConfigByAppAndKey(app,"host")

        #获取全部用例
        result = self.loadAllCaseByAPP(app)

        #遍历用例
        for case in result:
            print(case)
            if case['run'] == "yes":
                try:
                    #执行用例
                    response = self.runCase(case,api_host_obj)

                    # 断言判断
                    assert_msg = self.assertResponse(case,response)

                    #更新数据库
                    rows = self.updateResultByCaseId(response,assert_msg['is_pass'],assert_msg['msg'],case['id'])
                    print("更新结果 rows={0}".format(str(rows)))
                except Exception as e:
                    print("用例id={0}，标题：{1}，执行报错：{2}".format(case['id'], case['tltle'], e))

            # 发送测试报告
            self.sendTestReport(app)

    def runCase(self,case,api_host_obj):
        """
        执行单个测试用例
        :param case:
        :param api_host_obj:
        :return:
        """
        print("test")
        pass






    def assertResponse(self,case,response):
        """
        断言响应内容,更新用例执行情况
        :param case:
        :param response:
        :return:
        """
        assert_type = case['assert_type']
        expect_result = case['expect_result']
        is_pass = False

        # 判断业务状态码
        if  assert_type == 'code':
            if expect_result == response['code']:
                is_pass = True
                print('测试用例通过')
            else:
                print('测试不通过')

        # 判断list的长度大小和类型
        elif assert_type == "page":
            response_list = response[assert_type]['list']
            if int(expect_result) == len(response_list) and  isinstance(response_list,list):
                is_pass = True
                print('测试用例通过')
            else:
                print('测试不通过')
        elif assert_type == 'data':
             data = response["data"]
             data_num = case['data_num']
            





        # else:








    def sendTestReport(self,app):
        """
        发送测试报告
        :param app:
        :return:
        """
        pass





if __name__ == '__main__':
    sql = XdclassTestCase()
    num = sql.findCaseById(1)
    print(num)