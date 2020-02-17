import pymysql

class DB:
    def __init__(self):
        self.conn=pymysql.connect(host='192.168.117.128',port=3306,user='root',passwd='',db='TESTDB') # passwd 不是 password
        self.cur=self.conn.cursor()

    def __del__(self):# 析构函数，实例删除时触发
        self.cur.close()
        self.conn.close()

    def query(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def exec(self,sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(str(e))

    def check_user(self,name):
        result=self.query("select * from EMPLOYEE where FIRST_NAME='{}'".format(name))
        return True if result else False

    def del_user(self,name):
        self.exec("delete from EMPLOYEE where FIRST_NAME='{}'".format(name))

if __name__ == '__main__':
    db=DB()
    if db.check_user("Lizy"):
        db.del_user("Lizy")





