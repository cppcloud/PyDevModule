from SqlHelper import *

if __name__ == '__main__':
    # 创建 MysqlHelper 对象，传入连接参数
    mysql_helper = SqlHelper()

    # sql = "insert into t_student values (%s,%s,%s)"
    # params = (11, "王五", "123456")
    # result = mysql_helper.get_one(sql, params)
    # print(result)



    # # 测试查询单条数据
    sql = 'SELECT * FROM t_student WHERE id = %s'
    params = (1)
    result = mysql_helper.get_one(sql, params)
    print(result)
    #
    # # 测试查询多条数据
    # sql = 'SELECT * FROM user WHERE age > %s'
    # params = (20,)
    # result = mysql_helper.get_all(sql, params)
    # print(result)
    #
    # # 测试插入数据
    # sql = 'INSERT INTO user(name, age) VALUES(%s, %s)'
    # params = ('Tom', 25)
    # count = mysql_helper.insert(sql, params)
    # print(count)
    #
    # # 测试修改数据
    # sql = 'UPDATE user SET age = %s WHERE id = %s'
    # params = (30, 1)
    # count = mysql_helper.update(sql, params)
    # print(count)
    #
    # # 测试删除数据
    # sql = 'DELETE FROM user WHERE id = %s'
    # params = (2,)
    # count = mysql_helper.delete(sql, params)
    # print(count)
    #
    # # 再次创建 MysqlHelper 对象，验证单例模式
    # mysql_helper2 = MysqlHelper(MysqlHelper.conn_params2)
    # print(mysql_helper is mysql_helper2)  # 输出 True
    #
    # # 关闭数据库连接
    # mysql_helper.__close()
