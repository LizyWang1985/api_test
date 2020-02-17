import  pymysql
#本文件为学习笔记文件，另一文件db.py把所有数据库操作封装成公用的数据库模块，方便重复操作使用
'''数据库连接==================================='''

# 打开数据库连接
IP='192.168.117.128'
db=pymysql.connect(IP,"root","","TESTDB")

#使用cursor()方法创建一个游标对象 cursor
cursor=db.cursor()

#使用execute（）方法执行SQL查询
cursor.execute("SELECT VERSION()")

#使用fetchone()方法获取单条数据
data=cursor.fetchone()

print("Database version:%s" %data)

#关闭数据库连接
db.close()

'''创建数据库表================================='''
#打开数据库连接
IP='192.168.117.128'
db=pymysql.connect(IP,"root","","TESTDB")

#使用cursor()方法创建一个游标对象 cursor
cursor=db.cursor()

#使用execute（）方法执行SQL查询
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#使用预处理语句创建表
sql="""CREATE TABLE EMPLOYEE(
        FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1),
        INCOME FLOAT,
        PRIMARY KEY (FIRST_NAME))"""

cursor.execute(sql)

#关闭数据库连接
db.close()

'''数据库插入操作===================================================
cursor.execute(sql, args) 执行单条 SQL
executemany(sql, args) 批量执行 SQL
# 批量插入
effect_row = cursor.executemany(
    'INSERT INTO `users` (`name`, `age`) VALUES (%s, %s) ON DUPLICATE KEY UPDATE age=VALUES(age)', [
        ('hello', 13),
        ('fake', 28),
    ])
    
'''
#打开数据库连接
IP='192.168.117.128'
db=pymysql.connect(IP,"root","","TESTDB")

#使用cursor()方法创建一个游标对象 cursor
cursor=db.cursor()

#SQL插入语句,sql和sql1两种写法
sql="""INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)
        VALUES ('Mac','Mohan',20,'M',2000)"""


sql1 = "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)VALUES ('%s', '%s',  %s,'%s',%s)" %('Mac', 'Mohan', 30, 'M', 2000)

try:
    #执行语句
    cursor.execute(sql1)
    #提交到数据库执行
    db.commit()
except:
    #如果发生错误则回滚
    db.rollback()

#关闭数据库连接
db.close()

'''#以下代码使用变量向SQL语句中传递参数:
user_id = "test123"
password = "password"

con.execute('insert into Login values( %s,  %s)' % \
             (user_id, password))
'''

'''数据库查询操===================================================================
Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。

fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
fetchall(): 接收全部的返回结果行.
rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数
cursor.fetchmany(3) # 获取前N条数据

游标控制
所有的数据查询操作均基于游标，我们可以通过cursor.scroll(num, mode)控制游标的位置。

cursor.scroll(1, mode='relative') # 相对当前位置移动
cursor.scroll(2, mode='absolute') # 相对绝对位置移动'''


#实例：查询EMPLOYEE表中salary（工资）字段大于1000的所有数据：

#打开数据库连接
IP='192.168.117.128'
db=pymysql.connect(IP,"root","","TESTDB")

#使用cursor()方法创建一个游标对象 cursor
cursor=db.cursor()

#SQL查询语句
sql="SELECT * FROM EMPLOYEE WHERE INCOME > %s" %(1000)

try:
    #执行SQL语句
    cursor.execute(sql)
    #获取所有的记录列表
    results=cursor.fetchall()
    for row in results:
        fname=row[0]
        lname=row[1]
        age=row[2]
        sex=row[3]
        income=row[4]
        #打印结果
        print ("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
             (fname, lname, age, sex, income ))
except:
    print("Error:unable to fetch data")

db.close()

'''数据库更新操作========================================================'''
#打开数据库连接
IP='192.168.117.128'
db=pymysql.connect(IP,"root","","TESTDB")

#使用cursor()方法创建一个游标对象 cursor
cursor=db.cursor()

#SQL更新语句
sql="UPDATE EMPLOYEE SET AGE=AGE+1 WHERE SEX='%c'"%('M')
try:
    #执行语句
    cursor.execute(sql)
    #提交到数据库执行
    db.commit()
except:
    #如果发生错误则回滚
    db.rollback()

#关闭数据库连接
db.close()

'''删除操作============================================'''
#打开数据库连接
IP='192.168.117.128'
db=pymysql.connect(IP,"root","","TESTDB")

#使用cursor()方法创建一个游标对象 cursor
cursor=db.cursor()

#SQL删除语句
sql="DELETE FROM EMPLOYEE WHERE AGE>%s"% (20)
try:
    #执行语句
    cursor.execute(sql)
    #提交到数据库执行
    db.commit()
except:
    #如果发生错误则回滚
    db.rollback()

#关闭数据库连接
db.close()

'''后言
数据库连接信息建议写到配置文件中，从配置文件中读取
sql语句建议先在手工测试一下没有语法问题再进行封装
通过封装各种sql可以完成各种业务操作
更改数据库有风险，操作需谨慎！！！
'''