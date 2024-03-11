import yaml
import atexit
from pymysql import connect

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class SqlHelper(Singleton):
    def __init__(self, config_file='config.yaml'):
        if not hasattr(self, '_init_flag'):
            with open(config_file, 'r') as f:
                config = yaml.safe_load(f)
                db_config = config['database']
                self.__host = db_config['host']
                self.__port = db_config['port']
                self.__db = db_config['db']
                self.__user = db_config['user']
                self.__passwd = db_config['passwd']
                self.__charset = db_config['charset']
            self._init_flag = True
            self.__connect()
            atexit.register(self.__close)

    def __connect(self):
        self.__conn = connect(host=self.__host, port=self.__port, db=self.__db, user=self.__user, passwd=self.__passwd,
                              charset=self.__charset)
        self.__cursor = self.__conn.cursor()

    def __close(self):
        self.__cursor.close()
        self.__conn.close()

    def get_one(self, sql, params=None):
        result = None
        try:
            if params:
                self.__cursor.execute(sql, params)
            else:
                self.__cursor.execute(sql)
            result = self.__cursor.fetchone()
        except Exception as e:
            print(e)
        return result

    def get_all(self, sql, params=None):
        lst = ()
        try:
            if params:
                self.__cursor.execute(sql, params)
            else:
                self.__cursor.execute(sql)
            lst = self.__cursor.fetchall()
        except Exception as e:
            print(e)
        return lst

    def insert(self, sql, params=None):
        return self.__edit(sql, params)

    def update(self, sql, params=None):
        return self.__edit(sql, params)

    def delete(self, sql, params=None):
        return self.__edit(sql, params)

    def __edit(self, sql, params=None):
        count = 0
        try:
            if params:
                count = self.__cursor.execute(sql, params)
            else:
                count = self.__cursor.execute(sql)
            self.__conn.commit()
        except Exception as e:
            print(e)
        return count
