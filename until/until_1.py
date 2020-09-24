import  pymysql

conn = pymysql.connect("10.172.0.181", "root", "123456", 'sys')

# 使用 cursor 方法获取操作游标,得到一个可以执行sql语句,并且操作结果作为字典返回的游标
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

try:
    # 使用execute 方法连接查询
    cursor.execute("select * from `sys_config`")

    data = cursor.fetchall()

    print(data)
except Exception as e:
    print(e)

finally:
    # 关闭数据库
    conn.close()