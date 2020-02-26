import unittest
import requests


'''
参考：unittest官方文档https://docs.python.org/2/library/unittest.html

unittest特点

python自带的单元测试框架，无需安装
用例执行互不干扰
提供不同范围的setUp(测试准备)和tearDown(测试清理)方法
提供丰富的断言方法
可以通过discover批量执行所有模块的用例
可以通过TestSuite(测试集)灵活的组织用例

unittest几大组成部分
estCase: 用例对象，编写测试用例时要继承该类，以具有TestCase的属性和方法
TestSuite: 测试集或测试套件，测试用例的集合，用来组织用例，支持嵌套
TestLoader: 用例加载器，用于向TestSuite中添加用例
TextTestRunner: 用例执行器（输出文本结果），一般以TestSuite为单位执行用例
TestResult: 测试结果

用例编写=========================================
新建一个test_开头（必须）的.py文件，如test_user_login.py
导入unittest
编写一个Test开头（必须）的类，并继承unittest.TestCase，做为测试类
在类中编写一个test_开头（必须）的方法，作为用例
test_user_login.py # 文件必须test_开头'''




class TestUserLogin(unittest.TestCase):# 类必须Test开头，继承TestCase才能识别为用例类
    url='http://115.28.108.130:5000/api/user/login/'

    def test_user_login_normal(self):# 一条测试用例，必须test_开头
        data={"name":"范冰冰","password":"123456"}
        res=requests.post(url=self.url,data=data)
        print(res.text)
        self.    assertIn('登录成功', res.text)  # 断言

    def test_user_login_password_wrong(self):
        data={"name":"范冰冰","password":"456231"}
        res=requests.post(url=self.url,data=data)
        self.assertIn("登录失败",res.text) #断言

if __name__ == '__main__':# 如果是直接从当前模块执行（非别的模块调用本模块）
    unittest.main(verbosity=2) # 运行本测试类所有用例,verbosity为结果显示级别

''''用例执行顺序：并非按书写顺序执行，而是按用例名ascii码先后顺序执行'''

'''常见的用例断言方法
case = unittest.TestCase()
case.assertEqual(1,2.0/2) # 通过1=2.0/2
case.assertEqual(1, True) # 通过
case.assertIs(1.0, 2.0/2) # 失败，不是同一对象
case.assertListEqual([1,2],[1,2]) # 通过（顺序要一致）
case.assertDictEqual({"a":1,"b":2},{"b":2,"a":1}) # 通过，字典本无序
case.assertIsNone({}) # 失败
case.assertFalse({}) # 通过，空字典为False
case.assertIn("h","hello") # 通过
case.assertGreater(3,2) # 通过，3>2
case.assertIsInstance({"a":1}, dict) # 通过
'''


'''用例组织及运行==============================================================================
除了使用unittest.main()运行整个测试类之外，我们还可以通过TestSuite来灵活的组织要运行的测试集
1.新建TestSuite并添加测试用例
2.使用makeSuite来制作用例集
3.使用TestLoader（用例加载器）生成测试集
4.使用discover（用例发现）遍历所有的用例
    注意：
        子目录中需要包含__init__.py文件，及应为的Python包
        所有用例因为test_*.py,包含测试类应以Test开头，并继承unittest.TestCase, 用例应以test_开头
5.测试集嵌套
'''
suite=unittest.TestSuite()
suite.addTest(TestUserLogin("test_user_login_normal")) #添加单个测试用例
suite.addTests([TestUserReg('test_user_reg_normal'),TestUserReg('test_user_reg_exist')]) # 添加多个用例

#运行测试集
unittest.TextTestRunner(verbosity=2).run(suite)  # verbosity显示级别，运行顺序为添加到suite中的顺序

'''使用makeSuite来制作用例集'''
suite1=unittest.makeSuite(TestUserLogin,'test_user_login_nomal')#使用测试类的单条用例制作测试集
suite2=unittest.makeSuite(TestUserLogin)# 使用整个测试类制作测试集合(包含该测试类所有用例)
unittest.TextTestRunner(verbosity=2).run(suite1)

'''使用TestLoader（用例加载器）生成测试集'''
suite3=unittest.TestLoader().loadTestsFromTestCase() # 加载该测试类所有用例并生成测试集
unittest.TextTestRunner(verbosity=2).run(suite3)


'''使用discover（用例发现）遍历所有的用例
注意：
子目录中需要包含__init__.py文件，及应为的Python包
所有用例因为test_*.py,包含测试类应以Test开头，并继承unittest.TestCase, 用例应以test_开头'''
suite4=unittest.defaultTestLoader.discover("../api_test/")  #遍历当前目录及子包中所有test_*.py中所有unittest用例
unittest.TextTestRunner(verbosity=2).run(suite4)

'''测试集嵌套
'''
suite5=unittest.TestSuite([suite1,suite2])  # 将两个测试集组合为一个

