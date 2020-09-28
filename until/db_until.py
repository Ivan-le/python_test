import pymysql

from warnings import filterwarnings

# 忽略告警信息

filterwarnings('ignore',category=pymysql.Warning)

class MysqlDb():

    def __init__(self):

        self.conn = pymysql.connect("10.172.0.172", "root", "m654321", 'Test_case')

        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):

        self.cur.close()

        self.conn.close()

    def query(self, sql, state="all"):
        """
        查询
        :param sql: 查询的sql
        :param state: all 是查询全部
        :return:
        """
        self.cur.execute(sql)
        if state == "all":
            data = self.cur.fetchall()
        else:
            data = self.cur.fetchone()
        return data

    def execute(self,sql):
        """
        更新,删除,新增
        :param sql:
        :return:
        """

        try:
            # 使用execute操作sql
            rows = self.cur.execute(sql)
            print(rows)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            print("数据库操作异常{0}".format(e))
            # 事务回滚
            self.conn.rollback()
        return rows

if __name__ == '__main__':
    mydb = MysqlDb()
    r = mydb.query("select * from `config` where app='测试1' AND dict_key='host'")
    print(r)
