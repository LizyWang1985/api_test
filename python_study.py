import os


print("hello world")
print("你好，世界")

'''多行语句
Python语句中一般以新行作为语句的结束符。
但是我们可以使用斜杠（ \）将一行的语句分为多行显示，如下所示：
total = item_one+\
        item_two+\
        item_three
'''

'''
字符串
如果你要实现从字符串中获取一段子字符串的话，可以使用 [头下标:尾下标] 来截取相应的字符串，其中下标是从 0 开始算起，可以是正数或负数，下标可以为空表示取到头或尾。
[头下标:尾下标] 获取的子字符串包含头下标的字符，但不包含尾下标的字符。
加号（+）是字符串连接运算符，星号（*）是重复操作。
'''


str="Hello world!"
print(str)           # 输出完整字符串
print(str[0])       # 输出字符串中的第一个字符
print(str[1:5])    # 输出字符串中第三个至第六个之间的字符串llo
print(str[2:])       # 输出从第三个字符开始的字符串llo World!
print(str * 2)       # 输出字符串两次 Hello World!Hello World!
print(str + "TEST")  # 输出连接的字符串 Hello World!TEST

letters='checdse'
print(letters[1:4:2])

'''类'''
class Employee:
    '所有员工的基类'
    empCount=0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name:",self.name,",Salary:",self.salary)

'''empCount 变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用 Employee.empCount 访问。

第一种方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法

self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。'''

#类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。

'''创建实例对象
以下使用类的名称 Employee 来实例化，并通过 __init__ 方法接收参数。'''
"创建Employee类的第一个对象"
emp1=Employee("Zara",2000)
"创建Employee类的第二个对象"
emp2=Employee("Manni",5000)

'''访问属性
您可以使用点号 . 来访问对象的属性。使用如下类的名称访问类变量:'''
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" %Employee.empCount)

emp1.age=7
emp1.age=8
print(emp1.age)

'''你也可以使用以下函数的方式来访问属性：

getattr(obj, name[, default]) : 访问对象的属性。
hasattr(obj,name) : 检查是否存在一个属性。
setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
delattr(obj, name) : 删除属性。'''

hasattr(emp1,'age')
getattr(emp1,'age')
setattr(emp1,'age',9)
print(emp1.age)
delattr(emp1,'age')

'''Python内置类属性
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）'''

print("Employee.__doc__:",Employee.__doc__)
print("Employee.__name__:",Employee.__name__)
print("Employee.__module:",Employee.__module__)
print("Employee.__bases__:",Employee.__bases__)
print("Employee.__dict__:",Employee.__dict__)


'''类的继承===============================================================
通过继承创建的新类称为子类或派生类，被继承的类称为基类、父类或超类。
在python中继承中的一些特点：

1、如果在子类中需要父类的构造方法就需要显示的调用父类的构造方法，或者不重写父类的构造方法。详细说明可查看：python 子类继承父类构造函数说明。
2、在调用基类的方法时，需要加上基类的类名前缀，且需要带上 self 参数变量。区别在于类中调用普通函数时并不需要带上 self 参数
3、Python 总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。
继承语法
class 派生类名(基类名)'''

class Parent: #定义父类
    parentAttr=100
    def __init__(self):
        print("调用父类构造函数")

    def parentMethod(self):
        print("调用父类方法")

    def setAttr(self, attr):
        Parent.parentAttr=attr

    def getAttr(self):
        print("父类属性：",Parent.parentAttr)

class Child(Parent): #定义子类
    def __init__(self):
        print("调用子类构造方法")

    def childMethod(self):
        print("调用子类方法")

c=Child()  #实例子类
c.childMethod() #调用子类方法
c.parentMethod() #调用父类方法
c.setAttr(200) #再次调用父类方法--设置属性值
c.getAttr()  #再次调用父类方法-获取属性值
'''
方法重写
如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法：
'''

'''文件I/O====================================================================================================================
读取键盘输入input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，但是 input 可以接收一个Python表达式作为输入，并将运算结果返回。
打开和关闭文件
你必须先用Python内置的open()函数打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写。
file object = open(file_name [, access_mode][, buffering])
模式	    r	r+	w	w+	a	a+
读	        +	+		+		+
写		    +	+	+	+	+
创建			    +	+	+	+
覆盖			    +	+		
指针在开始	+	+	+	+		
指针在结尾				    +	+

file.closed	返回true如果文件已被关闭，否则返回false。
file.mode	返回被打开文件的访问模式。
file.name	返回文件的名称。
file.softspace	如果用print输出后，必须跟一个空格符，则返回false。否则返回true。'''

fo=open('foo.text','w') #open(file, mode='r'),file:文件路径（相对或者绝对路径）
print("文件名：",fo.name)
print("是否已关闭：",fo.closed)
print("访问模式：",fo.mode)
#print("末尾是否强制加空格：",fo.softspace)
#关闭文件，File 对象的 close（）方法刷新缓冲区里任何还没写入的信息，并关闭该文件，这之后便不能再进行写入。
fo.close()


'''如何使用read()和write()方法来读取和写入文件。
write()方法
write()方法可将任何字符串写入一个打开的文件。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字
write()方法不会在字符串的结尾添加换行符('\n')
read()方法
read（）方法从一个打开的文件中读取一个字符串。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。
fileObject.read([count]) 在这里，被传递的参数是要从已打开文件中读取的字节计数。该方法从文件的开头开始读入，如果没有传入count，它会尝试尽可能多地读取更多的内容，很可能是直到文件的末尾。

文件定位
tell()方法告诉你文件内的当前位置, 换句话说，下一次的读写会发生在文件开头这么多字节之后。
seek（offset [,from]）方法改变当前文件的位置。Offset变量表示要移动的字节数。From变量指定开始移动字节的参考位置。
如果from被设为0，这意味着将文件的开头作为移动字节的参考位置。如果设为1，则使用当前的位置作为参考位置。如果它被设为2，那么该文件的末尾将作为参考位置。'''

fo=open("foo.text","w")
fo.write("www.baidu.com\nVery Good!\n")
fo.close()

fo=open("foo.text",'r+')
str=fo.read(10)
print("读取的字符串是：",str)

#查找当前位置
position=fo.tell()
print("当前的位置：",position)

#把指针再次定位到文件开头
position=fo.seek(0,0)
str=fo.read(10)
print("重新读取字符串：",str)

fo.close()

'''重命名和删除文件
os.rename(current_file_name, new_file_name)
os.remove(file_name)'''

#给出当前的目录
print(os.getcwd())


'''异常处理=============================================================================================
try:  #执行代码
    runoob()
except AssertionError as error: #发生异常执行的代码，异常的类型和 except 之后的名称相符，那么对应的 except 子句将被执行。
    print(error)
else:   #没有异常时执行的代码
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:    #不管有没有异常都要执行的代码块
    print('这句话，无论异常是否发生都会执行。')
'''
try:#正常的操作
    fh=open("testfile","w")
    fh.write("这是一个测试文件，用于测试异常！！！")
except IOError: #发生异常，执行这块代码
    print("Error：没有找到文件或读取文件失败")
else:#如果没有异常执行这块代码
    print("内容写入文件成功")
    fh.close()


#with 语句适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作，释放资源，比如文件使用后自动关闭／线程中锁的自动获取和释放等。
with open("１.txt") as file:
    data = file.read()



