import sys
import MySQLdb
reload(sys)
sys.setdefaultencoding("utf-8")

# mysql - offline
SQL_CFG_170 = {"host": "192.168.14.170",
    "user": "spider",
    "passwd": "spider2013",
    "port": 3306,
    "database_price": "price",
    "database_report": "report",
} 

# mysql - online
SQL_CFG = {"host": "w.ihotelreport.p.mysql.elong.com",
    "user": "ihotel_report_w",
    "passwd": "Gh4Ul6Xd0Fn3",
    "port": 6227,
    "database_price": "ihotel_price",
    "database_report": "ihotel_report"
} 


class CDataBase:
    def __init__(self, host, user, passwd, db, port = 3306):
        self.__host = host
        self.__user = user
        self.__passwd = passwd
        self.__port = int(port) 
        self.__db = db
        self.__conn = MySQLdb.connect(host = self.__host,
                                      user = self.__user,
                                      passwd = self.__passwd,
                                      db = self.__db,
                                      port = self.__port)
        self.__cur = self.__conn.cursor()

    def __del__(self):
        self.__cur.close()  
        self.__conn.close() 

    def ExecSql(self, sql) :
        erows = self.__cur.execute(sql)
        if erows >= 0:
          self.__conn.commit()
        else :
          erows = -1
          self.__conn.rollback()
        return erows 

    def ExecManySql(self, sql, param):
        if self.__cur.executemany(sql, param) >= 1:
          self.__conn.commit() 
        else:
          self.__conn.rollback()

    def GetAllList(self, sql):
        self.__cur.execute(sql)
        return self.__cur.fetchall()


if __name__ == "__main__":
    mql_db = CDataBase(SQL_CFG["host"],SQL_CFG["user"],SQL_CFG["passwd"],SQL_CFG["database_report"], SQL_CFG["port"])
    sql = "SELECT * FROM ihotel_report.ps_listcache_daily LIMIT 100;"
    result = mql_db.GetAllList(sql)
    print result, type(result)
