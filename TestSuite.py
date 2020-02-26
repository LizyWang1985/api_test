import unittest
from test.user.test_user_login import TestUserLogin
from test.user.test_user_reg import  TestUserReg

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



