from SqlHelper import *

if __name__ == '__main__':
    mysql_helper = SqlHelper()

    # Test insertion of data
    sql = 'INSERT INTO user(name, age) VALUES(%s, %s)'
    params = ('Tom', 25)
    count = mysql_helper.insert(sql, params)
    print(count)


    # Test insertion of data
    sql = 'INSERT INTO user(name, age) VALUES(%s, %s)'
    params = ('T', 29)
    count = mysql_helper.insert(sql, params)
    print(count)


    # Test insertion of data
    sql = 'INSERT INTO user(name, age) VALUES(%s, %s)'
    params = ('m', 10)
    count = mysql_helper.insert(sql, params)
    print(count)



    sql = 'SELECT * FROM user WHERE id = %s'
    params = (1,)
    result = mysql_helper.get_one(sql, params)
    print(result)

    # Test querying multiple pieces of data
    sql = 'SELECT * FROM user WHERE age > %s'
    params = (20,)
    result = mysql_helper.get_all(sql, params)
    print(result)



    # Test modified data
    sql = 'UPDATE user SET age = %s WHERE id = %s'
    params = (30, 1)
    count = mysql_helper.update(sql, params)
    print(count)

    # Test deletion of data
    sql = 'DELETE FROM user WHERE id = %s'
    params = (2,)
    count = mysql_helper.delete(sql, params)
    print(count)

    # Create the MysqlHelper object again, verifying the singleton pattern
    mysql_helper2 = SqlHelper()
    print(mysql_helper is mysql_helper2)  # output True